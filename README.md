# Freelance Sample Work

Small, real scripts that show how I work: clean code, clear output, a short
note on how to run each. These are demos — client jobs handle the messy
edge cases (pagination, anti-bot, weird file formats) the same way.

The manual job that eats your week — scraping, spreadsheets, file & report
grunt-work — rebuilt to run itself in minutes. What takes 2–4 days by hand,
an automation does 10–20× faster — then runs itself free, every time after.

**Services:** web scraping & monitoring · data/spreadsheet automation · custom scripts (files, PDFs, reports, APIs, scheduled jobs) · ComfyUI fixes
**Turnaround:** most jobs 1–3 days · from $30 · every job ships with a README so you can re-run it yourself.

---

## 1. `web_scraper_demo.py` — scrape a site into clean CSV
Pulls a paginated listing into `quotes.csv` (text, author, tags). Handles
pagination and sets a real User-Agent.

```bash
pip install requests beautifulsoup4
python web_scraper_demo.py
```

## 2. `excel_cleaner.py` — clean a messy spreadsheet
Drops blank rows, trims/normalizes text, fixes headers, removes duplicates,
title-cases names. Outputs `*_cleaned.xlsx`.

```bash
pip install pandas openpyxl
python excel_cleaner.py yourfile.xlsx
```

## 3. `batch_rename.ps1` — batch-rename files (PowerShell)
Renames a folder of files to a clean, sortable pattern. `-WhatIf` previews
before changing anything.

```powershell
.\batch_rename.ps1 -Folder ".\photos" -Prefix "product" -WhatIf
.\batch_rename.ps1 -Folder ".\photos" -Prefix "product"
```

---

## ComfyUI / Stable-Diffusion work
Output from a ComfyUI batch pipeline I built — **same character (consistent face,
identity, and style) held across 1000+ images**, generated cheaply in batch. Five
samples below; full set in [`screenshots/`](./screenshots).

![sample 1](./screenshots/comfyui-batch-01.png)
![sample 2](./screenshots/comfyui-batch-02.png)
![sample 3](./screenshots/comfyui-batch-03.png)
![sample 4](./screenshots/comfyui-batch-04.png)
![sample 5](./screenshots/comfyui-batch-05.png)

If your workflow is drifting on identity, crashing, or generating one image at a
time, this is the kind of pipeline I can fix or build for you.

---

## Hire me
Got something repetitive eating your time? Send the task — I'll tell you
straight if I can knock it out, and quote within the hour.
**Discord:** @yashbhati937 · **Email:** yashbhati937@gmail.com
