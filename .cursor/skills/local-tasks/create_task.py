#!/usr/bin/env python3
"""
Create a local task for execution by local Cursor instance.
Cloud Agent uses this to create tasks that require local capabilities.
"""
import json
import sys
import argparse
from pathlib import Path
from datetime import datetime, timezone

def create_task(task_id, task_type, priority, context_description, payload_dict=None):
    """Create a new local task."""
    
    # Ensure directories exist
    queue_dir = Path('/workspace/.private/local-tasks/queue')
    queue_dir.mkdir(parents=True, exist_ok=True)
    
    # Create task structure
    task = {
        "id": task_id,
        "type": task_type,
        "status": "pending",
        "priority": priority,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "created_by": "cloud-agent",
        "context": {
            "description": context_description,
            "agent_run": "cloud-agent-current-run",
            "workspace": "/workspace"
        },
        "payload": payload_dict or {},
        "execution": {
            "executed_at": None,
            "executed_by": None,
            "result": None,
            "logs": []
        }
    }
    
    # Save task
    task_file = queue_dir / f"{task_id}.json"
    with open(task_file, 'w', encoding='utf-8') as f:
        json.dump(task, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Task created: {task_file}")
    print(f"   ID: {task_id}")
    print(f"   Type: {task_type}")
    print(f"   Priority: {priority}")
    
    return task_file

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create local task for local Cursor execution')
    parser.add_argument('--id', required=True, help='Unique task ID')
    parser.add_argument('--type', required=True, help='Task type (email_send, file_access, etc.)')
    parser.add_argument('--priority', default='normal', help='Priority: low, normal, high, urgent')
    parser.add_argument('--context', required=True, help='Task description/context')
    parser.add_argument('--payload', help='JSON payload for task execution')
    
    args = parser.parse_args()
    
    payload = None
    if args.payload:
        try:
            payload = json.loads(args.payload)
        except json.JSONDecodeError as e:
            print(f"❌ Invalid JSON payload: {e}")
            sys.exit(1)
    
    create_task(args.id, args.type, args.priority, args.context, payload)
