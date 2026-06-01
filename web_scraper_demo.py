"""
web_scraper_demo.py — demo: scrape a listing page into clean CSV.

Real client jobs handle pagination, anti-bot headers, and messy markup.
This demo keeps it small and readable so you can see the approach.

Usage:
    python web_scraper_demo.py
Output:
    quotes.csv  (text, author, tags)
"""

import csv
import requests
from bs4 import BeautifulSoup

BASE = "https://quotes.toscrape.com"  # public sandbox site, safe to scrape


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

    next_link = soup.select_one("li.next a")
    next_url = BASE + next_link["href"] if next_link else None
    return rows, next_url


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
