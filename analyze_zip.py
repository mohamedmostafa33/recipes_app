"""
List contents of zappa package to find unwanted files
"""
import tarfile
import os
from collections import defaultdict
import glob

# Find the tar.gz file
tar_files = glob.glob('recipes-app-dev-*.tar.gz')
if not tar_files:
    print("ERROR: No recipes-app-dev-*.tar.gz found!")
    exit(1)

zip_path = tar_files[0]
print(f"Found: {zip_path}")

print("="*80)
print(f"Analyzing: {zip_path}")
print(f"File size: {os.path.getsize(zip_path) / 1024 / 1024:.2f} MB")
print("="*80)

# Track folder sizes
folder_sizes = defaultdict(int)
unwanted_files = {
    'media': [],
    'static': [],
    'staticfiles': [],
    'recipes/images': [],
    '__pycache__': [],
    'db.sqlite3': [],
    '.pyc': [],
    'env': [],
}

with tarfile.open(zip_path, 'r:gz') as tf:
    total_files = len(tf.getnames())
    members = tf.getmembers()
    total_size = sum(member.size for member in members)
    
    print(f"\nTotal files: {total_files}")
    print(f"Uncompressed size: {total_size / 1024 / 1024:.2f} MB\n")
    
    # Analyze each file
    for member in members:
        filename = member.name
        size = member.size
        
        # Skip directories
        if member.isdir():
            continue
        
        # Get top-level folder
        if '/' in filename:
            top_folder = filename.split('/')[0]
            folder_sizes[top_folder] += size
        else:
            folder_sizes['<root>'] += size
        
        # Check for unwanted files
        if filename.startswith('media/'):
            unwanted_files['media'].append((filename, size))
        elif filename.startswith('static/'):
            unwanted_files['static'].append((filename, size))
        elif filename.startswith('staticfiles/'):
            unwanted_files['staticfiles'].append((filename, size))
        elif filename.startswith('recipes/images/'):
            unwanted_files['recipes/images'].append((filename, size))
        elif '__pycache__' in filename:
            unwanted_files['__pycache__'].append((filename, size))
        elif filename == 'db.sqlite3' or filename.endswith('/db.sqlite3'):
            unwanted_files['db.sqlite3'].append((filename, size))
        elif filename.endswith('.pyc'):
            unwanted_files['.pyc'].append((filename, size))
        elif filename.startswith('env/'):
            unwanted_files['env'].append((filename, size))

# Print top folders by size
print("\n" + "="*80)
print("TOP FOLDERS BY SIZE:")
print("="*80)
sorted_folders = sorted(folder_sizes.items(), key=lambda x: x[1], reverse=True)
for folder, size in sorted_folders[:15]:
    print(f"{folder:30s} {size/1024/1024:>10.2f} MB")

# Print unwanted files
print("\n" + "="*80)
print("UNWANTED FILES (Should be excluded):")
print("="*80)

total_unwanted_size = 0
for category, files in unwanted_files.items():
    if files:
        category_size = sum(f[1] for f in files)
        total_unwanted_size += category_size
        print(f"\n{category}: {len(files)} files, {category_size/1024/1024:.2f} MB")
        # Show first 5 files
        for filename, size in files[:5]:
            print(f"  - {filename} ({size/1024:.2f} KB)")
        if len(files) > 5:
            print(f"  ... and {len(files)-5} more")

print("\n" + "="*80)
print(f"TOTAL UNWANTED SIZE: {total_unwanted_size/1024/1024:.2f} MB")
print(f"Potential savings: {total_unwanted_size/total_size*100:.1f}% of package")
print("="*80)
