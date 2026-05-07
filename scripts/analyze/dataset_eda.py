from pathlib import Path
import warnings

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = PROJECT_ROOT / "data" / "processed" / "final_bulls_data.csv"
VISUALS_DIR = PROJECT_ROOT / "visuals"


warnings.filterwarnings("ignore", category=FutureWarning, module="seaborn")
plt.rcParams["figure.figsize"] = (12, 6)
sns.set_style("whitegrid")


def save_current_figure(filename):
    """Save the current matplotlib figure and close it."""
    output_path = VISUALS_DIR / filename
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"Saved visual: {output_path}")


def print_dataset_summary(df):
    print("Loaded dataset with rows:", len(df), "and columns:", len(df.columns))
    print("\nColumn names:")
    print(df.columns.tolist())

    print("\nData types:")
    print(df.dtypes)

    print("\nMissing values by column:")
    print(df.isna().sum().sort_values(ascending=False).head(20))

    print("\nNumeric summary for key columns:")
    print(df[["W/L%", "Pk", "G", "PTS", "TRB", "AST", "FG%"]].describe())

    missing = df.isna().sum()
    print("\nColumns with missing values:")
    print(missing[missing > 0])

    print("\nSeason range:", df["Season"].min(), "to", df["Season"].max())
    print("Unique draft picks:", df["Pk"].nunique())
    print("Player count:", df["Player"].nunique())

    print("\nPlayoff value counts:")
    print(df["Playoffs"].value_counts(dropna=False))


def plot_pick_vs_win_percentage(df):
    plt.figure()
    sns.scatterplot(
        data=df,
        x="Pk",
        y="W/L%",
        hue="Playoffs",
        palette="viridis",
        edgecolor="black",
        s=100,
    )
    plt.gca().invert_xaxis()
    plt.title("Draft Pick Number vs Bulls Win Percentage")
    plt.xlabel("Draft Pick (1 = highest)")
    plt.ylabel("Win Percentage")
    plt.legend(title="Playoffs", bbox_to_anchor=(1.05, 1), loc="upper left")
    save_current_figure("draft_pick_vs_win_percentage.png")

    corr_pick = df["Pk"].corr(df["W/L%"])
    print("\nCorrelation between draft pick and win percentage:", round(corr_pick, 3))

    pick_bins = [0, 10, 20, 40, 60]
    labels = ["Top 10", "11-20", "21-40", "41+"]
    df["Pick Tier"] = pd.cut(df["Pk"], bins=pick_bins, labels=labels, right=True)
    avg_by_tier = df.groupby("Pick Tier", observed=False)["W/L%"].mean().reset_index()
    print("\nAverage win percentage by draft pick tier:")
    print(avg_by_tier)

    plt.figure()
    sns.barplot(data=avg_by_tier, x="Pick Tier", y="W/L%", palette="coolwarm")
    plt.title("Average Bulls Win Percentage by Draft Pick Tier")
    plt.xlabel("Draft Pick Tier")
    plt.ylabel("Average Win Percentage")
    plt.ylim(0, 1)
    save_current_figure("average_win_percentage_by_pick_tier.png")


def plot_games_vs_win_percentage(df):
    plt.figure()
    sns.scatterplot(
        data=df,
        x="G",
        y="W/L%",
        hue="Pk",
        palette="Spectral",
        edgecolor="black",
        s=100,
    )
    plt.title("Rookie Games Played vs Bulls Win Percentage")
    plt.xlabel("Rookie Games Played")
    plt.ylabel("Win Percentage")
    save_current_figure("rookie_games_vs_win_percentage.png")

    print(
        "\nCorrelation between rookie games and win percentage:",
        round(df["G"].corr(df["W/L%"]), 3),
    )

    df["Games Group"] = pd.cut(
        df["G"],
        bins=[-1, 20, 40, 60, 82],
        labels=["0-20", "21-40", "41-60", "61-82"],
    )
    avg_games = df.groupby("Games Group", observed=False)["W/L%"].mean().reset_index()
    print("\nAverage win percentage by rookie games played group:")
    print(avg_games)

    plt.figure()
    sns.barplot(data=avg_games, x="Games Group", y="W/L%", palette="magma")
    plt.title("Average Win Percentage by Rookie Games Played Group")
    plt.xlabel("Rookie Games Played Range")
    plt.ylabel("Average Win Percentage")
    plt.ylim(0, 1)
    save_current_figure("average_win_percentage_by_games_group.png")


def plot_correlation_matrix(df):
    stats_cols = ["W/L%", "Pk", "G", "PTS", "TRB", "AST", "FG%", "3P%", "eFG%"]
    stats_df = df[stats_cols].copy()
    correlations = stats_df.corr()

    print("\nCorrelations with win percentage:")
    print(correlations["W/L%"].sort_values(ascending=False))

    plt.figure()
    sns.heatmap(correlations, annot=True, cmap="coolwarm", fmt=".2f", center=0)
    plt.title("Correlation Matrix for Win Percentage and Rookie Metrics")
    save_current_figure("win_percentage_rookie_metrics_correlation_matrix.png")


def plot_key_rookie_metrics(df):
    metrics = ["PTS", "TRB", "AST", "FG%"]

    for metric in metrics:
        safe_metric = metric.replace("%", "pct")
        plt.figure()
        sns.scatterplot(
            data=df,
            x=metric,
            y="W/L%",
            hue="Pk",
            palette="viridis",
            edgecolor="black",
            s=100,
        )
        plt.title(f"Rookie {metric} vs Bulls Win Percentage")
        plt.xlabel(f"Rookie {metric}")
        plt.ylabel("Win Percentage")
        save_current_figure(f"rookie_{safe_metric.lower()}_vs_win_percentage.png")


def plot_season_context(df):
    valid_seasons = df.drop_duplicates(subset="Season").sort_values("Season")

    plt.figure()
    plt.plot(valid_seasons["Season"], valid_seasons["W/L%"], marker="o")
    plt.title("Chicago Bulls Win Percentage by Season")
    plt.xlabel("Season")
    plt.ylabel("Win Percentage")
    plt.xticks(valid_seasons["Season"], rotation=45)
    plt.ylim(0, 1)
    plt.grid(True, linestyle="--", alpha=0.5)
    save_current_figure("bulls_win_percentage_by_season.png")

    plt.figure()
    sns.scatterplot(
        data=valid_seasons,
        x="Season",
        y="Finish",
        size="W/L%",
        sizes=(50, 300),
        hue="W/L%",
        palette="coolwarm",
        legend=False,
    )
    plt.gca().invert_yaxis()
    plt.title("Season Finish vs Year (size reflects win percentage)")
    plt.ylabel("Division Finish (1 = best)")
    plt.xticks(valid_seasons["Season"], rotation=45)
    save_current_figure("season_finish_vs_year.png")


def main():
    VISUALS_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(DATA_PATH)
    print_dataset_summary(df)

    plot_pick_vs_win_percentage(df)
    plot_games_vs_win_percentage(df)
    plot_correlation_matrix(df)
    plot_key_rookie_metrics(df)
    plot_season_context(df)

    print("\nEDA complete.")


if __name__ == "__main__":
    main()
