"""
Check recipes in database and their image paths
"""
import os
import sys
import django

# Setup Django
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from recipes.models import Recipe
from django.core.files.storage import default_storage

def check_recipes():
    """Check all recipes and their images"""
    print("Checking Recipes Database...")
    print("="*80)
    
    recipes = Recipe.objects.all().order_by('-id')
    
    if not recipes:
        print("❌ No recipes found in database")
        return
    
    print(f"✅ Found {recipes.count()} recipe(s)\n")
    
    for recipe in recipes:
        print(f"Recipe ID: {recipe.id}")
        print(f"Title: {recipe.title}")
        print(f"Author: {recipe.author.username}")
        print(f"Created: {recipe.created_at}")
        
        if recipe.image:
            print(f"Image Field Value: {recipe.image.name}")
            print(f"Image URL: {recipe.image.url}")
            print(f"Storage Class: {recipe.image.storage.__class__.__name__}")
            
            # Check if file exists
            if recipe.image.storage.exists(recipe.image.name):
                print(f"✅ Image exists in storage")
                print(f"   Storage location: {getattr(recipe.image.storage, 'location', 'S3')}")
            else:
                print(f"❌ Image NOT found in storage")
            
            # Check local file
            local_path = os.path.join('media', recipe.image.name)
            if os.path.exists(local_path):
                print(f"⚠️  Image exists LOCALLY at: {local_path}")
            else:
                print(f"ℹ️  Image NOT in local media folder")
        else:
            print(f"⚠️  No image attached")
        
        print("-"*80)
    
    # Check default storage
    print(f"\n📦 DEFAULT_FILE_STORAGE Configuration:")
    print(f"   Class: {default_storage.__class__.__name__}")
    print(f"   Module: {default_storage.__class__.__module__}")
    if hasattr(default_storage, 'location'):
        print(f"   Location: {default_storage.location}")
    if hasattr(default_storage, 'bucket_name'):
        print(f"   S3 Bucket: {default_storage.bucket_name}")
    
    print("="*80)

if __name__ == '__main__':
    check_recipes()
