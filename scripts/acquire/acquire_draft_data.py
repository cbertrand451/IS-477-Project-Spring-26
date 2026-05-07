"""Acquire raw Chicago Bulls draft data from Basketball Reference."""

from pathlib import Path
import hashlib
import os

import pandas as pd


URL = "https://www.basketball-reference.com/teams/CHI/draft.html"
PROJECT_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_PATH = PROJECT_ROOT / "data" / "raw" / "chicago_draft_data.csv"
CHECKSUM_PATH = PROJECT_ROOT / "data" / "raw" / "chicago_draft_data.sha256"


# flatten basketball reference's multiple level draft table headers
def flatten_columns(df):
    if not isinstance(df.columns, pd.MultiIndex):
        return df

    new_cols = []
    seen = {}

    for _, sub in df.columns:
        if sub in seen:
            seen[sub] += 1
            col_name = f"{sub}.{seen[sub] - 1}"
        else:
            seen[sub] = 1
            col_name = sub
        new_cols.append(col_name)

    df.columns = new_cols
    return df


def scrape_draft_data(url):
    df = pd.read_html(url, attrs={"id": "draft"})[0]
    df = flatten_columns(df)
    df = df[df["Year"] != "Year"].copy()
    df = df[df["Year"].astype(int) >= 2000]
    return df.reset_index(drop=True)


def save_draft_data(df, output_path):
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    print("Draft data saved to:", output_path)


def compute_sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def write_checksum(data_path, checksum_path):
    checksum = compute_sha256(data_path)
    with open(checksum_path, "w") as f:
        f.write(f"{checksum}  {os.path.basename(data_path)}\n")

    print("Checksum saved to:", checksum_path)
    # print("SHA-256:", checksum)


def main():
    draft_df = scrape_draft_data(URL)
    save_draft_data(draft_df, OUTPUT_PATH)
    write_checksum(OUTPUT_PATH, CHECKSUM_PATH)


if __name__ == "__main__":
    main()
