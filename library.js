/* The HTML cards are the source of truth; no separate article manifest. */
(() => {
  const cards = Array.from(document.querySelectorAll('.note-card'));
  const input = document.querySelector('#note-search');
  if (!input || !cards.length) return;
  const filters = Array.from(document.querySelectorAll('[data-filter]'));
  const perPage = 6;
  let topic = 'all';
  let page = 1;
  const normalize = value => value.normalize('NFKC').toLocaleLowerCase().replace(/\s+/g, ' ').trim();
  const indexed = cards.map(card => ({card, text: normalize(card.textContent), topics: (card.dataset.topics || '').split(/\s+/)}));
  const status = document.querySelector('#note-status');
  const pagination = document.querySelector('#note-pagination');
  const previous = document.querySelector('#previous-page');
  const next = document.querySelector('#next-page');
  document.querySelector('.library-tools').hidden = false;
  document.querySelector('.library-status').hidden = false;
  document.querySelector('#note-total').textContent = `${cards.length} 篇笔记`;
  filters.forEach(button => {
    const key = button.dataset.filter;
    const count = key === 'all' ? cards.length : indexed.filter(item => item.topics.includes(key)).length;
    const badge = document.createElement('span');
    badge.className = 'filter-count';
    badge.textContent = count;
    button.append(badge);
    button.addEventListener('click', () => {topic = key; page = 1; render();});
  });
  function render() {
    const terms = normalize(input.value).split(' ').filter(Boolean);
    const matches = indexed.filter(item => (topic === 'all' || item.topics.includes(topic)) && terms.every(term => item.text.includes(term)));
    const pages = Math.max(1, Math.ceil(matches.length / perPage));
    page = Math.min(page, pages);
    cards.forEach(card => {card.hidden = true;});
    matches.slice((page - 1) * perPage, page * perPage).forEach(item => {item.card.hidden = false;});
    filters.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.filter === topic)));
    status.textContent = matches.length ? `共 ${matches.length} 篇 · 显示 ${(page - 1) * perPage + 1}–${Math.min(page * perPage, matches.length)} 篇` : '找到 0 篇笔记';
    document.querySelector('#empty-notes').hidden = matches.length !== 0;
    pagination.hidden = pages <= 1;
    document.querySelector('#page-label').textContent = `第 ${page} / ${pages} 页`;
    previous.disabled = page <= 1;
    next.disabled = page >= pages;
  }
  input.addEventListener('input', () => {page = 1; render();});
  previous.addEventListener('click', () => {if (page > 1) {page--; render();document.querySelector('#notes').scrollIntoView({block:'start'});}});
  next.addEventListener('click', () => {page++;render();document.querySelector('#notes').scrollIntoView({block:'start'});});
  document.querySelector('#reset-notes').addEventListener('click', () => {topic = 'all';page = 1;input.value = '';render();input.focus();});
  render();
})();
