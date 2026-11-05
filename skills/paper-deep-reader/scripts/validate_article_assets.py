#!/usr/bin/env python3
"""Check saved article assets, not prose quality or scientific correctness."""
import argparse
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('report', type=Path)
    parser.add_argument('--manifest', required=True, type=Path)
    parser.add_argument('--source-map', required=True, type=Path)
    parser.add_argument('--text-only', action='store_true')
    args = parser.parse_args()
    errors = []
    try:
        text = args.report.read_text(encoding='utf-8')
        manifest = json.loads(args.manifest.read_text(encoding='utf-8'))
        source = json.loads(args.source_map.read_text(encoding='utf-8'))
    except (OSError, ValueError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 2
    root = args.report.resolve().parent
    images = set()
    # Standard inline Markdown links, optionally with an angle-bracket target.
    for match in re.finditer(r'(!?)\[[^\]]*\]\((<[^>]+>|[^\s)]+)(?:\s+"[^"]*")?\)', text):
        raw = match[2].strip('<>')
        url = urlsplit(raw)
        if url.scheme or url.netloc or not url.path:
            continue
        path = (root / unquote(url.path)).resolve()
        valid_target = path.is_file() or (not match[1] and path.is_dir() and (path / 'index.html').is_file())
        if not valid_target:
            errors.append(f'Missing local target: {raw}')
        if match[1]:
            images.add(path)
    visuals = manifest.get('visuals') if isinstance(manifest, dict) else None
    if not isinstance(visuals, list) or not visuals:
        errors.append('Manifest must have a nonempty visuals list.')
        visuals = []
    key_count = 0
    for item in visuals:
        if not isinstance(item, dict):
            errors.append('Invalid manifest entry.')
            continue
        label = item.get('label', '(unlabeled)')
        if not isinstance(item.get('key'), bool) or not item.get('classification_reason'):
            errors.append(f'{label}: missing key classification or reason.')
        if item.get('key') is not True:
            continue
        key_count += 1
        if item.get('selected_for_report') is not True:
            errors.append(f'{label}: key visual not selected.')
        if args.text_only:
            review = item.get('text_review', {})
            if review.get('status') != 'complete' or not review.get('sources'):
                errors.append(f'{label}: incomplete text evidence review.')
        else:
            asset = item.get('selected_asset')
            if not isinstance(asset, str) or (root / asset).resolve() not in images:
                errors.append(f'{label}: selected asset not embedded in report.')
            if item.get('visual_verification') not in ('complete', 'externally-verified') or item.get('crop_review_required') is not False:
                errors.append(f'{label}: visual review not recorded as complete.')
    paper = source.get('paper', {}) if isinstance(source, dict) else {}
    if not paper.get('title') or not paper.get('sources'):
        errors.append('Source map lacks paper title or sources.')
    if errors:
        print('\n'.join('ERROR: ' + e for e in errors))
        return 1
    print(f'PASS assets: {len(images)} local images, {key_count} key visuals; source record present.')
    print('Scope: no network, prose, formula, pixel-verification or factual validation. Recorded review status is not proof of review.')
    if args.text_only:
        print('Text-only: manually confirm each key evidence card appears in the article.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
