"""Clean integrated Bulls data using the integrate notebook steps."""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
INPUT_PATH = PROJECT_ROOT / "data" / "processed" / "integrated_bulls_draft_data.csv"
OUTPUT_PATH = PROJECT_ROOT / "data" / "processed" / "final_bulls_data.csv"


STAT_COLUMNS_TO_FILL = [
    "G",
    "GS",
    "MP",
    "FG",
    "FGA",
    "FG%",
    "3P",
    "3PA",
    "3P%",
    "2P",
    "2PA",
    "2P%",
    "eFG%",
    "FT",
    "FTA",
    "FT%",
    "ORB",
    "DRB",
    "TRB",
    "AST",
    "STL",
    "BLK",
    "TOV",
    "PF",
    "PTS",
]


def extract_roy_rank(awards):
    if pd.isnull(awards):
        return 0

    awards_prefix = awards[:5]
    awards_suffix = awards_prefix[-1]

    if awards_prefix.startswith("ROY-") and awards_suffix.isdigit():
        return int(awards_suffix)

    return 0


def clean_integrated_data(df):
    df = df.copy()

    df.loc[df["Player"] == "Marko Simonovic", "Age"] = 21
    df.loc[df["Player"] == "Marko Simonovic", "Pos"] = "C"

    df.loc[df["Player"] == "JamesOn Curry", "Age"] = 22
    df.loc[df["Player"] == "JamesOn Curry", "Pos"] = "PG"

    df.loc[df["Player"] == "Mario Austin", "Age"] = 21
    df.loc[df["Player"] == "Mario Austin", "Pos"] = "SF"

    df.loc[df["Player"] == "Tommy Smith", "Age"] = 23
    df.loc[df["Player"] == "Tommy Smith", "Pos"] = "SF"

    df[STAT_COLUMNS_TO_FILL] = df[STAT_COLUMNS_TO_FILL].fillna(0)
    df["Playoffs"] = df["Playoffs"].fillna("Missed Playoffs")
    df["ROY"] = df["Awards"].apply(extract_roy_rank)
    df["Awards"] = df["Awards"].fillna("None")

    return df


def main():
    df = pd.read_csv(INPUT_PATH)
    cleaned_df = clean_integrated_data(df)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    cleaned_df.to_csv(OUTPUT_PATH, index=False)

    print(f"Loaded {len(df)} integrated rows from {INPUT_PATH}")
    print(f"Saved final cleaned data to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
