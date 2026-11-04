"""Render the four published evidence pages. Inspect images before publishing."""
import argparse
from pathlib import Path
import fitz

base = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--sources', type=Path, default=base / 'sources')
parser.add_argument('--output', type=Path, default=base / 'rendered-pages')
args = parser.parse_args()
args.output.mkdir(parents=True, exist_ok=True)
for name, page in [('scaling', 7), ('quality', 5), ('molmoact2', 11), ('foundry', 25)]:
    with fitz.open(args.sources / f'{name}.pdf') as doc:
        doc[page - 1].get_pixmap(matrix=fitz.Matrix(1.5, 1.5)).save(
            args.output / f'{name}-p{page}.png')
print('Rendered candidate pages to', args.output, '; visual review required.')
