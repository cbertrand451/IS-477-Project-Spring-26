# Chicago Bulls Rookie Evaluation Status Report
Reed Haas & Colin Bertrand

## Task updates

## Updated timeline

## Project plan changes

Scraping data from basketball-reference.com no longer is feasible. Colin tried multiple scripts from previous users on GitHub, tried public APIs, libraries built specifically for that website, but all actions were blocked with a 403 credential by the site. More research found that basketball-reference.com blocked many attempts to scrape due to bot activity. This forced Colin to manually download data from basketball-reference.com and programatically merge the data together. 

## Challenges

- basketball-reference.com data scraping: site consistently gave 403 status code, meaning access was denied to the site through requests library. 

## Teammate Role Summary

**Reed**: I've updated the repository with a new folder "code" that will house all of our relevant coding pipelines from cleaning, integrating, processing, and analyzing data. I also made a "data folder" that will house both raw & cleaned data (naming will differentiate the cleaned datasets). I used a Jupyter notebook to clean Dataset 2, where I specifically dropped columns that had missing values or were unnecessary to the project. (ex: dropped "League" column since the Bulls have played in the NBA since 2000, the beginning of our timeline, so it tells us no new information). I also reformatted the "Season" column so it removes the appended year (i.e. removed "-26" from "2025-26") and then converted the column data type to integer so we have a primary key to join both datasets on.
