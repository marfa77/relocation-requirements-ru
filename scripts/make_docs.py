"""Regenerate README.md, docs/index.html, docs/sitemap.xml, docs/robots.txt from data/programs.json."""
import json, pathlib, html
root = pathlib.Path(__file__).resolve().parent.parent
d = json.load(open(root/"data/programs.json")); E = d["entries"]
REPO = "https://github.com/marfa77/relocation-requirements-ru"; PAGES = "https://marfa77.github.io/relocation-requirements-ru/"
def inc(e):
    if e["min_income_amount"] is not None: return f'{e["min_income_amount"]:,} {e["min_income_currency"]}/{ {"month":"мес","year":"год"}[e["min_income_period"]] }'
    if e["min_funds_amount"] is not None: return f'{e["min_funds_amount"]:,} {e["min_funds_currency"]} (остаток)'
    return "см. правило"
v = lambda x: "—" if x is None else str(x)
rows = "\n".join(f'| {e["country"]} | {e["program_ru"]} | {inc(e)} | {v(e["citizenship_years"])} | [офиц. источник]({e["source_url"]}) | [гайд Emigro]({e["emigro_guide_url"]}) |' for e in E)
(root/"README.md").write_text((root/"README.template.md").read_text().replace("{{TABLE}}", rows).replace("{{N}}", str(len(E))).replace("{{C}}", str(len({e['iso2'] for e in E}))))
trs = "\n".join(f'<tr><td>{html.escape(e["country"])}</td><td>{html.escape(e["program_ru"])}<br><small>{html.escape(e["program_en"])}</small></td><td>{html.escape(inc(e))}</td><td>{html.escape(v(e["min_income_rule"]))}</td><td>{html.escape(v(e["application_fee"]))}</td><td>{html.escape(v(e["permit_duration"]))}</td><td>{html.escape(v(e["pr_path"]))}</td><td>{html.escape(v(e["citizenship_years"]))}</td><td><a href="{html.escape(e["source_url"])}" rel="noopener">Источник</a> · <a href="{e["emigro_guide_url"]}">Гайд</a></td></tr>' for e in E)
desc = f"Открытый датасет требований {len(E)} программ ВНЖ и виз (Португалия D7/D8, Испания, Италия, Кипр, Германия, Сербия, Грузия, Таиланд): минимальный доход, сборы, сроки, путь к ПМЖ/гражданству — только из официальных источников."
ld = {"@context":"https://schema.org","@type":"Dataset","name":"Relocation requirements (relocation-requirements-ru)","description":desc,"inLanguage":["ru","en"],
 "url":PAGES,"license":"https://creativecommons.org/licenses/by/4.0/","isAccessibleForFree":True,"version":d["version"],"dateModified":d["source_checked"],
 "keywords":["relocation","visa","digital nomad visa","residence permit","ВНЖ","релокация"],"creator":{"@type":"Organization","name":"Emigro","url":"https://emigro.online"},
 "spatialCoverage":sorted({e["country"] for e in E}),
 "distribution":[{"@type":"DataDownload","encodingFormat":"application/json","contentUrl":"https://raw.githubusercontent.com/marfa77/relocation-requirements-ru/main/data/programs.json"},
                 {"@type":"DataDownload","encodingFormat":"text/csv","contentUrl":"https://raw.githubusercontent.com/marfa77/relocation-requirements-ru/main/data/programs.csv"}]}
page = f'''<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Требования ВНЖ и виз для релокации — открытый датасет</title><meta name="description" content="{html.escape(desc)}"><link rel="canonical" href="{PAGES}">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<style>body{{font:15px/1.5 system-ui,sans-serif;margin:0 auto;max-width:1200px;padding:24px;color:#1a1a1a}}input{{width:100%;padding:10px;font-size:1rem;border:1px solid #bbb;border-radius:6px;margin:12px 0}}
table{{border-collapse:collapse;width:100%}}th,td{{text-align:left;padding:7px 8px;border-bottom:1px solid #e3e3e3;vertical-align:top}}th{{background:#f5f5f5;position:sticky;top:0}}a{{color:#0b5cad}}small{{color:#666}}</style></head>
<body><h1>Требования ВНЖ и виз для релокации</h1>
<p>{html.escape(desc)} Пустое значение (—) = не удалось подтвердить на официальной странице; ничего не додумано. Проверено {d["source_checked"]}.
Скачать <a href="{REPO}/blob/main/data/programs.json">JSON</a> · <a href="{REPO}/blob/main/data/programs.csv">CSV</a> · <a href="{REPO}">GitHub</a>. Лицензия данных CC BY 4.0.</p>
<p lang="en"><small>English: open dataset of key residence/visa programs with official minimum income/funds, fees, duration and path to PR/citizenship; every value links to an official source.</small></p>
<input id="q" type="search" placeholder="Фильтр: страна или программа (Portugal, nomad, D7…)" aria-label="Фильтр">
<table id="t"><thead><tr><th>Страна</th><th>Программа</th><th>Мин. доход / средства</th><th>Правило (как в источнике)</th><th>Сбор</th><th>Срок</th><th>ПМЖ</th><th>Гражданство, лет</th><th>Ссылки</th></tr></thead><tbody>
{trs}
</tbody></table>
<p><small>Не юридическая консультация. Требования меняются — сверяйтесь с консульством. Пошаговые гайды и чек-листы по каждой стране — на <a href="https://emigro.online">Emigro</a>.</small></p>
<script>document.getElementById('q').addEventListener('input',e=>{{const q=e.target.value.toLowerCase();for(const r of document.querySelectorAll('#t tbody tr'))r.style.display=r.textContent.toLowerCase().includes(q)?'':'none'}});</script>
</body></html>'''
(root/"docs/index.html").write_text(page)
(root/"docs/sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{PAGES}</loc><lastmod>{d["source_checked"]}</lastmod></url></urlset>\n')
(root/"docs/robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {PAGES}sitemap.xml\n")
print("docs ok")
