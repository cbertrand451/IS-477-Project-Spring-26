# Status Report

### Chicago Bulls NBA Draft Picks vs Season Outcomes
#### Colin Bertrand and Reed Haas



## Task updates

To restate the goal of this project, we want to determine how teams’ draft strategies and behaviors influence team success in their upcoming season. We start by manually downloading two different datasets from basketball-reference.com shown in the data folder of the repository. We plan to integrate these datasets together and run preprocessing, and machine learning analyses on the combined dataset to answer our research questions. We also plan to create new variables that we will treat as the response in linear regression models, which is the difference in win percentage between adjacent teams. To generalize this, we want to see if the team performed better or worse with the introduction of this rookie. We intend to stick to our timeline (as seen below) and complete each task within the given week.

## Updated timeline

#### April 15 - 17th

- **Colin**: Once both datasets are ready, integrate data based on season. There may be multiple players per season, meaning that each individual player will have the correlating season outcome. 
- **Reed**: Clean joined dataset after integration, checking for any incorrect formatting or bad joining methods
- **Reed and Colin**: Perform basic exploratory data analysis on initial joined dataset. Colin can focus on NBA draft statistics, like average draft pick number or player analytics, while Reed can focus on season outcome statistics, like how far did the team make it on average, and how many wins the team got that season. 

---

#### April 20 - 24th

- **Colin**: Find correlations between the rank of the pick for the rookie and the winning percentage of the Chicago Bulls that season. Create a visualisation based on that relationship, likely a heatmap, to showcase how picks affect season outcomes.
- **Reed**: Create a linear regression model of draft characteristics against team winning percentage, as well as a linear model of draft characteristics against winning percentage differential between adjacent seasons. Evaluate the performance of each model compared to the results.
- **Reed and Colin**: Take note of results, and find any stand out correlations that may come from the pick/season outcome relationship, the linear models, or both. 

---

#### April 27 - May 1st

- **Colin**: Create additional visualisations based on correlation between pick rank and season outcome. Depending on correlation, visualisation can be line plot, scatter plot, etc. Also analyze whether number of games played by a rookie has an effect on season outcome. This statistics can also be visualised by a plot, either line plot or box plot. 
- **Reed**: Create visualisations for linear models, and finalize results from the linear models into a summarized report. 
- **Reed and Colin**: Create a detailed report of the results, as well as finish the final project submission with the pipeline and analytical results found from the project. Include visualisations and code made/used in the project.

## Project plan changes

The 2025 season can now be included in this analysis because their season is over as of April 12th, 2026.

We also updated the project plan with the comments that were left to us. We updated the timeline with weekly tasks and shared goals. The constraints and gap sections were updated with relevant course info, as well as talking about additional issues we may run into. We updated the dataset descriptions with howo we will be merging the data, as well. 

## Challenges

Scraping data from basketball-reference.com no longer is feasible. Colin tried multiple scripts from previous users on GitHub, tried public APIs, libraries built specifically for that website, but all actions were blocked with a 403 credential by the site. More research found that basketball-reference.com blocked many attempts to scrape due to bot activity. This forced Colin to manually download data from basketball-reference.com and programatically merge the data together. 

The rookie year data also had to be added manually, which proved to be time consuming. Some of the players had columns that others didn't so additional steps needed to be taken in the cleaning process to make sure that each rookie had the same statistical columns.

## Teammate Role Summary

**Reed**: I've updated the repository with a new folder "code" that will house all of our relevant coding pipelines from cleaning, integrating, processing, and analyzing data. I also made a "data folder" that will house both raw & cleaned data (naming will differentiate the cleaned datasets). I used a Jupyter notebook to clean Dataset 2, where I specifically dropped columns that had missing values or were unnecessary to the project. (ex: dropped "League" column since the Bulls have played in the NBA since 2000, the beginning of our timeline, so it tells us no new information). I also reformatted the "Season" column so it removes the appended year (i.e. removed "-26" from "2025-26") and then converted the column data type to integer so we have a primary key to join both datasets on.
