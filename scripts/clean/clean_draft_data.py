"""Clean Chicago Bulls draft data using the clean_dataset1 notebook steps."""

from pathlib import Path
import sys

import pandas as pd
from pandas.errors import EmptyDataError


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DRAFT_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "chicago_draft_data.csv"
ROOKIE_STATS_DIR = PROJECT_ROOT / "data" / "raw" / "rookie_stats_data"
OUTPUT_PATH = PROJECT_ROOT / "data" / "processed" / "draft_data_cleaned.csv"

DRAFT_STAT_COLUMNS = [
    "G",
    "MP",
    "PTS",
    "TRB",
    "AST",
    "FG%",
    "3P%",
    "FT%",
    "MP.1",
    "PTS.1",
    "TRB.1",
    "AST.1",
    "WS",
    "WS/48",
    "BPM",
    "VORP",
]

ROOKIE_COLUMNS = [
    "Age",
    "Pos",
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
    "Awards",
]


def configure_output_encoding():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")


def load_draft_data(path):
    df = pd.read_csv(path)
    df = df[df["Year"] != "Year"].copy()
    df = df.dropna(subset=["Player"]).reset_index(drop=True)

    df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
    df = df[df["Year"].notna()].copy()
    df["Year"] = df["Year"].astype(int)
    df = df[df["Year"] >= 2000].copy()

    traded_mask = df["Player"].astype(str).str.contains("\u21b3", regex=False, na=False)
    df = df[~traded_mask].reset_index(drop=True)

    return df


def player_name_from_csv(csv_file):
    return csv_file.stem.replace("_", " ")


def load_rookie_row(csv_file):
    try:
        player_df = pd.read_csv(csv_file)
    except EmptyDataError:
        return None

    if player_df.empty:
        return None

    available_cols = [col for col in ROOKIE_COLUMNS if col in player_df.columns]
    if not available_cols:
        return None

    non_empty_rows = player_df[available_cols].dropna(how="all")
    if non_empty_rows.empty:
        return None

    return player_df.loc[non_empty_rows.index[0]]


def build_rookie_lookup(rookie_stats_dir):
    rookie_lookup = {}
    skipped_files = []

    for csv_file in sorted(rookie_stats_dir.glob("*.csv")):
        rookie_row = load_rookie_row(csv_file)
        if rookie_row is None:
            skipped_files.append(csv_file.name)
            continue

        rookie_lookup[player_name_from_csv(csv_file)] = rookie_row

    return rookie_lookup, skipped_files


def merge_rookie_stats(draft_df, rookie_lookup):
    draft_df = draft_df.drop(
        columns=[col for col in DRAFT_STAT_COLUMNS if col in draft_df.columns]
    )

    for col in ROOKIE_COLUMNS:
        if col not in draft_df.columns:
            draft_df[col] = pd.NA

    missing_players = []

    for _, draft_row in draft_df.iterrows():
        player_name = draft_row["Player"]
        rookie_row = rookie_lookup.get(player_name)
        row_mask = draft_df["Player"].eq(player_name)

        if rookie_row is None:
            missing_players.append(player_name)
            continue

        available_cols = [col for col in ROOKIE_COLUMNS if col in rookie_row.index]
        draft_df.loc[row_mask, available_cols] = rookie_row[available_cols].values

    return draft_df.reset_index(drop=True), missing_players


def save_cleaned_data(df, output_path):
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)


def main():
    configure_output_encoding()

    draft_df = load_draft_data(DRAFT_DATA_PATH)
    rookie_lookup, skipped_files = build_rookie_lookup(ROOKIE_STATS_DIR)
    cleaned_df, missing_players = merge_rookie_stats(draft_df, rookie_lookup)
    save_cleaned_data(cleaned_df, OUTPUT_PATH)

    print(f"Loaded {len(draft_df)} draft rows from {DRAFT_DATA_PATH}")
    print(f"Loaded rookie stats for {len(rookie_lookup)} players")
    print(f"Skipped {len(skipped_files)} rookie files without usable rows")
    print(f"Kept {len(missing_players)} draft rows without rookie data")
    print(f"Saved cleaned draft data to {OUTPUT_PATH}")

    if skipped_files:
        print("Skipped rookie files:")
        for file_name in skipped_files:
            print(f"  {file_name}")

    if missing_players:
        print("Draft players kept without rookie data:")
        for player_name in missing_players:
            print(f"  {player_name}")


if __name__ == "__main__":
    main()
