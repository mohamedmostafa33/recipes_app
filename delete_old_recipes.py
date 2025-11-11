"""
Delete all existing recipes (they use old storage)
"""
import os
import sys
import django

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from recipes.models import Recipe

def delete_all_recipes():
    """Delete all recipes"""
    recipes = Recipe.objects.all()
    count = recipes.count()
    
    if count == 0:
        print("No recipes to delete")
        return
    
    print(f"Found {count} recipe(s)")
    for recipe in recipes:
        print(f"  - {recipe.title} (ID: {recipe.id})")
    
    confirm = input(f"\nDelete all {count} recipe(s)? (yes/no): ")
    
    if confirm.lower() == 'yes':
        recipes.delete()
        print(f"\nDeleted {count} recipe(s) successfully!")
    else:
        print("\nCancelled")

if __name__ == '__main__':
    delete_all_recipes()
