# -*- coding: utf-8 -*-
"""Генератор одностраничника «Банк решений ЕГЭ» из репозитория EGEINF.
Сканирует kompege/zadachi_po_nomeru/ и собирает самодостаточный site/index.html.
Запуск: python scripts/build_site.py  (из корня репозитория)
"""
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ZPN = ROOT / "kompege" / "zadachi_po_nomeru"
OUT = ROOT / "site" / "index.html"

tasks = []  # {num, id, kind: py|img|table, part?, code?, file?, data: [...]}
DATA_EXT = (".txt", ".xls", ".xlsx", ".ods")
for d in sorted(ZPN.iterdir()):
    if not d.is_dir() or not d.name.startswith("task"):
        continue
    if d.name == "task192021":
        num = 19
    else:
        num = int(d.name[4:])
    if num == 27:
        for sub in sorted(d.iterdir()):
            if not (sub.is_dir() and sub.name.isdigit()):
                continue
            tid = sub.name
            for f in sorted(sub.glob("27_[AB]_*.py")):
                part = f.name.split("_")[1]
                data = [p.name for p in sub.iterdir() if p.suffix.lower() in DATA_EXT]
                tasks.append({"num": 27, "id": tid, "part": part, "kind": "py",
                              "code": f.read_text(encoding="utf-8"),
                              "data": sorted(data)})
    else:
        def data_for(tid):
            return sorted(p.name for p in d.iterdir()
                          if p.stem.startswith(f"{num}_{tid}") or p.stem.startswith(f"{num}.{num}_{tid}")
                          if p.suffix.lower() in DATA_EXT)
        for f in sorted(d.iterdir()):
            m = re.match(r"^(\d{4,6})$", f.stem)
            if not m:
                continue  # пропускаем *_slow, *bad, файлы данных N_ID.*
            tid = m.group(1)
            ext = f.suffix.lower()
            if ext == ".py":
                tasks.append({"num": num, "id": tid, "kind": "py",
                              "code": f.read_text(encoding="utf-8"), "data": data_for(tid)})
            elif ext in (".png", ".jpg", ".jpeg"):
                tasks.append({"num": num, "id": tid, "kind": "img",
                              "file": f.name, "data": data_for(tid)})
            elif ext in (".ods", ".xlsx"):
                tasks.append({"num": num, "id": tid, "kind": "table",
                              "file": f.name, "data": data_for(tid)})

by_num = {}
for t in tasks:
    by_num.setdefault(t["num"], []).append(t)

payload = json.dumps(tasks, ensure_ascii=False).replace("</", "<\\/")

