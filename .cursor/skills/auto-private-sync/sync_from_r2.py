#!/usr/bin/env python3
"""
Auto-sync .private/ directory from R2 storage.
Called by auto-private-sync skill when .private/ is missing.
"""
import boto3
import os
import sys
from pathlib import Path

def main():
    # Check R2 credentials
    required_vars = ['STORAGE_ENDPOINT', 'STORAGE_ACCESS_KEY', 'STORAGE_SECRET_KEY', 'STORAGE_BUCKET_PRIVATE']
    missing = [v for v in required_vars if not os.environ.get(v)]
    
    if missing:
        print(f"❌ Error: Missing R2 credentials: {', '.join(missing)}")
        print("Add them to Cursor Cloud Secrets (cursor.com → Cloud Agents → Secrets)")
        sys.exit(1)
    
    # R2 credentials
    endpoint = os.environ['STORAGE_ENDPOINT']
    access_key = os.environ['STORAGE_ACCESS_KEY']
    secret_key = os.environ['STORAGE_SECRET_KEY']
    bucket_name = os.environ['STORAGE_BUCKET_PRIVATE']
    region = os.environ.get('STORAGE_REGION', 'auto')
    
    # Create S3 client for R2
    s3 = boto3.client(
        's3',
        endpoint_url=endpoint,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name=region
    )
    
    # Create .private directory
    private_dir = Path('/workspace/.private')
    private_dir.mkdir(exist_ok=True)
    
    print(f"📥 Downloading .private files from R2 bucket...")
    
    try:
        # List all objects with dot-private/mindcraft-zttts/ prefix
        response = s3.list_objects_v2(Bucket=bucket_name, Prefix='dot-private/mindcraft-zttts/')
        
        if 'Contents' not in response:
            print("⚠️  No .private files found in R2 bucket")
            sys.exit(0)
        
        downloaded = 0
        skipped = 0
        
        for obj in response['Contents']:
            key = obj['Key']
            
            # Skip directory markers
            if key.endswith('/'):
                continue
            
            # Get filename relative to dot-private/mindcraft-zttts/
            filename = key.replace('dot-private/mindcraft-zttts/', '')
            local_path = private_dir / filename
            
            # Skip if already exists
            if local_path.exists():
                skipped += 1
                continue
            
            # Create subdirectories if needed
            local_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Download file
            s3.download_file(bucket_name, key, str(local_path))
            downloaded += 1
            
            # Report progress for large downloads
            if downloaded % 10 == 0:
                print(f"  Downloaded {downloaded} files...")
        
        print(f"\n✅ Sync complete!")
        print(f"   Downloaded: {downloaded} files")
        if skipped > 0:
            print(f"   Skipped (already exist): {skipped} files")
        
        # List some downloaded files
        if downloaded > 0:
            print("\nKey files available:")
            important_files = [
                'imap-triage.env',
                'life-queue.fu.md',
                'CPU.md',
                'imap-gmail.env',
            ]
            for f in important_files:
                path = private_dir / f
                if path.exists():
                    print(f"  ✓ {f}")
        
    except Exception as e:
        print(f"\n❌ Error during sync: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()
