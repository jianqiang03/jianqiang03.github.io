"""Render an existing note from its canonical report.md; retain its page shell/styles.
Usage: python scripts/render-paper-note.py dm05 [vpp2 dyna-2]
Requires: markdown, beautifulsoup4. Does not deploy.
"""
from pathlib import Path
import hashlib
import sys
import markdown
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
FOCUS = {
    'dm05': ['从一条示教追到模型', '历史如何成为 token', '一次训练更新', '推理如何用同一'],
    'vpp2': ['代码路径', '精确到损失', '梯度与冻结', '数据选择本身'],
    'dyna-2': ['实现主线', '梯度路径', '损失实现', '系统改进如何'],
}
for slug in sys.argv[1:]:
    if slug not in FOCUS:
        raise SystemExit(f'Unknown note: {slug}')
    directory = ROOT / 'notes' / slug
    shell = BeautifulSoup((directory / 'index.html').read_text(), 'html.parser')
    body = BeautifulSoup(markdown.markdown((directory / 'report.md').read_text(), extensions=['tables', 'fenced_code']), 'html.parser')
    toc = []
    focus = []
    for i, heading in enumerate(body.select('h2'), 1):
        heading['id'] = f's{i}'
        toc.append((heading['id'], heading.get_text()))
    for i, heading in enumerate(body.select('h3'), 1):
        heading['id'] = f'm{i}'
        if any(term in heading.get_text() for term in FOCUS[slug]):
            focus.append((heading['id'], heading.get_text()))
    nav = body.new_tag('blockquote')
    title = body.new_tag('strong')
    title.string = '实现深读 · 从样本到训练，再到执行'
    nav.append(title)
    for anchor, label in focus:
        nav.append(body.new_tag('br'))
        link = body.new_tag('a', href='#' + anchor)
        link.string = label
        nav.append(link)
    first = body.select_one('blockquote')
    first.insert_after(nav)
    for table in body.select('table'):
        table.wrap(body.new_tag('div', attrs={'class': 'table-scroll', 'tabindex': '0', 'role': 'region', 'aria-label': '数据表格，可横向滚动'}))
    for im in body.select('img'):
        im['loading'] = 'lazy'
        im['tabindex'] = '0'
        im['title'] = '点击放大；Esc 关闭'
    main = shell.select_one('main')
    main.clear()
    for child in list(body.contents):
        main.append(child.extract())
    footer = shell.new_tag('footer')
    footer.string = '2026-11-03 · 实现深读更新。论文、报告与固定版本代码分别标注；未运行模型训练或推理。原始图表归作者所有。'
    main.append(footer)
    aside = shell.select_one('aside')
    for link in list(aside.select('a[href^="#"]')):
        link.decompose()
    for anchor, label in toc:
        link = shell.new_tag('a', href='#' + anchor)
        link.string = label
        aside.append(link)
    version = hashlib.sha256((ROOT / 'notes/reading.css').read_bytes()).hexdigest()[:12]
    for link in shell.select('link[rel="stylesheet"]'):
        if 'reading.css' in link.get('href', ''):
            link['href'] = '../reading.css?v=' + version
    (directory / 'index.html').write_text(str(shell))
    print('Rendered', slug)
