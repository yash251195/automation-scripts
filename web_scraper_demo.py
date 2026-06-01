"""
Scrape a paginated listing into a CSV.

Hits quotes.toscrape.com (a public sandbox), grabs text/author/tags from every
page, follows the "next" link until there isn't one, writes quotes.csv.

    python web_scraper_demo.py
"""

import csv
import requests
from bs4 import BeautifulSoup

BASE = "https://quotes.toscrape.com"


def scrape_page(url):
    resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (demo scraper)"}, timeout=15)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    rows = []
    for q in soup.select(".quote"):
        rows.append({
            "text": q.select_one(".text").get_text(strip=True),
            "author": q.select_one(".author").get_text(strip=True),
            "tags": ", ".join(t.get_text(strip=True) for t in q.select(".tag")),
        })

    nxt = soup.select_one("li.next a")
    return rows, (BASE + nxt["href"] if nxt else None)


def main():
    all_rows, url = [], BASE
    while url:
        rows, url = scrape_page(url)
        all_rows.extend(rows)
        print(f"scraped {len(rows)} rows, total {len(all_rows)}")

    with open("quotes.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["text", "author", "tags"])
        writer.writeheader()
        writer.writerows(all_rows)
    print(f"wrote quotes.csv ({len(all_rows)} rows)")


if __name__ == "__main__":
    main()
