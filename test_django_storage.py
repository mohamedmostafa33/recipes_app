"""
Test Django file upload to S3 directly
"""
import os
import sys
import django

# Setup Django
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from config.storage_backends import MediaStorage

def test_django_storage():
    """Test Django's storage backend"""
    print("Testing Django Storage Backend...")
    print("="*50)
    
    # Test content
    test_content = b"Test image file from Django"
    test_filename = "recipes/images/test_image.jpg"
    
    try:
        # Test 1: Default storage
        print("\n1. Testing DEFAULT_FILE_STORAGE...")
        print(f"   Storage class: {default_storage.__class__.__name__}")
        print(f"   Location: {getattr(default_storage, 'location', 'N/A')}")
        
        # Save file
        file_obj = ContentFile(test_content, name=test_filename)
        saved_path = default_storage.save(test_filename, file_obj)
        
        print(f"✅ File saved successfully!")
        print(f"   Path: {saved_path}")
        print(f"   URL: {default_storage.url(saved_path)}")
        
        # Check if exists
        if default_storage.exists(saved_path):
            print(f"✅ File exists on storage")
        else:
            print(f"❌ File doesn't exist on storage")
        
        # Cleanup
        default_storage.delete(saved_path)
        print(f"✅ File deleted successfully")
        
        print("\n" + "="*50)
        print("🎉 Django storage is working correctly!")
        print("="*50)
        
        return True
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print(f"   Type: {type(e).__name__}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    test_django_storage()
