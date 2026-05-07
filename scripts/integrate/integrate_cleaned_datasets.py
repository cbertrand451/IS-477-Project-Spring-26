"""Integrate cleaned Bulls season and draft datasets."""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
BULLS_SEASON_PATH = PROJECT_ROOT / "data" / "processed" / "bulls_season_data.csv"
DRAFT_DATA_PATH = PROJECT_ROOT / "data" / "processed" / "draft_data_cleaned.csv"
OUTPUT_PATH = PROJECT_ROOT / "data" / "processed" / "integrated_bulls_draft_data.csv"


def integrate_datasets(bulls_df, draft_df):
    return pd.merge(bulls_df, draft_df, left_on="Season", right_on="Year", how="inner")


def main():
    bulls_df = pd.read_csv(BULLS_SEASON_PATH)
    draft_df = pd.read_csv(DRAFT_DATA_PATH)
    merged_df = integrate_datasets(bulls_df, draft_df)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    merged_df.to_csv(OUTPUT_PATH, index=False)

    print(f"Loaded {len(bulls_df)} Bulls season rows from {BULLS_SEASON_PATH}")
    print(f"Loaded {len(draft_df)} draft rows from {DRAFT_DATA_PATH}")
    print(f"Saved integrated data to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
