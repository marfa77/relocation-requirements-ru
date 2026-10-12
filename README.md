# relocation-requirements-ru

**RU** · [EN](#english)

Открытый машиночитаемый датасет требований **13 ключевых программ ВНЖ и виз** в 8 странах: Португалия (D7, D8), Испания (digital nomad, non-lucrative), Италия (elective residence, digital nomad), Кипр (digital nomad, категория F), Германия (Голубая карта ЕС), Сербия (временный ВНЖ), Грузия (безвиз на год), Таиланд (DTV, LTR). Минимальный доход/средства, сборы, сроки, путь к ПМЖ/гражданству — **только из официальных источников** (`source_url`), проверено 2026-10-12. Не удалось подтвердить — `null`; ничего не угадано.

**Таблица с фильтром:** https://marfa77.github.io/relocation-requirements-ru/

| Страна | Программа | Мин. доход / средства | Гражданство, лет | Источник | Гайд |
|---|---|---|---|---|---|
| Portugal | Виза D7 (пенсионеры / пассивный доход) | 920 EUR/мес | — | [офиц. источник](https://vistos.mne.gov.pt/en/national-visas/necessary-documentation/means-of-subsistence) | [гайд Emigro](https://www.emigro.online/ru/portugal/programs/portugal-d7-passive-income) |
| Portugal | Виза цифрового кочевника (D8) | 3,680 EUR/мес | — | [офиц. источник](https://www.vfsglobal.com/one-pager/portugal/pakistan/english/pdf/checklist-national-residence-digital-nomads.pdf) | [гайд Emigro](https://www.emigro.online/ru/portugal/programs/portugal-d8-digital-nomad) |
| Spain | Виза цифрового кочевника (телеработник) | см. правило | 10 | [офиц. источник](https://www.one.gob.es/es/tramites/solicitud-del-visado-de-nomada-digital) | [гайд Emigro](https://www.emigro.online/ru/spain/programs/spain-digital-nomad) |
| Spain | ВНЖ без права работы (non-lucrativa) | см. правило | 10 | [офиц. источник](https://www.exteriores.gob.es/Consulados/londres/en/ServiciosConsulares/Paginas/Consular/Visado-de-residencia-no-lucrativa.aspx) | [гайд Emigro](https://www.emigro.online/ru/spain/programs/spain-non-lucrative) |
| Italy | Виза elective residence (residenza elettiva) | 31,000 EUR/год | — | [офиц. источник](https://consnewyork.esteri.it/en/servizi-consolari-e-visti/servizi-per-il-cittadino-straniero/visti/visas-to-enter-italy/elective-residency/) | [гайд Emigro](https://www.emigro.online/ru/italy/programs/italy-elective-residence) |
| Italy | Виза цифрового кочевника / удалённого работника | 24,789 EUR/год | — | [офиц. источник](https://consboston.esteri.it/en/servizi-consolari-e-visti/servizi-per-il-cittadino-straniero/visti/digital-nomad-remote-worker/) | [гайд Emigro](https://www.emigro.online/ru/italy/programs/italy-digital-nomad) |
| Cyprus | Виза цифрового кочевника Кипра | 3,500 EUR/мес | — | [офиц. источник](https://www.gov.cy/mip-md/en/documents/digital-nomads-and-family-members/) | [гайд Emigro](https://www.emigro.online/ru/cyprus/programs/cyprus-digital-nomad) |
| Cyprus | ПМЖ Кипра категории F | 9,568.17 EUR/год | — | [офиц. источник](https://www.gov.cy/mip-md/en/documents/companies-investors-permanent-residence-3/immigration-permits/) | [гайд Emigro](https://www.emigro.online/ru/cyprus/programs/cyprus-category-f) |
| Germany | Голубая карта ЕС | 50,700 EUR/год | 5 | [офиц. источник](https://www.make-it-in-germany.com/en/visa-residence/types/eu-blue-card) | [гайд Emigro](https://www.emigro.online/ru/germany/programs/germany-eu-blue-card) |
| Serbia | Временный вид на жительство (privremeni boravak) | см. правило | — | [офиц. источник](https://www.mup.gov.rs/wps/wcm/connect/2c0a7b8f-76f9-4e9a-a5e8-e742c69472cf/Temporary+residence+EN.pdf?CVID=o-r2uEO&MOD=AJPERES) | [гайд Emigro](https://www.emigro.online/ru/guides/vnj-serbiya-dlya-rossiyan-2026) |
| Georgia | Безвизовое пребывание до 1 года | см. правило | — | [офиц. источник](https://migration.commission.ge/files/visa_free_countries.pdf) | [гайд Emigro](https://www.emigro.online/ru/guides/gruziya-dlya-rossiyan-2026) |
| Thailand | Виза Destination Thailand (DTV) | 500,000 THB (остаток) | — | [офиц. источник](https://www.thaievisa.go.th/visa/dtv-visa) | [гайд Emigro](https://www.emigro.online/ru/thailand) |
| Thailand | Виза LTR — удалённый профессионал | 80,000 USD/год | — | [офиц. источник](https://ltr.boi.go.th/) | [гайд Emigro](https://www.emigro.online/ru/thailand) |

- `data/programs.json` — основные данные · `data/programs.csv` — генерируется из JSON
- `min_income_rule` — правило дословно по смыслу источника (например, «200% SMI»); `min_income_amount` заполнен только если сумма указана официально (или явно выведена из официальных чисел — см. `notes`)
- `verification`: `official_text_read` (текст официальной страницы прочитан напрямую), `official_search_extract` (сайт блокирует скрипты; текст взят из поискового индекса официальной страницы), `official_partner_text_read` (чек-лист посольства у официального визового партнёра)
- `scripts/validate.py` — схема, синхронизация CSV, проверка ссылок

## English

Open, machine-readable dataset of **13 key residence/visa programs** in 8 countries (Portugal D7/D8, Spain digital nomad + non-lucrative, Italy elective residence + digital nomad, Cyprus digital nomad + Category F, Germany EU Blue Card, Serbia temporary residence, Georgia one-year visa-free stay, Thailand DTV + LTR): official minimum income/funds, fees, duration, language requirement, path to PR/citizenship, each with an official `source_url`, checked 2026-10-12. Unverifiable values are `null` — nothing is guessed.

```python
import json, urllib.request
url = "https://raw.githubusercontent.com/marfa77/relocation-requirements-ru/main/data/programs.json"
P = json.load(urllib.request.urlopen(url))["entries"]
print([(p["id"], p["min_income_amount"], p["min_income_currency"]) for p in P if p["category"] == "digital_nomad"])
```

Validate: `pip install jsonschema && python scripts/validate.py`. Contribute by editing `scripts/build_data.py` (official URLs only), then `build_data.py → make_docs.py → validate.py`.

## Как цитировать / How to cite

> Emigro (2026). *relocation-requirements-ru: Residence & visa program requirements* (v1.0.0) [Data set]. https://github.com/marfa77/relocation-requirements-ru

## Лицензия / License

Данные / Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Код / Code (`scripts/`, `schema/`): MIT.

## Дисклеймер / Disclaimer

Не юридическая консультация, не связано с госорганами. Требования меняются — сверяйтесь с консульством. Not legal advice. Step-by-step guides: [Emigro](https://emigro.online).
