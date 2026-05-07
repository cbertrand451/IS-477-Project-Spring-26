"""Acquire rookie-year stats for Chicago Bulls draft picks."""

from pathlib import Path
import argparse
import time

import pandas as pd
from pandas.errors import EmptyDataError


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DRAFT_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "chicago_draft_data.csv"
OUTPUT_DIR = PROJECT_ROOT / "data" / "raw" / "rookie_stats_data"
DEFAULT_DELAY_SECONDS = 6
DID_NOT_PLAY_PREFIX = "Did not play"
ROOKIE_STATS_COLUMNS = [
    "Season",
    "Age",
    "Team",
    "Lg",
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


class DidNotPlayError(ValueError):
    """Raised when Basketball Reference has no played rookie season for a player."""


def load_draft_players(path):
    df = pd.read_csv(path)
    df = df[df["Year"] != "Year"].copy()
    df = df[df["Year"].astype(int) >= 2000]
    df = df.dropna(subset=["Player"]).reset_index(drop=True)

    traded_mask = df["Player"].astype(str).str.contains(r"\(", regex=True, na=False)
    df = df[~traded_mask].reset_index(drop=True)

    return (
        df["Player"]
        .dropna()
        .astype(str)
        .str.strip()
        .drop_duplicates()
        .tolist()
    )


def player_filename(player_name):
    return f"{player_name.replace(' ', '_')}.csv"


def create_player_files(player_names, output_dir):
    output_dir.mkdir(parents=True, exist_ok=True)

    created_files = []
    existing_files = []

    for player_name in player_names:
        file_path = output_dir / player_filename(player_name)

        if file_path.exists():
            existing_files.append(file_path.name)
            continue

        file_path.touch()
        created_files.append(file_path.name)

    print(f"Created {len(created_files)} CSV files in {output_dir}")
    print(f"Skipped {len(existing_files)} existing files")


def build_player_url(player_name):
    parts = player_name.split()
    if len(parts) < 2:
        raise ValueError("Player name must include at least first and last name.")

    first_name = parts[0]
    last_name = parts[-1]
    clean_last = "".join(c.lower() for c in last_name if c.isalnum())
    clean_first = "".join(c.lower() for c in first_name if c.isalnum())

    if not clean_last or not clean_first:
        raise ValueError("Player name could not be converted to a URL code.")

    first_letter = clean_last[0]
    player_code = f"{clean_last[:5]}{clean_first[:2]}01"
    return f"https://www.basketball-reference.com/players/{first_letter}/{player_code}.html"


def find_per_game_table(tables):
    for table in tables:
        if {"Season", "G", "GS", "MP", "FG", "FGA", "eFG%", "PTS"}.issubset(
            table.columns
        ):
            return table
    raise ValueError("Per game table not found.")


def is_did_not_play_row(row):
    values = row.drop(labels=["Season"], errors="ignore").dropna().astype(str)
    return (
        not values.empty
        and values.str.startswith(DID_NOT_PLAY_PREFIX, na=False).all()
    )


def nullify_did_not_play_rows(df):
    df = df.copy()
    did_not_play_mask = df.apply(is_did_not_play_row, axis=1)
    columns_to_null = [column for column in df.columns if column != "Season"]
    df.loc[did_not_play_mask, columns_to_null] = pd.NA
    return df


def existing_file_has_only_did_not_play_data(file_path):
    try:
        df = pd.read_csv(file_path)
    except EmptyDataError:
        return False

    if df.empty:
        return False

    return df.apply(is_did_not_play_row, axis=1).all()


def fetch_rookie_data(player_name):
    url = build_player_url(player_name)
    print(f"Fetching data for {player_name} from {url}")

    try:
        tables = pd.read_html(url, attrs={"id": "per_game_stats"})
    except ValueError:
        tables = pd.read_html(url)

    per_game_df = find_per_game_table(tables)
    per_game_df = per_game_df[per_game_df["Season"] != "Season"]
    per_game_df = nullify_did_not_play_rows(per_game_df)

    if per_game_df.empty:
        raise DidNotPlayError("No NBA rookie season found; player did not play.")

    return per_game_df.iloc[0:1]


def scrape_player_files(player_names, output_dir, delay_seconds, overwrite):
    saved_files = []
    failed_players = []
    skipped_files = []
    skipped_did_not_play = []

    for player_name in player_names:
        file_path = output_dir / player_filename(player_name)

        if file_path.exists() and file_path.stat().st_size > 0 and not overwrite:
            if existing_file_has_only_did_not_play_data(file_path):
                file_path.unlink()
                print(f"Removed did-not-play data for {player_name}: {file_path}")
            else:
                skipped_files.append(file_path.name)
                print(f"Skipping existing data for {player_name}: {file_path}")
                continue

        try:
            rookie_data = fetch_rookie_data(player_name)
            rookie_data.to_csv(file_path, index=False)
            saved_files.append(file_path.name)
            print(f"Saved data for {player_name} to {file_path}")
        except DidNotPlayError as exc:
            if file_path.exists():
                file_path.unlink()
            skipped_did_not_play.append(player_name)
            print(f"Skipped {player_name}: {exc}")
        except Exception as exc:
            failed_players.append((player_name, str(exc)))
            print(f"Failed to fetch data for {player_name}: {exc}")

        time.sleep(delay_seconds)

    print(f"Saved {len(saved_files)} player files.")
    print(f"Skipped {len(skipped_files)} existing player files.")
    print(f"Skipped {len(skipped_did_not_play)} players with no NBA rookie season.")
    print(f"Failed to fetch {len(failed_players)} players.")

    if skipped_did_not_play:
        print("Players skipped because they did not play:")
        for player_name in skipped_did_not_play:
            print(f"  {player_name}")

    if failed_players:
        print("Failed players:")
        for player_name, error in failed_players:
            print(f"  {player_name}: {error}")


def unify_player_file_columns(output_dir):
    csv_files = sorted(output_dir.glob("*.csv"))
    file_data = {}

    for csv_file in csv_files:
        try:
            df = pd.read_csv(csv_file)
            file_data[csv_file] = df
        except EmptyDataError:
            file_data[csv_file] = None

    if not csv_files:
        print("No column information was found in the CSV files.")
        return

    updated_files = []
    empty_files = []

    for csv_file, df in file_data.items():
        if df is None:
            fixed_df = pd.DataFrame([{column: pd.NA for column in ROOKIE_STATS_COLUMNS}])
            empty_files.append(csv_file.name)
            missing_columns = ROOKIE_STATS_COLUMNS.copy()
            extra_columns = []
        else:
            missing_columns = [
                column for column in ROOKIE_STATS_COLUMNS if column not in df.columns
            ]
            extra_columns = [
                column for column in df.columns if column not in ROOKIE_STATS_COLUMNS
            ]
            fixed_df = df.copy()

            for column in missing_columns:
                fixed_df[column] = pd.NA

            fixed_df = nullify_did_not_play_rows(fixed_df)
            fixed_df = fixed_df[ROOKIE_STATS_COLUMNS]

        fixed_df.to_csv(csv_file, index=False)

        if missing_columns or extra_columns:
            updated_files.append((csv_file.name, missing_columns, extra_columns))

    print(f"Checked {len(csv_files)} files.")
    print(f"Unified column set has {len(ROOKIE_STATS_COLUMNS)} columns.")

    if empty_files:
        print("Empty files filled with NA values:")
        for file_name in empty_files:
            print(f"  {file_name}")

    if updated_files:
        print("Files updated with missing or extra columns:")
        for file_name, missing_columns, extra_columns in updated_files:
            print(
                f"  {file_name}: added {missing_columns}; removed {extra_columns}"
            )
    else:
        print("All files already had the same columns.")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Acquire rookie-year stats for Bulls draft picks."
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=DEFAULT_DELAY_SECONDS,
        help="Seconds to wait between Basketball Reference requests.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing non-empty player CSV files.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    player_names = load_draft_players(DRAFT_DATA_PATH)

    print(f"Found {len(player_names)} Bulls draft players from 2000 or later.")
    create_player_files(player_names, OUTPUT_DIR)
    scrape_player_files(player_names, OUTPUT_DIR, args.delay, args.overwrite)
    unify_player_file_columns(OUTPUT_DIR)


if __name__ == "__main__":
    main()
