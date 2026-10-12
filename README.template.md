# relocation-requirements-ru

**RU** · [EN](#english)

Открытый машиночитаемый датасет требований **{{N}} ключевых программ ВНЖ и виз** в {{C}} странах: Португалия (D7, D8), Испания (digital nomad, non-lucrative), Италия (elective residence, digital nomad), Кипр (digital nomad, категория F), Германия (Голубая карта ЕС), Сербия (временный ВНЖ), Грузия (безвиз на год), Таиланд (DTV, LTR). Минимальный доход/средства, сборы, сроки, путь к ПМЖ/гражданству — **только из официальных источников** (`source_url`), проверено 2026-10-12. Не удалось подтвердить — `null`; ничего не угадано.

**Таблица с фильтром:** https://marfa77.github.io/relocation-requirements-ru/

| Страна | Программа | Мин. доход / средства | Гражданство, лет | Источник | Гайд |
|---|---|---|---|---|---|
{{TABLE}}

- `data/programs.json` — основные данные · `data/programs.csv` — генерируется из JSON
- `min_income_rule` — правило дословно по смыслу источника (например, «200% SMI»); `min_income_amount` заполнен только если сумма указана официально (или явно выведена из официальных чисел — см. `notes`)
- `verification`: `official_text_read` (текст официальной страницы прочитан напрямую), `official_search_extract` (сайт блокирует скрипты; текст взят из поискового индекса официальной страницы), `official_partner_text_read` (чек-лист посольства у официального визового партнёра)
- `scripts/validate.py` — схема, синхронизация CSV, проверка ссылок

## English

Open, machine-readable dataset of **{{N}} key residence/visa programs** in {{C}} countries (Portugal D7/D8, Spain digital nomad + non-lucrative, Italy elective residence + digital nomad, Cyprus digital nomad + Category F, Germany EU Blue Card, Serbia temporary residence, Georgia one-year visa-free stay, Thailand DTV + LTR): official minimum income/funds, fees, duration, language requirement, path to PR/citizenship, each with an official `source_url`, checked 2026-10-12. Unverifiable values are `null` — nothing is guessed.

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
