# Data Acquisition Instructions

This document describes the process used to acquire the two datasets for this project.

---

# Overview of Data Sources

## Dataset 1: Chicago Bulls Draft Data
- **URL:** https://www.basketball-reference.com/teams/CHI/draft.html, 39 misc Player Pages
- **Format:** CSV  
- **Source:** basketball-reference.com

## Dataset 2: Chicago Bulls
- **URL:** https://www.basketball-reference.com/teams/CHI/
- **Access Method:** Manual download 
- **Format:** CSV  
- **Stored at:** data/raw/bulls_data.csv

Both datasets were found on basketball-reference.com

The first dataset(S) were acquired programatically. The table with all of the bulls historical draft picks was scraped using pandas read html feature. Then, using the names of the drafted players, a url was crafted for each player, and their rookie year stats were also scraped. 

**IMPORTANT**: when running the acquisition script for the rookie year stats, the script may take 2-5 minutes. A manual timer had to be set in between each request. Sport Reference allows a maximum of 20 requests per minute, and if that is passed, the IP address of the user can get "jailed" for up to an hour. The script stays closer to 10 requests per minute to avoid that limit.

The second dataset was acquired manually on basketball-reference.com, bu clicking the "Share & Export" option above the dataset we wanted, and then copy and pasted into a new csv file.

---

# Files Created by Acquisition Scripts and Manual Downloads

Running the acquisition scripts produces the following files:

- data/raw/chicago_draft_data.csv
- data/raw/chicago_draft_data.sha256

Manually added the following file:
- data/raw/bulls_data.csv

Generated checksum file for the manually added file:
- data/raw/bulls_data.sha256

Raw data files are stored in *data/raw/* and never modified.  

---

# Reproducing Data Acquisition

To reproduce the acquisition process, run the following scripts from the project root:

### Step 1: Download Draft Data

python scripts/acquire/acquire_draft_data.py

### Step 2: Scrape the Rookie Year Data

python scripts/acquire/acquire_rookie_data.py

Manually download the dataset from basketbal-reference.com at the provided URL and save it to:

data/raw/bulls_Data.csv

URL: https://www.basketball-reference.com/teams/CHI/

Then run the following script to generate the checksum file for the manually downloaded dataset:
python scripts/acquire/chicago_bulls_season_data_sha256.py

The scripts will download datasets and create the necessary checksum files for integrity verification.
---

# Verify Data Integrity

Verify the integrity of the downloaded files by runnning the check sha256 python script:

python scripts/acquire/check_sha256.py

This will compare the computed SHA-256 checksums against the stored checksum files to ensure data integrity. an output of "MATCH" means a succesful verification, and "MISMATCH" means unsuccessful.

---

# Licensing and Ethical Considerations

### Sports Reference /  Basketball Reference

Terms of Use: https://www.sports-reference.com/termsofuse.html

Sports Reference says they support "data democratization", meaning they allow for the use and modification of the data found on their webpages. 

They state that they do not support aggressive scraping or botting. Sport Reference allows a maximum of 20 requests per minute. To stay safely below that limit and avoid getting temporarily "jailed" by the site, the rookie data acquisition script waits between requests and runs closer to 10 requests per minute. This keeps the workflow reproducible without overwhelming the servers or limiting the site for other users.
