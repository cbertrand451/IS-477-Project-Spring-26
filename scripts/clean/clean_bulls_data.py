"""Clean Bulls season data using the clean_dataset2 notebook steps."""

from pathlib import Path

import numpy as np
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
INPUT_PATH = PROJECT_ROOT / "data" / "raw" / "bulls_data.csv"
OUTPUT_PATH = PROJECT_ROOT / "data" / "processed" / "bulls_season_data.csv"


def clean_bulls_data(df):
    df = df.copy()

    df["Season"] = df["Season"].apply(lambda x: int(x.split("-")[0]))
    df.drop(columns=["Unnamed: 8", "Unnamed: 15"], inplace=True)
    df["Finish"] = df["Finish"].apply(
        lambda x: int(x[0]) if isinstance(x, str) else np.nan
    )
    df.drop(columns=["Lg"], inplace=True)

    return df


def main():
    df = pd.read_csv(INPUT_PATH)
    cleaned_df = clean_bulls_data(df)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    cleaned_df.to_csv(OUTPUT_PATH, index=False)

    print(f"Loaded {len(df)} rows from {INPUT_PATH}")
    print(f"Saved cleaned Bulls season data to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
