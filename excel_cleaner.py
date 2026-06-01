"""
excel_cleaner.py — demo: clean a messy spreadsheet.

Typical client mess: duplicate rows, inconsistent casing, stray whitespace,
blank rows, dates stored as text. This shows the common fixes.

Usage:
    python excel_cleaner.py input.xlsx
Output:
    input_cleaned.xlsx
"""

import sys
import pandas as pd


def clean(df):
    # drop fully-blank rows
    df = df.dropna(how="all")

    # strip whitespace + normalize header names
    df.columns = [str(c).strip().lower().replace(" ", "_") for c in df.columns]

    # trim string cells, collapse inner whitespace
    for col in df.select_dtypes(include="object"):
        df[col] = (
            df[col].astype(str)
            .str.strip()
            .str.replace(r"\s+", " ", regex=True)
            .replace({"nan": ""})
        )

    # title-case a 'name' column if present
    if "name" in df.columns:
        df["name"] = df["name"].str.title()

    # drop exact duplicate rows
    before = len(df)
    df = df.drop_duplicates()
    print(f"removed {before - len(df)} duplicate rows")

    return df


def main():
    if len(sys.argv) < 2:
        print("usage: python excel_cleaner.py input.xlsx")
        sys.exit(1)

    path = sys.argv[1]
    df = pd.read_excel(path)
    cleaned = clean(df)
    out = path.rsplit(".", 1)[0] + "_cleaned.xlsx"
    cleaned.to_excel(out, index=False)
    print(f"wrote {out} ({len(cleaned)} rows)")


if __name__ == "__main__":
    main()
