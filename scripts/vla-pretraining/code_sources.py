"""Download selected official source files at the commits used by the published note.

Publication version: pins commits instead of resolving rolling main; does not
execute downloaded source code. See code-manifest.json for repositories/files.
"""
import json
from pathlib import Path
import requests

BASE = Path(__file__).resolve().parent
DEST = BASE / 'sources'
DEST.mkdir(parents=True, exist_ok=True)
manifest = json.loads((BASE / 'code-manifest.json').read_text())
for name, entry in manifest.items():
    for file in entry['files']:
        url = f"https://raw.githubusercontent.com/{entry['repo']}/{entry['commit']}/{file}"
        response = requests.get(url, timeout=120)
        response.raise_for_status()
        (DEST / f"{name}--{file.replace('/', '__')}").write_text(response.text)
(DEST / 'code-manifest.json').write_text(json.dumps(manifest, indent=2))
print('Downloaded pinned source files to', DEST)
