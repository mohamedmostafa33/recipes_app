"""
Simple listing of tar.gz contents
"""
import tarfile
import glob
import os

# Find tar.gz
tar_files = glob.glob('recipes-app-dev-*.tar.gz')
if not tar_files:
    print("ERROR: No tar.gz found!")
    exit(1)

tar_path = tar_files[0]
print(f"Analyzing: {tar_path}")
print(f"Size: {os.path.getsize(tar_path) / 1024 / 1024:.2f} MB\n")

with tarfile.open(tar_path, 'r:gz') as tf:
    members = tf.getmembers()
    
    # Count by category
    categories = {
        'media/': 0,
        'static/': 0,
        'staticfiles/': 0,
        'recipes/images/': 0,
        '__pycache__': 0,
        '.pyc': 0,
        '.sqlite3': 0,
        '.md': 0,
        'test_': 0,
        'check_': 0,
    }
    
    category_files = {k: [] for k in categories.keys()}
    other_files = []
    
    for member in members:
        if member.isdir():
            continue
            
        name = member.name
        found = False
        
        for pattern in categories:
            if pattern in name or name.endswith(pattern.replace('/', '')):
                categories[pattern] += 1
                if len(category_files[pattern]) < 10:
                    category_files[pattern].append(name)
                found = True
                break
        
        if not found and len(other_files) < 20:
            other_files.append(name)
    
    print("="*80)
    print("EXCLUDED FILES FOUND IN PACKAGE:")
    print("="*80)
    
    for pattern, count in categories.items():
        if count > 0:
            print(f"\n{pattern}: {count} files")
            for f in category_files[pattern][:5]:
                print(f"  - {f}")
            if len(category_files[pattern]) > 5:
                print(f"  ... and {count - 5} more")
    
    print("\n" + "="*80)
    print("SAMPLE OF OTHER FILES (first 20):")
    print("="*80)
    for f in other_files:
        print(f"  {f}")
    
    print(f"\n\nTotal files: {len([m for m in members if not m.isdir()])}")
