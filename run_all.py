import subprocess
import os


def run(script_path):
    print(f"\nRunning: {script_path}")
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"

    result = subprocess.run(
        ["python", script_path],
        capture_output=True,
        text=True,
        encoding="utf-8",
        env=env,
    )
    print(result.stdout)

    if result.returncode != 0:
        print(result.stderr)
        raise RuntimeError(f"Script failed: {script_path}")

    print(f"Completed: {script_path}")


def main():
    print("Starting full workflow automation...\n")

    # acquire data
    run("scripts/acquire/acquire_draft_data.py")
    # WARNING!! This script may take 2-5 minutes to run as it scrapes basketball-reference.com for rookie stats
    # I set a manual timer in between each scrape so that the IP address of the user doesn;t get banned
    # basketball-reference.com has a 1 hour ban for super fast botting, I believe
    run("scripts/acquire/acquire_rookie_data.py")
    # manual season dataset only needs checksum creation
    run("scripts/acquire/chicago_bulls_season_data_sha256.py")
    # check the integrity of the data using checksum and sha
    run("scripts/acquire/check_sha256.py")


    # clean and combine draft picks with rookie-year stats
    run("scripts/clean/clean_draft_data.py")
    run("scripts/clean/clean_bulls_data.py")
    # integrate the now cleaned datasets
    run("scripts/integrate/integrate_cleaned_datasets.py")
    # clean the integrated dataset for analysis
    run("scripts/clean/clean_integrated_data.py")

    # run the eda analyzing
    run("scripts/analyze/dataset_eda.py")
    # create the model and visualizations
    run("scripts/analyze/modeling.py")

    
    print("\nWorkflow finished\n")


if __name__ == "__main__":
    main()
