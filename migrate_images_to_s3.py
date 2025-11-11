"""
Migrate existing recipe images to S3
"""
import os
import sys
import django

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from recipes.models import Recipe
from django.core.files import File
from config.storage_backends import MediaStorage

def migrate_images_to_s3():
    """Migrate all recipe images from local storage to S3"""
    print("Migrating Recipe Images to S3...")
    print("="*80)
    
    recipes = Recipe.objects.filter(image__isnull=False)
    
    if not recipes:
        print("No recipes with images found")
        return
    
    s3_storage = MediaStorage()
    migrated = 0
    errors = 0
    
    for recipe in recipes:
        try:
            print(f"\nProcessing Recipe #{recipe.id}: {recipe.title}")
            old_image_name = recipe.image.name
            print(f"  Old path: {old_image_name}")
            
            # Check if already on S3
            if isinstance(recipe.image.storage, MediaStorage):
                print(f"  Already on S3, skipping")
                continue
            
            # Check if local file exists
            local_path = os.path.join('media', old_image_name)
            if not os.path.exists(local_path):
                # Try in recipes/images directly
                local_path = os.path.join(old_image_name)
                if not os.path.exists(local_path):
                    print(f"  ERROR: Local file not found at {local_path}")
                    errors += 1
                    continue
            
            # Read local file
            with open(local_path, 'rb') as f:
                file_content = File(f)
                
                # Save to S3
                new_name = s3_storage.save(old_image_name, file_content)
                print(f"  Uploaded to S3: {new_name}")
                print(f"  URL: {s3_storage.url(new_name)}")
                
                # Update recipe to use new storage
                recipe.image.name = new_name
                recipe.image.storage = s3_storage
                recipe.save(update_fields=['image'])
                
                migrated += 1
                print(f"  SUCCESS")
                
        except Exception as e:
            print(f"  ERROR: {e}")
            errors += 1
            import traceback
            traceback.print_exc()
    
    print("\n" + "="*80)
    print(f"Migration completed:")
    print(f"  Migrated: {migrated}")
    print(f"  Errors: {errors}")
    print("="*80)

if __name__ == '__main__':
    migrate_images_to_s3()