HTML = """<!DOCTYPE html>
<html lang="ru" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#15171a">
<title>ЕГЭ Информатика · банк решений</title>
<script>try{var t=localStorage.getItem('ege-theme');document.documentElement.dataset.theme=(t===null?'dark':t);}catch(e){document.documentElement.dataset.theme='dark';}</script>
<style>
:root{
  --bg:#fbfaf7; --fg:#1f2328; --muted:#5b6169; --faint:#8b9199;
  --card:#f4f2ee; --code-bg:#f3f1ec; --border:#e6e2da;
  --accent:#2f7d43; --accent-soft:rgba(47,125,67,.12);
  --syn-k:#034c7c; --syn-s:#a44185; --syn-c:#8a8a90; --syn-n:#174781; --syn-b:#7eb233;
  --maxw:1120px;
}
html[data-theme="dark"]{
  --bg:#15171a; --fg:#e9e7e3; --muted:#a9a7a2; --faint:#7d7b76;
  --card:#1c1f23; --code-bg:#1e2126; --border:#2b2f34;
  --accent:#6fb07f; --accent-soft:rgba(111,176,127,.14);
  --syn-k:#c586c0; --syn-s:#ce9178; --syn-c:#7a7a80; --syn-n:#b5cea8; --syn-b:#dcdcaa;
}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;
  background:var(--bg);color:var(--fg);font-size:17px;line-height:1.6;padding-bottom:64px}
a{color:var(--accent)}
header{max-width:var(--maxw);margin:0 auto;padding:40px 24px 8px}
h1{font-size:clamp(26px,3.4vw,34px);font-weight:650;letter-spacing:-.01em;line-height:1.15}
.sub{color:var(--muted);margin-top:10px;font-size:15px}
.sub a{text-decoration:none}
.sub a:hover{text-decoration:underline}
.row{display:flex;flex-wrap:wrap;gap:8px;margin-top:18px;align-items:center}
.pill{display:inline-flex;align-items:center;gap:6px;padding:7px 13px;border:1px solid var(--border);
  border-radius:999px;background:var(--card);color:var(--fg);text-decoration:none;font-size:14px;
  transition:border-color .15s ease,color .15s ease,background-color .15s ease}
.pill:hover{border-color:var(--accent);color:var(--accent)}
.pill.here{border-color:var(--accent);color:var(--accent);background:var(--accent-soft);font-weight:600}
.clone{position:relative}
.clone-btn{font:inherit;font-size:14px;padding:7px 13px;border:1px solid var(--accent);border-radius:999px;
  background:var(--accent-soft);color:var(--accent);cursor:pointer;transition:background-color .15s ease}
.clone-btn:hover{background:var(--accent);color:var(--bg)}
.clone-menu{position:absolute;top:calc(100% + 6px);right:0;z-index:20;min-width:230px;display:none;
  flex-direction:column;padding:6px;border:1px solid var(--border);border-radius:12px;background:var(--bg);
  box-shadow:0 12px 32px rgba(0,0,0,.16)}
.clone.open .clone-menu{display:flex}
.clone-menu a,.clone-menu button{display:block;width:100%;text-align:left;font:inherit;font-size:14px;
  padding:9px 12px;border:0;border-radius:8px;background:none;color:var(--fg);text-decoration:none;cursor:pointer}
.clone-menu a:hover,.clone-menu button:hover{background:var(--card);color:var(--accent)}
.bar{position:sticky;top:0;background:var(--bg);z-index:10;border-bottom:1px solid var(--border)}
.bar-in{max-width:var(--maxw);margin:0 auto;padding:12px 24px;display:flex;gap:10px;flex-wrap:wrap;align-items:center}
#q{flex:1;min-width:200px;padding:10px 14px;font-size:15px;border:1px solid var(--border);
  border-radius:10px;background:var(--card);color:var(--fg);
  transition:border-color .15s ease,box-shadow .15s ease}
#q:focus{outline:none;border-color:var(--accent);box-shadow:0 0 0 3px var(--accent-soft)}
#clear{display:none;font:inherit;font-size:14px;padding:8px 12px;border:1px solid var(--border);
  border-radius:10px;background:none;color:var(--muted);cursor:pointer}
#clear:hover{color:var(--fg);border-color:var(--faint)}
#count{color:var(--muted);font-size:14px;white-space:nowrap;font-variant-numeric:tabular-nums}
#theme{font:inherit;font-size:15px;background:none;border:1px solid var(--border);border-radius:10px;
  color:var(--muted);padding:8px 12px;cursor:pointer;transition:background-color .15s ease,color .15s ease}
#theme:hover{background:var(--card);color:var(--fg)}
#chips{max-width:var(--maxw);margin:0 auto;padding:20px 24px 6px;column-count:3;column-gap:28px}
.group{display:flex;flex-direction:column;gap:10px;min-width:0;break-inside:avoid;margin:0 0 20px}
.group-title{font-size:13px;color:var(--muted);font-weight:700;letter-spacing:.02em;
  padding-bottom:6px;border-bottom:1px solid var(--border)}
.group-list{display:flex;flex-wrap:wrap;gap:8px}
.chip{display:inline-flex;align-items:center;justify-content:center;min-width:48px;padding:7px 14px;
  border:1px solid var(--border);border-radius:999px;background:var(--card);color:var(--fg);
  font-family:inherit;font-size:15px;line-height:1.2;cursor:pointer;
  transition:border-color .15s ease,background-color .15s ease,color .15s ease}
.chip:hover{border-color:var(--accent)}
.chip.on{border-color:var(--accent);background:var(--accent-soft);color:var(--accent);font-weight:600}
.chip.stub{opacity:.5;border-style:dashed;cursor:default}
.chip.stub:hover{border-color:var(--border)}
.chip.stub.on{opacity:.85;background:var(--card);color:var(--muted);font-weight:400}
.chip{padding:8px 16px;border-radius:999px;border:1px solid var(--border);background:var(--card);
  color:var(--fg);font-size:15px;cursor:pointer;font-family:inherit;min-width:48px;
  transition:background-color .15s ease,color .15s ease,border-color .15s ease}
.chip:hover{border-color:var(--faint)}
.chip.on{background:var(--accent-soft);border-color:var(--accent);color:var(--accent);font-weight:600}
.chip.stub{opacity:.5;border-style:dashed;cursor:default}
.chip.stub:hover{border-color:var(--border)}
.chip.stub.on{opacity:.85;background:var(--card);color:var(--muted);border-color:var(--border);font-weight:400}
main{max-width:var(--maxw);margin:0 auto;padding:0 24px}
.numhead{display:flex;align-items:baseline;gap:12px;margin:36px 0 14px;border-bottom:1px solid var(--border);padding-bottom:10px}
.numhead h2{font-size:22px;font-weight:600;letter-spacing:-.01em}
.numhead span{color:var(--faint);font-size:13px}
.card{background:var(--card);border:1px solid var(--border);border-radius:10px;margin-bottom:14px;overflow:hidden;
  transition:border-color .15s ease,box-shadow .15s ease}
.card:hover{border-color:var(--faint)}
.card.open{border-color:var(--accent);box-shadow:0 4px 20px rgba(0,0,0,.05)}
.card-h{display:flex;align-items:center;gap:12px;padding:14px 16px;flex-wrap:wrap;cursor:pointer}
.tid{font-family:Consolas,Monaco,monospace;font-weight:700;font-size:16px}
.tid a{text-decoration:none}
.tid a:hover{text-decoration:underline}
.tools{margin-left:auto;display:flex;gap:8px;align-items:center;flex-wrap:wrap}
.tools a{color:var(--muted);text-decoration:none;font-size:13px;padding:4px 10px;border:1px solid var(--border);
  border-radius:999px;background:var(--bg);transition:color .15s ease,border-color .15s ease}
.tools a:hover{color:var(--accent);border-color:var(--accent)}
.copy{font:inherit;font-size:13px;padding:4px 11px;border:1px solid var(--border);border-radius:999px;
  background:var(--bg);color:var(--muted);cursor:pointer;transition:color .15s ease,border-color .15s ease}
.copy:hover{color:var(--accent);border-color:var(--accent)}
.chev{color:var(--faint);font-size:22px;line-height:1;transition:transform .18s cubic-bezier(.23,1,.32,1);transform:rotate(0)}
.card.open .chev{transform:rotate(90deg)}
.body{display:grid;grid-template-rows:0fr;transition:grid-template-rows .2s cubic-bezier(.23,1,.32,1)}
.card.open .body{grid-template-rows:1fr}
.body>pre,.body>.code-wrap{min-height:0;overflow:hidden}
pre{background:var(--code-bg);padding:0 16px;overflow-x:auto;tab-size:4;
  font-family:Consolas,Monaco,monospace;font-size:14px;line-height:1.65;
  border-top:1px solid transparent;transition:padding .18s ease,border-color .18s ease}
.card.open pre{padding:16px;border-top-color:var(--border)}
pre.imgbox{background:var(--bg);text-align:center}
pre.imgbox img{max-width:100%;height:auto;border-radius:8px}
.k{color:var(--syn-k);font-weight:600}
.s{color:var(--syn-s)}
.c{color:var(--syn-c);font-style:italic}
.n{color:var(--syn-n)}
.b{color:var(--syn-b)}
footer{max-width:var(--maxw);margin:48px auto 0;padding:0 24px;color:var(--faint);font-size:13px}
footer .row{margin-top:16px}
.empty{color:var(--muted);text-align:center;padding:56px 24px;display:none;font-size:16px}
.hint{max-width:var(--maxw);margin:0 auto;color:var(--muted);text-align:center;padding:56px 24px;font-size:16px}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
/* крупнее текст */
body{font-size:18px;line-height:1.65}
h1{font-size:clamp(26px,3.2vw,32px);font-weight:600}
.sub{font-size:16px}
.pill,.clone-btn,.clone-menu a,.clone-menu button{font-size:15px}
#q{font-size:16px;padding:11px 15px}
#clear,#count{font-size:15px}
#theme{font-size:16px}
.group-title{font-size:14px}
.chip{font-size:15px}
.numhead h2{font-size:20px}
.numhead span{font-size:14px}
.tid{font-size:17px}
.tools a,.copy{font-size:14px}
pre{font-size:15px}
footer{font-size:14px}
.empty,.hint{font-size:17px}
/* a11y / UX */
:root{color-scheme:light}
html[data-theme="dark"]{color-scheme:dark}
a,button,.chip{touch-action:manipulation}
*{-webkit-tap-highlight-color:rgba(0,0,0,0)}
h1,.numhead h2{text-wrap:balance}
.chip .n,#count,.numhead span{font-variant-numeric:tabular-nums}
.skip{position:absolute;left:-9999px;top:0;background:var(--bg);color:var(--fg);padding:10px 14px;border:1px solid var(--border);border-radius:8px;z-index:100}
.skip:focus{left:12px;top:12px}
main{scroll-margin-top:84px}
#top{position:fixed;right:20px;bottom:20px;z-index:50;width:44px;height:44px;border-radius:50%;
  border:1px solid var(--border);background:var(--card);color:var(--fg);font-size:20px;line-height:1;cursor:pointer;
  opacity:0;visibility:hidden;transition:opacity .2s ease,transform .2s ease,border-color .15s ease;
  box-shadow:0 6px 20px rgba(0,0,0,.18)}
#top.show{opacity:1;visibility:visible}
#top:hover{border-color:var(--accent);color:var(--accent)}
@media (max-width:820px){#chips{column-count:2}}
@media (max-width:560px){#chips{column-count:1}}
@media (prefers-reduced-motion: reduce){
  *{animation-duration:.01ms !important;transition-duration:.01ms !important}
}
</style>
</head>
<body>
<a class="skip" href="#main">К содержанию</a>
<header>
  <h1>ЕГЭ Информатика · банк решений</h1>
  <p class="sub"><span id="total"></span> · Python, таблицы, скриншоты · задачи с <a href="https://kompege.ru/task">kompege.ru</a></p>
</header>
<div class="bar"><div class="bar-in">
  <input id="q" type="search" name="q" autocomplete="off" spellcheck="false" placeholder="Поиск по номеру задачи (ID)…" aria-label="Поиск по ID">
  <button id="clear" type="button" title="Очистить" aria-label="Очистить поиск">×</button>
  <span id="count" aria-live="polite"></span>
  <span class="clone">
    <button class="clone-btn" type="button">Клонировать ▾</button>
    <span class="clone-menu">
      <a class="js-vscode" href="#">Открыть в VS Code</a>
      <a class="js-pycharm" href="#">Открыть в PyCharm</a>
      <button class="js-cmd" type="button">Скопировать git clone</button>
    </span>
  </span>
  <button id="theme" type="button" title="Тёмная тема" aria-label="Переключить тему">◐</button>
</div></div>
<nav id="chips"></nav>
<main id="main"></main>
<p class="empty" id="empty">Ничего не найдено. Сбросьте фильтр или измените запрос.</p>
<footer>
  Арсений Обозненко ·
  <a href="mailto:fapa2fa@gmail.com">fapa2fa@gmail.com</a> ·
  <a href="https://t.me/neonco" target="_blank" rel="noopener">tg</a> ·
  <a href="https://vk.ru/elpelp" target="_blank" rel="noopener">VK</a>
  <div class="row">
    <a class="pill" data-site="github" href="https://github.com/neonco/EGEINF">GitHub · репо</a>
    <a class="pill" data-site="gitverse" href="https://gitverse.ru/neonco/EGEINF">GitVerse · репо</a>
    <a class="pill" data-site="ghpages" href="https://neonco.github.io/EGEINF/">GitHub · сайт</a>
    <a class="pill" data-site="gvpages" href="https://neonco.gitverse.site/egeinf/">GitVerse · сайт</a>
  </div>
</footer>
<button id="top" type="button" aria-label="Наверх" title="Наверх">↑</button>
<script id="data" type="application/json">__PAYLOAD__</script>
<script>
const TASKS = JSON.parse(document.getElementById('data').textContent);
const $ = s => document.querySelector(s);
const $$ = s => document.querySelectorAll(s);
const esc = s => s.replace(/[&<>]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));

/* ---- host-aware links ---- */
const HOST = location.host;
const IS_GV = HOST.indexOf('gitverse.site') >= 0;
const REPO = IS_GV ? 'https://gitverse.ru/neonco/EGEINF.git' : 'https://github.com/neonco/EGEINF.git';
const SITE = HOST.indexOf('gitverse.site') >= 0 ? 'gvpages'
           : HOST.indexOf('github.io') >= 0 ? 'ghpages' : '';
if (SITE) $$('[data-site="' + SITE + '"]').forEach(e => e.classList.add('here'));
$$('.js-vscode').forEach(a => a.setAttribute('href', 'vscode://vscode.git/clone?url=' + encodeURIComponent(REPO)));
$$('.js-pycharm').forEach(a => a.setAttribute('href', 'jetbrains://pycharm/checkout/git?checkout.repo=' + encodeURIComponent(REPO) + '&idea.required.plugins.id=Git4Idea'));

function copyText(text, btn, done){
  const mark = () => { if (!btn) return; const t = btn.textContent; btn.textContent = done; setTimeout(() => { btn.textContent = t; }, 1500); };
  const fallback = () => {
    const ta = document.createElement('textarea');
    ta.value = text; ta.style.position = 'fixed'; ta.style.opacity = '0';
    document.body.appendChild(ta); ta.select();
    try { document.execCommand('copy'); mark(); } catch (e) {}
    document.body.removeChild(ta);
  };
  if (navigator.clipboard && window.isSecureContext) navigator.clipboard.writeText(text).then(mark).catch(fallback);
  else fallback();
}

/* ---- clone dropdown ---- */
document.addEventListener('click', e => {
  const t = e.target.closest('.clone-btn');
  $$('.clone.open').forEach(el => { if (!t || el !== t.closest('.clone')) el.classList.remove('open'); });
  if (t) t.closest('.clone').classList.toggle('open');
  const cmd = e.target.closest('.js-cmd');
  if (cmd) copyText('git clone ' + REPO, cmd, 'Скопировано ✓');
});
document.addEventListener('keydown', e => { if (e.key === 'Escape') $$('.clone.open').forEach(el => el.classList.remove('open')); });

const KW = /\\b(False|None|True|and|as|assert|async|await|break|class|continue|def|del|elif|else|except|finally|for|from|global|if|import|in|is|lambda|nonlocal|not|or|pass|raise|return|try|while|with|yield)\\b/g;
const BI = /\\b(print|len|range|int|str|float|list|dict|set|tuple|sorted|sum|min|max|abs|open|input|enumerate|zip|map|filter|any|all|round|type|isinstance|ord|chr|bin|hex|oct|pow|divmod|reversed)\\b/g;

function hl(code){
  let s = esc(code);
  const store = [];
  s = s.replace(/(#[^\\n]*|"(?:[^"\\\\\\n]|\\\\.)*"|'(?:[^'\\\\\\n]|\\\\.)*')/g, m => {
    store.push(m); return "\\u0000S" + (store.length-1) + "\\u0000";
  });
  s = s.replace(KW,'<span class="k">$1</span>')
       .replace(BI,'<span class="b">$1</span>')
       .replace(/\\b(\\d+(?:\\.\\d+)?)\\b/g,'<span class="n">$1</span>');
  s = s.replace(/\\u0000S(\\d+)\\u0000/g, (_,i)=>{
    const t = store[+i];
    return t.startsWith('#') ? '<span class="c">'+t+'</span>' : '<span class="s">'+t+'</span>';
  });
  return s;
}

const haveNums = [...new Set(TASKS.map(t=>t.num))].sort((a,b)=>a-b);
const nums = [];
for (let i = 1; i <= 27; i++) {
  if (i === 20 || i === 21) continue;  // 19–21 — один номер
  nums.push(i);
}
const chipsEl = $('#chips');
const params = new URLSearchParams(location.search);
let activeNum = params.get('n') !== null ? +params.get('n') : null;
let query = params.get('q') || '';
if (query) $('#q').value = query;

const DESC = {
  1:'Граф + табличка', 2:'Табличка истинности xyzw', 3:'Магазины-Артикулы',
  4:'Дерево по условию Фано', 5:'Перевод числа с IF - ELSE', 6:'Черепашка',
  7:'Объём картинка или музыка', 8:'Перебор слов', 9:'Строки с числами',
  10:'Word ctrl+F', 11:'Пароли на предприятии', 12:'Машина Тьюринга',
  13:'IP', 14:'Системы счисления', 15:'Логические приколы перебором',
  16:'Переписать + @cache (иногда setrecursionlimit)', 17:'Читать файл + 2 прогона',
  18:'Робот', 19:'Игра Петя-Ваня', 22:'Параллельные процессы',
  23:'Количество программ', 24:'Больная строка на миллионы символов',
  25:'Делители-маски', 26:'Сортировки и жадные алгоритмы', 27:'Трудоёмкая, но шаблон',
};
const GROUPS = [
  { title: 'прога база',         nums: [2, 5, 8, 13, 14, 15, 17] },
  { title: 'прога рекурсии',     nums: [16, 19, 23] },
  { title: 'прога набор власти', nums: [24, 25, 26, 27] },
  { title: 'судоку ручками',     nums: [1, 4, 6, 7, 10, 11, 12] },
  { title: 'excel',              nums: [3, 9, 18, 22] },
];
function chipHtml(n){
  const label = n===19 ? '19–21' : n;
  const stub = haveNums.includes(n) ? '' : ' stub';
  const t = DESC[n] ? esc(DESC[n]) + (stub ? ' · решений пока нет' : '') : (stub ? 'решений пока нет' : '');
  const title = t ? ` title="${t}"` : '';
  return `<button class="chip${stub}" data-n="${n}"${title}>${label}</button>`;
}
chipsEl.innerHTML = GROUPS.map(g =>
  `<div class="group"><div class="group-title">${g.title}</div><div class="group-list">${g.nums.map(chipHtml).join('')}</div></div>`
).join('');

function label(n){
  const base = n===19 ? 'Задания 19–21' : 'Задание '+n;
  return DESC[n] ? base + ' · ' + esc(DESC[n]) : base;
}

function render(){
  const main = $('#main'); main.innerHTML='';
  chipsEl.querySelectorAll('.chip').forEach(c=>
    c.classList.toggle('on', !query && +c.dataset.n===activeNum));
  $('#clear').style.display = query ? 'inline-block' : 'none';
  const filtering = !!query || activeNum !== null;
  if (!filtering){
    chipsEl.style.display = '';
    $('#count').textContent = '';
    $('#empty').style.display = 'none';
    const u0 = new URL(location.href);
    u0.searchParams.delete('q'); u0.searchParams.delete('n');
    history.replaceState(null, '', u0);
    return;
  }
  let shown = 0;
  nums.forEach(n=>{
    if (activeNum && !query && n!==activeNum) return;
    const list = TASKS.filter(t=>t.num===n &&
      (!query || t.id.includes(query)));
    if (!list.length) return;
    const h = document.createElement('div');
    h.className='numhead';
    h.innerHTML = `<h2>${label(n)}</h2><span>${list.length} реш.</span>`;
    main.appendChild(h);
    list.forEach(t=>{
      shown++;
      const card = document.createElement('div');
      card.className = query ? 'card open' : 'card';
      const part = t.part ? ` · часть ${t.part}` : '';
      const dir = n===27 ? `task27/${t.id}` : (n===19 ? 'task192021' : 'task'+n);
      const ghBase = `https://github.com/neonco/EGEINF/blob/master/kompege/zadachi_po_nomeru/${dir}`;
      const rawBase = `https://raw.githubusercontent.com/neonco/EGEINF/master/kompege/zadachi_po_nomeru/${dir}`;
      const dataLinks = t.data.map(d=>`<a href="${ghBase}/${d}">${d}</a>`).join('');
      let bodyHtml, tools = '';
      if (t.kind === 'img') {
        bodyHtml = `<div class="body"><pre class="imgbox"><img loading="lazy" decoding="async" src="${rawBase}/${t.file}" alt="Решение ${t.id}"></pre></div>`;
      } else if (t.kind === 'table') {
        bodyHtml = '';
        tools += `<a href="${ghBase}/${t.file}">таблица ${t.file}</a>`;
      } else {
        bodyHtml = `<div class="body"><pre translate="no">${hl(t.code)}</pre></div>`;
        tools += `<button class="copy" type="button">Копировать код</button>`;
      }
      card.innerHTML = `
        <div class="card-h">
          <span class="tid"><a href="https://kompege.ru/task?id=${t.id}" target="_blank" rel="noopener">№ ${t.id}</a>${part}</span>
          <span class="tools">${tools}${dataLinks}</span>
          <span class="chev" aria-hidden="true">›</span>
        </div>
        ${bodyHtml}`;
      const head = card.querySelector('.card-h');
      head.setAttribute('role','button');
      head.setAttribute('tabindex','0');
      head.setAttribute('aria-expanded', query ? 'true' : 'false');
      const toggleCard = () => {
        const open = card.classList.toggle('open');
        head.setAttribute('aria-expanded', open ? 'true' : 'false');
      };
      head.addEventListener('click', e=>{
        if (e.target.closest('a') || e.target.closest('button')) return;
        toggleCard();
      });
      head.addEventListener('keydown', e=>{
        if (e.key === 'Enter' || e.key === ' '){ e.preventDefault(); toggleCard(); }
      });
      const copyBtn = card.querySelector('.copy');
      if (copyBtn) copyBtn.addEventListener('click', e=>{ e.stopPropagation(); copyText(t.code, copyBtn, 'Скопировано ✓'); });
      main.appendChild(card);
    });
  });
  $('#count').textContent = shown + ' реш.';
  $('#clear').style.display = query ? 'inline-block' : 'none';
  $('#empty').style.display = shown ? 'none' : 'block';
  chipsEl.style.display = (query && shown) ? 'none' : '';
  const u = new URL(location.href);
  if (query) u.searchParams.set('q', query); else u.searchParams.delete('q');
  if (!query && activeNum !== null) u.searchParams.set('n', activeNum); else u.searchParams.delete('n');
  history.replaceState(null, '', u);
}

chipsEl.addEventListener('click', e=>{
  const b = e.target.closest('.chip'); if(!b) return;
  const n = +b.dataset.n;
  activeNum = activeNum===n ? null : n;
  chipsEl.querySelectorAll('.chip').forEach(c=>c.classList.toggle('on', +c.dataset.n===activeNum));
  render();
});
$('#q').addEventListener('input', e=>{ query = e.target.value.trim(); render(); });
$('#q').addEventListener('keydown', e=>{ if (e.key==='Escape'){ e.target.value=''; query=''; render(); } });
$('#clear').addEventListener('click', ()=>{ query=''; $('#q').value=''; activeNum=null; render(); $('#q').focus(); });

const root = document.documentElement;
const themeMeta = document.querySelector('meta[name=theme-color]');
function syncThemeColor(){ if (themeMeta) themeMeta.setAttribute('content', root.dataset.theme==='dark' ? '#15171a' : '#fbfaf7'); }
syncThemeColor();
$('#theme').addEventListener('click', ()=>{
  root.dataset.theme = root.dataset.theme==='dark' ? '' : 'dark';
  localStorage.setItem('ege-theme', root.dataset.theme);
  syncThemeColor();
});

$('#total').textContent = TASKS.length + ' решений';
const topBtn = $('#top');
const onScroll = () => topBtn.classList.toggle('show', window.scrollY > 400);
addEventListener('scroll', onScroll, {passive:true});
onScroll();
topBtn.addEventListener('click', () => window.scrollTo({top:0, behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth'}));
render();
</script>
</body>
</html>
"""

OUT.write_text(HTML.replace("__PAYLOAD__", payload), encoding="utf-8")
print(f"OK: {OUT} ({OUT.stat().st_size} байт), задач: {len(tasks)}, номеров: {len(by_num)}")
