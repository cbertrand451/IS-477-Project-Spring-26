# Data Quality Assessment and Cleaning Documentation

This document describes the profiling and cleaning steps performed on the 2 (3 before initial merge) datasets used in this project:  
- Chicago Bulls Draft Data
- Rookie Year Stats
- Bulls historical Season Stats

---

## Data Profiling

### Draft Data
- The raw draft file had 406 rows and 22 columns.
- Basketball-reference repeats the table header inside the table, so rows where **Year** was equal to "Year" had to be removed.
- Some rows did not have a real player value, so they were dropped.
- The dataset had draft picks going back farther than the what we wanted for this project. Only kept the draft data from 2000 and later.
- Some players had the arrow symbol that showed they were not actually kept by the Bulls. These rows were removed because the project is about Bulls draft picks connected to Bulls seasons.
- The original draft data had career stat columns, but the project needed rookie year performance instead. Those columns were removed before adding the rookie year stats.

### Rookie Data
- Rookie year stats were stored as seperate csv files, one for each drafted player.
- Each rookie file was checked to make sure it was not empty and had at least one usable row of stat data.
- The first filled row was used as the rookie season row for the player.
- 35 player files had usable rookie data.
- 4 player files did not have usable rookie rows: Marko Simonovic, JamesOn Curry, Mario Austin, and Tommy Smith.
- These 4 players were kept in the dataset instead of being deleted. Their missing rookie data was cleaned after the merge.

### Season Data
- The raw Bulls season data had 60 rows and 19 columns.
- The **Season** column was stored like *2023-24*, which would not merge cleanly with the draft year column. It was changed to just the first year as an integer, like *2023*.
- The dataset had extra blank divider columns from basketball-reference named *Unnamed: 8* and *Unnamed: 15*. These were dropped.
- The **Finish** column was stored as text, but only the numeric finishing place was needed. It was changed to an integer value when possible.
- The **Lg** column was dropped because every row was NBA data and it did not add anything new to the analysis.

---

## Data Cleaning Steps

Cleaning was done in two main stages. The first stage cleaned the datasets before combining them, and the second stage cleaned the dataset after the merge.

---

## Cleaning Before Merging

### Draft Data and Rookie Data

The draft data was cleaned with:

python scripts/clean/clean_draft_data.py

This produced 39 draft rows and 34 columns.

### Bulls Season Data

The Bulls season data was cleaned with:

python scripts/clean/clean_bulls_data.py


This produced 60 season rows and 16 columns.

---

## Merging the Datasets

The datasets were integrated with:

python scripts/integrate/integrate_cleaned_datasets.py

The merged dataset was saved to:

data/processed/integrated_bulls_draft_data.csv

This produced 39 rows and 50 columns.

---

## Cleaning After Merging

The integrated dataset was cleaned with:

python scripts/clean/clean_integrated_data.py

This produced the final analysis dataset with 39 rows and 51 columns.

---

## Important Notes

- Raw data files in *data/raw/* were not edited directly.
- Cleaned data files were saved in *data/processed/*
- Missing rookie stats were not deleted because deleting them would remove valid Bulls draft picks from the project.
- Some missing **College** values are expected because some players were drafted from high school, overseas, or another paths
- The final dataset is the file that should be used for EDA, modeling, and visualizations:

data/processed/final_bulls_data.csv

---
