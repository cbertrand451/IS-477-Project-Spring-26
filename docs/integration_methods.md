# Integration Methods

This document explains how the datasets were combined for this project.

---

# Rookie Data and Draft Data

The rookie data and draft data were combined first.

The draft data had one row for each Chicago Bulls draft pick. The rookie data was stored as seperate csv files, with one file for each player.

To combine these, the player name was used as the matching value.

The script looked at each rookie csv file, got the player name from the file name, and matched it to the same player in the draft data.

Then, the rookie year stats were added onto the draft row for that player.

This created one cleaned draft dataset that had:

- Draft year
- Draft round
- Draft pick number
- Player name
- College
- Rookie year stats
- Rookie awards

Some players did not have usable rookie stat files. These players were still kept in the dataset so that real Bulls draft picks were not deleted.

The output from this step was:

**data/processed/draft_data_cleaned.csv**

---

# Draft Data and Bulls Season Data

After the draft and rookie data were combined, the next step was to combine that dataset with the Bulls season data.

The draft dataset used **Year** to show the year the player was drafted.

The Bulls season dataset used **Season** to show the year of the Bulls season.

Before merging, the season value was cleaned so it matched the draft year format. For example, a season like **2023-24** was changed to **2023**.

Then the two datasets were merged by matching:

- **Year** from the draft dataset
- **Season** from the Bulls season dataset

An inner merge was used. only rows with matching years in both datasets were kept.

This created a dataset where each Bulls draft pick was connected to the Bulls season from that same year.

The output from this step was:

**data/processed/integrated_bulls_draft_data.csv**

---

# Final Integrated Dataset

After merging, the integrated dataset was cleaned one more time.

Missing rookie stat values were filled with 0, missing playoff values were filled, and rookie of the year ranking was pulled out into its own column.

The final dataset used for analysis was:

**data/processed/final_bulls_data.csv**

---
