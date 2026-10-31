#!/usr/bin/env python3
"""
LOCAL CURSOR SCRIPT: Pull and execute tasks from R2 queue.
Run this on your local Windows/macOS machine with Cursor.

Prerequisites:
- boto3: pip install boto3
- R2 credentials in .private/storage.env or environment variables
- Task handlers in task_handlers/ directory

Usage:
    python .cursor/skills/local-tasks/pull_and_execute.py [--dry-run]
"""
import json
import sys
import os
from pathlib import Path
from datetime import datetime, timezone
import argparse

try:
    import boto3
except ImportError:
    print("❌ boto3 not installed. Run: pip install boto3")
    sys.exit(1)

def load_r2_config():
    """Load R2 credentials from environment or .private/storage.env"""
    
    # Try environment first
    endpoint = os.environ.get('STORAGE_ENDPOINT')
    access_key = os.environ.get('STORAGE_ACCESS_KEY')
    secret_key = os.environ.get('STORAGE_SECRET_KEY')
    bucket = os.environ.get('STORAGE_BUCKET_PRIVATE')
    
    # Try .private/storage.env
    if not all([endpoint, access_key, secret_key, bucket]):
        env_file = Path('.private/storage.env')
        if env_file.exists():
            with open(env_file) as f:
                for line in f:
                    if '=' in line and not line.startswith('#'):
                        key, value = line.strip().split('=', 1)
                        os.environ[key] = value
            endpoint = os.environ.get('STORAGE_ENDPOINT')
            access_key = os.environ.get('STORAGE_ACCESS_KEY')
            secret_key = os.environ.get('STORAGE_SECRET_KEY')
            bucket = os.environ.get('STORAGE_BUCKET_PRIVATE')
    
    if not all([endpoint, access_key, secret_key, bucket]):
        print("❌ Missing R2 credentials. Set STORAGE_* environment variables.")
        sys.exit(1)
    
    return endpoint, access_key, secret_key, bucket

def pull_tasks_from_r2(s3, bucket):
    """Pull pending tasks from R2."""
    
    print("📥 Pulling tasks from R2...")
    
    try:
        response = s3.list_objects_v2(
            Bucket=bucket,
            Prefix='dot-private/mindcraft-zttts/local-tasks/queue/'
        )
        
        if 'Contents' not in response:
            print("✓ No pending tasks")
            return []
        
        tasks = []
        for obj in response['Contents']:
            key = obj['Key']
            if not key.endswith('.json'):
                continue
            
            # Download task
            task_obj = s3.get_object(Bucket=bucket, Key=key)
            task_data = json.loads(task_obj['Body'].read().decode('utf-8'))
            
            if task_data.get('status') == 'pending':
                tasks.append((key, task_data))
                print(f"  ✓ {task_data['id']} ({task_data['type']}) - {task_data['priority']}")
        
        return tasks
    
    except Exception as e:
        print(f"❌ Error pulling tasks: {e}")
        return []

def execute_task(task_data, dry_run=False):
    """Execute a task based on its type."""
    
    task_type = task_data['type']
    task_id = task_data['id']
    
    print(f"\n🔧 Executing task: {task_id} ({task_type})")
    
    if dry_run:
        print("  [DRY RUN] Would execute task")
        return {"status": "dry_run", "message": "Dry run mode"}
    
    # Import task handler
    try:
        handler_module = __import__(f'task_handlers.{task_type}', fromlist=['execute'])
        result = handler_module.execute(task_data)
        return result
    except ImportError:
        print(f"  ⚠️  No handler for task type: {task_type}")
        print(f"  📄 Task details:")
        print(json.dumps(task_data, indent=2))
        return {"status": "no_handler", "message": f"No handler for {task_type}"}
    except Exception as e:
        print(f"  ❌ Execution failed: {e}")
        import traceback
        traceback.print_exc()
        return {"status": "error", "message": str(e)}

def mark_task_complete(s3, bucket, task_key, task_data, result):
    """Mark task as complete and move to completed/."""
    
    # Update task
    task_data['status'] = 'completed' if result.get('status') == 'success' else 'failed'
    task_data['execution']['executed_at'] = datetime.now(timezone.utc).isoformat()
    task_data['execution']['executed_by'] = 'local-cursor'
    task_data['execution']['result'] = result
    
    # Move to completed or failed
    new_folder = 'completed' if task_data['status'] == 'completed' else 'failed'
    new_key = task_key.replace('/queue/', f'/{new_folder}/')
    
    # Upload updated task
    s3.put_object(
        Bucket=bucket,
        Key=new_key,
        Body=json.dumps(task_data, indent=2, ensure_ascii=False).encode('utf-8'),
        ContentType='application/json'
    )
    
    # Delete from queue
    s3.delete_object(Bucket=bucket, Key=task_key)
    
    print(f"✅ Task marked as {task_data['status']}")

def main():
    parser = argparse.ArgumentParser(description='Pull and execute local tasks from R2')
    parser.add_argument('--dry-run', action='store_true', help='Show tasks without executing')
    args = parser.parse_args()
    
    print("🚀 Local Task Executor")
    print("=" * 50)
    
    # Load R2 config
    endpoint, access_key, secret_key, bucket = load_r2_config()
    
    # Create S3 client
    s3 = boto3.client(
        's3',
        endpoint_url=endpoint,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name='auto'
    )
    
    # Pull tasks
    tasks = pull_tasks_from_r2(s3, bucket)
    
    if not tasks:
        print("\n✓ No tasks to execute")
        return
    
    # Execute tasks by priority
    tasks.sort(key=lambda x: {'urgent': 0, 'high': 1, 'normal': 2, 'low': 3}.get(x[1].get('priority', 'normal'), 2))
    
    for task_key, task_data in tasks:
        result = execute_task(task_data, dry_run=args.dry_run)
        
        if not args.dry_run:
            mark_task_complete(s3, bucket, task_key, task_data, result)
    
    print("\n🎉 All tasks processed!")

if __name__ == '__main__':
    main()
