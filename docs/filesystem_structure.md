# Filesystem Structure and Naming Conventions

This document describes the filesystem layout and naming conventions used in the project. 
---

# Project Structure

The project's primary directories include data, scripts, visuals, notebooks, and docs folders. There are also some standalone files in the main project folder.

### Data

The data folder holds the lifecycle and transformation of the raw data used in this project. It holds the raw data taken from basketball-reference.com, and then the processed data created after cleaning and integration.

*data/raw/* holds the original csv files and checksum files. These raw files are not edited directly. This folder includes:

- chicago_draft_data.csv: the raw scraped Chicago Bulls draft table
- bulls_data.csv: the manually downloaded Bulls season data
- rookie_stats_data/: seperate csv files for each drafted player and their rookie year statistics
- .sha256 files: checksum files used to verify that the raw data did not change

*data/processed* holds the cleaned and integrated csv files created by the cleaning scripts. This folder includes:

- draft_data_cleaned.csv: cleaned draft data with rookie year player stats added
- bulls_season_data.csv: cleaned Bulls season data
- integrated_bulls_draft_data.csv: the merged draft and season dataset
- final_bulls_data.csv: the final cleaned dataset used for EDA, modeling, and visuals

### Scripts

The scripts folder holds all of the python scripts used to acquire, clean, integrate, analyze, and visualize the data. It has folders for each major step in the data curation process.

*scripts/acquire/* holds the scripts used to collect data and verify raw files:

*scripts/clean/* holds the scripts used to clean the datasets:

*scripts/integrate/* holds the script used to merge the cleaned datasets:

*scripts/analyze/* holds the scripts used for EDA and modeling:

*scripts/visuals/* is included as a place for visualization scripts if seperate visual scripts are needed.

### Visuals

The visuals folder holds the image outputs generated from the analysis and modeling scripts.

This includes plots such as:

- Bulls win percentage by season
- Draft pick vs win percentage
- Rookie stat relationships with win percentage
- Correlation heatmaps
- Linear regression predicted vs actual results
- Random forest tree and feature importance visuals

All generated .png files are stored in *visuals/* so that the project outputs are seperate from the code and data folders.

### Notebooks

The notebooks folder holds the Jupyter notebooks that were used as scratchwork before the final workflow was turned into scripts.

The notebooks were used to explore the data, test cleaning steps, integrate the datasets, run EDA, and build the models. The final reproducible workflow uses the scripts instead of relying on the notebooks.

### Docs

The docs folder holds the written documentation for the project. These documents explain how the data was acquired, cleaned, structured, and used.

This folder includes:

### Other

- README.md
- requirements.txt
- run_all.py: script responsible for running the entire project workflow in order
- ProjectPlan.md
- StatusReport.md
- .gitignore

---

# Naming Conventions

The following standards were applied project-wide:

- Lowercase file and directory names for most project files
- Words separated by underscores
- No spaces in filenames inside the project workflow folders
- Raw data stored in *data/raw/*
- Cleaned and integrated data stored in *data/processed/*
- Documentation stored as .md files in *docs/*

Some files have different naming because of where they came from or what they represent:

- Rookie stat csv files use player names, so they include capital letters and underscores, such as **Coby_White.csv**
- Some player names have punctuation or special characters because they match the player's actual name from basketball-reference.com.

---
