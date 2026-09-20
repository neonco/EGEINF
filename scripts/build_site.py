# -*- coding: utf-8 -*-
"""Генератор одностраничника «Банк решений ЕГЭ» из репозитория EGEINF.
Сканирует kompege/zadachi_po_nomeru/ и собирает самодостаточный site/index.html.
Запуск: python site/build_site.py  (из корня репозитория)
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
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ЕГЭ Информатика · банк решений</title>
<style>
:root{
  --bg:#ffffff; --fg:#1c1c1e; --muted:#6b6b70; --faint:#9a9aa0;
  --card:#f7f7f9; --code-bg:#f4f4f6; --border:#e4e4e8;
  --accent:#2e7d32; --accent-soft:rgba(46,125,50,.12);
  --syn-k:#034c7c; --syn-s:#a44185; --syn-c:#8a8a90; --syn-n:#174781; --syn-b:#7eb233;
}
html[data-theme="dark"]{
  --bg:#17181a; --fg:#e8e8ea; --muted:#a6a6ac; --faint:#7a7a80;
  --card:#1f2023; --code-bg:#222326; --border:#333439;
  --accent:#66bb6a; --accent-soft:rgba(102,187,106,.14);
  --syn-k:#c586c0; --syn-s:#ce9178; --syn-c:#7a7a80; --syn-n:#b5cea8; --syn-b:#dcdcaa;
}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;
  background:var(--bg);color:var(--fg);font-size:16px;padding-bottom:60px}
header{max-width:1080px;margin:0 auto;padding:32px 24px 8px}
h1{font-size:28px;font-weight:500;letter-spacing:0}
.sub{color:var(--muted);margin-top:8px;font-size:14px}
.sub a{color:var(--accent);text-decoration:none}
.bar{position:sticky;top:0;background:var(--bg);z-index:5;border-bottom:1px solid var(--border)}
.bar-in{max-width:1080px;margin:0 auto;padding:12px 24px;display:flex;gap:12px;flex-wrap:wrap;align-items:center}
#q{flex:1;min-width:180px;padding:8px 12px;font-size:14px;border:1px solid var(--border);
  border-radius:8px;background:var(--card);color:var(--fg);
  transition:border-color .15s ease, box-shadow .15s ease}
#q:focus{outline:none;border-color:var(--accent);box-shadow:0 0 0 3px var(--accent-soft)}
#theme{background:none;border:1px solid var(--border);border-radius:8px;color:var(--muted);
  padding:7px 11px;cursor:pointer;font-size:14px;
  transition:background-color .15s ease, color .15s ease}
#theme:hover{background:var(--card);color:var(--fg)}
.chips{max-width:1080px;margin:0 auto;padding:12px 24px;display:flex;flex-wrap:wrap;gap:8px}
.chip{padding:8px 18px;border-radius:999px;border:1px solid var(--border);background:var(--card);
  color:var(--fg);font-size:16px;cursor:pointer;font-family:inherit;min-width:52px;
  transition:background-color .15s ease, color .15s ease, border-color .15s ease}
.chip:hover{border-color:var(--faint)}
.chip.on{background:var(--accent-soft);border-color:var(--accent);color:var(--accent);font-weight:600}
.chip.stub{opacity:.45;border-style:dashed;cursor:default}
.chip.stub:hover{border-color:var(--border)}
.chip.stub.on{opacity:.8;background:var(--card);color:var(--muted);border-color:var(--border);font-weight:400}
main{max-width:1080px;margin:0 auto;padding:0 24px}
.numhead{display:flex;align-items:baseline;gap:12px;margin:32px 0 12px;border-bottom:1px solid var(--border);padding-bottom:8px}
.numhead h2{font-size:20px;font-weight:500;letter-spacing:0}
.numhead span{color:var(--faint);font-size:12px}
.card{background:var(--card);border:1px solid var(--border);border-radius:12px;margin-bottom:16px;overflow:hidden}
.card-h{display:flex;align-items:center;gap:12px;padding:12px 16px;flex-wrap:wrap;cursor:pointer}
.tid{font-family:Consolas,Monaco,monospace;font-weight:700;font-size:15px}
.tid a{color:var(--accent);text-decoration:none}
.links{margin-left:auto;display:flex;gap:12px;font-size:14px}
.links a{color:var(--muted);text-decoration:none}
.links a:hover{color:var(--accent)}
.body{display:grid;grid-template-rows:0fr;transition:grid-template-rows .18s cubic-bezier(.23,1,.32,1)}
.card.open .body{grid-template-rows:1fr}
.body>pre{min-height:0;overflow:hidden}
pre{background:var(--code-bg);padding:0 16px;overflow-x:auto;
  font-family:Consolas,Monaco,monospace;font-size:14px;line-height:1.55;
  border-top:1px solid transparent;transition:padding .18s ease, border-color .18s ease}
.card.open pre{padding:14px 16px;border-top-color:var(--border)}
pre.imgbox{background:var(--bg);text-align:center}
pre.imgbox img{max-width:100%;height:auto;border-radius:6px}
.toggle{color:var(--muted);font-size:14px;cursor:pointer;user-select:none}
.k{color:var(--syn-k);font-weight:600}
.s{color:var(--syn-s)}
.c{color:var(--syn-c);font-style:italic}
.n{color:var(--syn-n)}
.b{color:var(--syn-b)}
footer{max-width:1080px;margin:40px auto 0;padding:0 24px;color:var(--faint);font-size:12px}
.empty{color:var(--faint);text-align:center;padding:40px 0;display:none}
@media (prefers-reduced-motion: reduce){
  *{animation-duration:.01ms !important;transition-duration:.01ms !important}
}
</style>
</head>
<body>
<header>
  <h1>ЕГЭ Информатика · банк решений</h1>
  <p class="sub"><span id="total"></span> · python, таблицы, скриншоты · задачи с <a href="https://kompege.ru/task">kompege.ru</a> ·
    <a href="https://github.com/neonco/EGEINF">github.com/neonco/EGEINF</a></p>
</header>
<div class="bar"><div class="bar-in">
  <input id="q" type="search" placeholder="Поиск по номеру задачи (ID)…" aria-label="Поиск по ID">
  <button id="theme" title="Тёмная тема">◐</button>
</div></div>
<nav class="chips" id="chips"></nav>
<main id="main"></main>
<p class="empty" id="empty">Ничего не найдено</p>
<footer>Сгенерировано автоматически из репозитория EGEINF · build_site.py</footer>
<script id="data" type="application/json">__PAYLOAD__</script>
<script>
const TASKS = JSON.parse(document.getElementById('data').textContent);
const $ = s => document.querySelector(s);
const esc = s => s.replace(/[&<>]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));

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
let activeNum = null, query = '';

chipsEl.innerHTML = nums.map(n=>{
  const label = n===19 ? '19–21' : n;
  const stub = haveNums.includes(n) ? '' : ' stub';
  const title = stub ? ' title="пока нет решений"' : '';
  return `<button class="chip${stub}" data-n="${n}"${title}>${label}</button>`;
}).join('');

function label(n){ return n===19 ? 'Задания 19–21' : 'Задание '+n; }

function render(){
  const main = $('#main'); main.innerHTML='';
  // подсветка чипа — только когда поиск пуст (поиск глобальный, чип не участвует)
  chipsEl.querySelectorAll('.chip').forEach(c=>
    c.classList.toggle('on', !query && +c.dataset.n===activeNum));
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
      card.className='card';
      const part = t.part ? ` · часть ${t.part}` : '';
      const dir = n===27 ? `task27/${t.id}` : (n===19 ? 'task192021' : 'task'+n);
      const ghBase = `https://github.com/neonco/EGEINF/blob/master/kompege/zadachi_po_nomeru/${dir}`;
      const rawBase = `https://raw.githubusercontent.com/neonco/EGEINF/master/kompege/zadachi_po_nomeru/${dir}`;
      const dataLinks = t.data.map(d=>`<a href="${ghBase}/${d}">${d}</a>`).join('');
      let bodyHtml, toggleLabel;
      if (t.kind === 'img') {
        bodyHtml = `<div class="body"><pre class="imgbox"><img loading="lazy" src="${rawBase}/${t.file}" alt="Решение ${t.id}"></pre></div>`;
        toggleLabel = 'картинка ▾';
      } else if (t.kind === 'table') {
        bodyHtml = '';
        toggleLabel = '';
      } else {
        bodyHtml = `<div class="body"><pre>${hl(t.code)}</pre></div>`;
        toggleLabel = 'код ▾';
      }
      const tableLink = t.kind === 'table'
        ? `<a href="${ghBase}/${t.file}">таблица ${t.file}</a>` : '';
      card.innerHTML = `
        <div class="card-h">
          <span class="tid"><a href="https://kompege.ru/task?id=${t.id}" target="_blank" rel="noopener">№ ${t.id}</a>${part}</span>
          <span class="toggle">${toggleLabel}</span>
          <span class="links">${tableLink}${dataLinks}</span>
        </div>
        ${bodyHtml}`;
      card.querySelector('.card-h').addEventListener('click', e=>{
        if (e.target.tagName==='A') return;
        card.classList.toggle('open');
      });
      main.appendChild(card);
    });
  });
  $('#empty').style.display = shown ? 'none' : 'block';
}

chipsEl.addEventListener('click', e=>{
  const b = e.target.closest('.chip'); if(!b) return;
  const n = +b.dataset.n;
  activeNum = activeNum===n ? null : n;
  chipsEl.querySelectorAll('.chip').forEach(c=>c.classList.toggle('on', +c.dataset.n===activeNum));
  render();
});
$('#q').addEventListener('input', e=>{ query = e.target.value.trim(); render(); });

const root = document.documentElement;
const saved = localStorage.getItem('ege-theme');
if (saved) root.dataset.theme = saved;  // по умолчанию — светлая
$('#theme').addEventListener('click', ()=>{
  root.dataset.theme = root.dataset.theme==='dark' ? '' : 'dark';
  localStorage.setItem('ege-theme', root.dataset.theme);
});

$('#total').textContent = TASKS.length + ' решений';
render();
</script>
</body>
</html>
"""

OUT.write_text(HTML.replace("__PAYLOAD__", payload), encoding="utf-8")
print(f"OK: {OUT} ({OUT.stat().st_size} байт), задач: {len(tasks)}, номеров: {len(by_num)}")
"""
note: заменяем __PAYLOAD__ аккуратно — в payload могут быть последовательности типа </script>
"""
