"""
Clean up a messy spreadsheet and write a *_cleaned.xlsx next to it.

Drops blank rows, trims and collapses whitespace, normalizes header names,
title-cases a "name" column if there is one, and removes duplicate rows.

    python excel_cleaner.py input.xlsx
"""

import sys
import pandas as pd


def clean(df):
    df = df.dropna(how="all")

    # headers -> lower_snake_case so they're predictable to work with
    df.columns = [str(c).strip().lower().replace(" ", "_") for c in df.columns]

    for col in df.select_dtypes(include="object"):
        df[col] = (
            df[col].astype(str)
            .str.strip()
            .str.replace(r"\s+", " ", regex=True)
            .replace({"nan": ""})
        )

    if "name" in df.columns:
        df["name"] = df["name"].str.title()

    before = len(df)
    df = df.drop_duplicates()
    print(f"removed {before - len(df)} duplicate rows")

    return df


def main():
    if len(sys.argv) < 2:
        print("usage: python excel_cleaner.py input.xlsx")
        sys.exit(1)

    path = sys.argv[1]
    df = clean(pd.read_excel(path))
    out = path.rsplit(".", 1)[0] + "_cleaned.xlsx"
    df.to_excel(out, index=False)
    print(f"wrote {out} ({len(df)} rows)")


if __name__ == "__main__":
    main()
