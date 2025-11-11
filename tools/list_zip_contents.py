import sys
from zipfile import ZipFile

def human(n):
    for u in ['B','KB','MB','GB']:
        if n<1024:
            return f"{n:.1f}{u}"
        n/=1024
    return f"{n:.1f}TB"

if len(sys.argv)<2:
    print('Usage: python list_zip_contents.py <zipfile>')
    sys.exit(1)

zf = sys.argv[1]
with ZipFile(zf) as z:
    infos = z.infolist()
    print(f'Total entries: {len(infos)}')
    entries = []
    for i in infos:
        entries.append((i.filename, i.file_size, i.compress_size))
    # sort by file_size desc
    entries.sort(key=lambda x: x[1], reverse=True)
    print('\nTop 40 files by uncompressed size:')
    for fn, fs, cs in entries[:40]:
        print(f'{human(fs):>8}  {human(cs):>8}  {fn}')

    # show counts for common folders
    def cnt(prefix):
        return sum(1 for fn,_,_ in entries if fn.startswith(prefix))
    print('\nCounts:')
    for p in ['media/', 'recipes/images/', 'static/', 'staticfiles/', 'env/', 'env/', 'site-packages/']:
        print(f"  {p:<20} {cnt(p):>5}")
