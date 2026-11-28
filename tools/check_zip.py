#!/usr/bin/env python3
"""Pre-release check for a plugin zip: every require/include that uses the plugin's
own directory (constant ending in _DIR / _PATH, __DIR__, dirname(__FILE__),
plugin_dir_path(__FILE__)) must point to a file that is inside the zip.
Usage: python3 tools/check_zip.py path/to/plugin.zip   (exit 1 on any missing file)"""
import re, sys, zipfile, posixpath

z = zipfile.ZipFile(sys.argv[1])
names = set(n for n in z.namelist() if not n.endswith('/'))
pat = re.compile(r"""(?:require|include)(?:_once)?\s*\(?\s*(?:[A-Z_]+(?:_DIR|_PATH)|__DIR__|dirname\(\s*__FILE__\s*\)|plugin_dir_path\(\s*__FILE__\s*\))\s*\.\s*['"]([^'"]+)['"]""")
missing = []
for n in names:
    if not n.endswith('.php'):
        continue
    src = z.read(n).decode('utf-8', 'replace')
    root = n.split('/')[0] if '/' in n else ''
    for m in pat.finditer(src):
        rel = m.group(1).lstrip('/')
        # constants like LI_PLUGIN_DIR are the plugin root; __DIR__ is the file's own folder
        base = root if re.match(r'[A-Z_]+(_DIR|_PATH)', m.group(0).split('.')[0].split()[-1].strip('( ')) else posixpath.dirname(n)
        target = posixpath.normpath(posixpath.join(base, rel))
        if target not in names:
            missing.append(f"{n}: needs {target}")
for x in sorted(set(missing)):
    print("MISSING", x)
print("OK" if not missing else f"{len(set(missing))} missing file(s)")
sys.exit(1 if missing else 0)
