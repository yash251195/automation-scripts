# Sample work

A few small scripts I reach for on freelance jobs, plus output from a ComfyUI
batch pipeline. These are the trimmed public versions. The paid jobs deal with
the messier stuff (logins, pagination, odd file formats, bigger volumes).

What I take on: web scraping and monitoring, spreadsheet/data cleanup and
automation, custom Python/PowerShell scripts (files, PDFs, reports, APIs,
scheduled jobs), and ComfyUI workflow fixes. Most jobs run 1-3 days, from $30.

## web_scraper_demo.py
Scrapes a paginated listing into `quotes.csv` (text, author, tags). Sets a real
User-Agent and follows the next-page links to the end.

```bash
pip install requests beautifulsoup4
python web_scraper_demo.py
```

## excel_cleaner.py
Takes a messy `.xlsx`, drops blank rows, trims text, normalizes headers, and
removes duplicates. Writes a `*_cleaned.xlsx` next to the original.

```bash
pip install pandas openpyxl
python excel_cleaner.py yourfile.xlsx
```

## batch_rename.ps1
Renames a folder of files to a padded, sortable pattern. Run with `-WhatIf`
first to preview before it changes anything.

```powershell
.\batch_rename.ps1 -Folder ".\photos" -Prefix "product" -WhatIf
.\batch_rename.ps1 -Folder ".\photos" -Prefix "product"
```

## ComfyUI batch output
Same character held consistent across 1000+ generations, done cheaply in batch.
A few samples below, rest in [`screenshots/`](./screenshots).

![sample 1](./screenshots/comfyui-batch-01.png)
![sample 2](./screenshots/comfyui-batch-02.png)
![sample 3](./screenshots/comfyui-batch-03.png)
![sample 4](./screenshots/comfyui-batch-04.png)
![sample 5](./screenshots/comfyui-batch-05.png)

If a workflow keeps drifting on identity, running out of memory, or only doing
one image at a time, that's the kind of thing I fix.

## Contact
Discord @yashbhati937 or yashbhati937@gmail.com. Tell me the task and I'll say
if I can do it, usually within the hour.
