---
license: cc-by-4.0
pretty_name: Relocation requirements (residence & visa programs)
language: [ru, en]
size_categories: [n<1K]
tags: [relocation, visa, digital-nomad, residence-permit, government, open-data]
configs:
  - config_name: default
    data_files:
      - split: train
        path: programs.csv
---

# Relocation requirements (RU/EN)

13 key residence/visa programs in 8 countries (Portugal, Spain, Italy, Cyprus, Germany, Serbia, Georgia, Thailand) with official minimum income/funds, fees, duration and path to PR/citizenship. Each row has an official `source_url`, `source_checked` = 2026-10-12 and a `verification` method. Unverified values are null.

**Source & updates:** https://github.com/marfa77/relocation-requirements-ru

**Limitations:** rules change and vary by consulate; not legal advice.

Maintained by [Emigro](https://emigro.online).
