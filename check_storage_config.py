"""
Force restart test - check if MediaStorage is being used
"""
import os
import sys

# Make sure we're importing fresh
if 'django' in sys.modules:
    del sys.modules['django']
if 'config.settings' in sys.modules:
    del sys.modules['config.settings']

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

import django
django.setup()

from django.conf import settings
from django.core.files.storage import default_storage

print("Current Storage Configuration:")
print("="*80)

# Check STORAGES setting (Django 4.2+)
if hasattr(settings, 'STORAGES'):
    print("STORAGES configuration:")
    for key, config in settings.STORAGES.items():
        print(f"  {key}: {config.get('BACKEND', 'N/A')}")

print(f"\ndefault_storage class: {default_storage.__class__.__name__}")
print(f"default_storage module: {default_storage.__class__.__module__}")

if hasattr(default_storage, 'bucket_name'):
    print(f"S3 Bucket: {default_storage.bucket_name}")
    print("STATUS: Using S3 Storage - CORRECT!")
elif hasattr(default_storage, 'location'):
    print(f"Local Location: {default_storage.location}")
    print("STATUS: Using FileSystemStorage - WRONG!")
    print("\nPROBLEM: Django is not loading the correct storage backend!")
    print("SOLUTION: Make sure server is restarted completely")

print("="*80)
