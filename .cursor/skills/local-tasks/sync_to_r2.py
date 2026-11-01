#!/usr/bin/env python3
"""
Sync local tasks to R2 for pickup by local Cursor instance.
Cloud Agent uses this to upload pending tasks and artifacts.
"""
import os
import sys
from pathlib import Path
import boto3

def sync_to_r2():
    """Upload local tasks and artifacts to R2."""
    
    # Load R2 credentials
    endpoint = os.environ.get('STORAGE_ENDPOINT')
    access_key = os.environ.get('STORAGE_ACCESS_KEY')
    secret_key = os.environ.get('STORAGE_SECRET_KEY')
    bucket = os.environ.get('STORAGE_BUCKET_PRIVATE')
    
    if not all([endpoint, access_key, secret_key, bucket]):
        print("❌ Missing R2 credentials")
        sys.exit(1)
    
    # Create S3 client
    s3 = boto3.client(
        's3',
        endpoint_url=endpoint,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name='auto'
    )
    
    print("🔄 Syncing local tasks to R2...")
    
    # Upload tasks
    tasks_dir = Path('/workspace/.private/local-tasks')
    if not tasks_dir.exists():
        print("  ⚠️  No local tasks directory")
        return
    
    uploaded = 0
    
    for folder in ['queue', 'in-progress', 'completed', 'failed']:
        folder_path = tasks_dir / folder
        if not folder_path.exists():
            continue
        
        for task_file in folder_path.glob('*.json'):
            r2_key = f'dot-private/mindcraft-zttts/local-tasks/{folder}/{task_file.name}'
            
            with open(task_file, 'rb') as f:
                s3.put_object(
                    Bucket=bucket,
                    Key=r2_key,
                    Body=f.read(),
                    ContentType='application/json'
                )
            
            print(f"  ✓ {folder}/{task_file.name}")
            uploaded += 1
    
    # Upload tmp artifacts (like pegasus-booking.pdf)
    tmp_dir = Path('/workspace/tmp')
    if tmp_dir.exists():
        for pdf_file in tmp_dir.glob('*.pdf'):
            r2_key = f'dot-private/mindcraft-zttts/tmp/{pdf_file.name}'
            
            with open(pdf_file, 'rb') as f:
                s3.put_object(
                    Bucket=bucket,
                    Key=r2_key,
                    Body=f.read(),
                    ContentType='application/pdf'
                )
            
            print(f"  ✓ tmp/{pdf_file.name}")
            uploaded += 1
    
    print(f"\n✅ Uploaded {uploaded} files to R2")
    print("📌 Local Cursor can now pull tasks with:")
    print("   python .cursor/skills/local-tasks/pull_and_execute.py")

if __name__ == '__main__':
    sync_to_r2()
