"""
Test importing storage backends
"""
import sys
import os

sys.path.insert(0, r'E:\My programs\VS Code projects\GitHub\recipes_app')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Try to import the storage backends
try:
    from config.storage_backends import MediaStorage, StaticStorage
    print("SUCCESS: Storage backends imported successfully")
    print(f"MediaStorage class: {MediaStorage}")
    print(f"StaticStorage class: {StaticStorage}")
    print(f"MediaStorage location: {MediaStorage.location}")
    
    # Try to instantiate
    media_storage = MediaStorage()
    print(f"MediaStorage instance created: {media_storage}")
    print(f"Bucket name: {media_storage.bucket_name}")
    
except Exception as e:
    print(f"ERROR: Failed to import storage backends")
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
