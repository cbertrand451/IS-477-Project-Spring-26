# Project Plan

### Chicago Bulls NBA Draft Picks vs Season Outcomes
#### Colin Bertrand and Reed Haas



## Overview

The overall goal of this project is to determine how teams’ draft strategies and behaviors influence team success in their upcoming season. With the NBA lottery and the  variability in player stats and build coming out of high school and college, general managers for NBA teams want to get any type of drafting advantage they can to maximize wins. In this project, we’ll look at the Chicago Bulls as a case study, and examine their drafting habits characterized by the player and pick in the draft, and examine the relationship between them and the success of the team from 2000 to 2025. We’ll pull data regarding the Chicago Bulls season statistics, specifically highlighting wins and win-percentage as the response variable. We’ll also look at a dataset that holds draft players and picks as each observation, including features such as games played, pick number, player name, and rookie year metrics performance metrics. We plan to explore this relationship using a linear regression model with draft features as explanatory variables, and either wins or win percentages as the response variable. We’ll also use statistical models to determine whether the draft pick made a significant impact on the change in winning percentage for the following season compared to the last season. To examine the overall effect, we’ll use the differential in winning percentage between each year as a response variable, and draft characteristics as features.

## Team

**Colin**: In charge of scraping and curating the NBA Draft datasets. The current scraper downloads each season draft as an individual csv, so they will need to be combined with the index being the year. After being filtered for Chicago Bulls players, Colin will also scrape the data from each rookie’s year to get their stats from that specific season. Those stats will be added to the rookie’s information. Colin will be in charge of curating and cleaning that dataset. 

**Reed**: In charge of cleaning the Chicago Bulls season-by-season dataset and preparing dataset for further analysis. The data will need to be exported from the source website, and will hold each season dating back to 1967 as an observation. Reed will filter for seasons playing after 1999, and create a new response variable that takes the differential of adjacent seasons’ win percentages.

When both datasets are cleaned and curated, Colin and Reed will work collaboratively to analyze the statistics from each season. 

## Research or Business Question(s):

- How does a team's draft pick affect the team's season outcome? 
- Do the number of games played by that rookie affect how well the team does?
- Did the draft pick improve the win percentage from the previous year?

## Datasets

#### Dataset 1: 

NBA Draft Data scraped from basketball-reference.com using scrapers found on GitHub by user “kashav” on their page https://github.com/kshvmdn/nbadrafts/tree/master. Uses draft seasons from 2000 to present day. It contains the ranks of all the picks, team with the pick, player selected, and all of the player’s present day stats in the NBA. The player’s rookie year stats will be scraped using their name on basketball-reference.com, and be used in place of their current day stats. This dataset contributes to the research questions by providing the rank of the pick the team had for each season, as well as how big of an impact that rookie had on a team based on their statistics

#### Dataset 2:

The season outcomes of the Chicago Bulls from 2000 to present day. The data was exported from basketball-reference.com using the site’s export option. This dataset includes the season, number of wins, losses, and win percentage, along with final season outcomes. 

The key identifiers between these datasets will be the season. The NBA draft dataset will be filtered for Chicago Bulls picks later in the data lifecycle, which will allow us to add season outcomes to the rookie(s) draft pick based on the season they were picked. 

## Timeline

Both Colin and Reed will work on downloading and curating their own dataset. This can be done individually. This will be done by the next interim status report.

- Scrape basketball data from basketball-reference.com
- Combine each season draft into master draft dataset
- Filter for Chicago Bulls picks
- Scrape player data from their rookie year on basketball-reference.com
- Clean data, derive new columns, drop unnecessary columns
- Integrate season outcome dataset into Chicago Bulls Draft Picks dataset

April will be time to start analysis using the two datasets. They will be integrated based on season, so that each pick will have the season, rank, and season outcomes. These picks will be used in the linear regression models to find the correlation between draft picks and season outcomes. 

- Integrate datasets based on season
- Exploratory data analysis
- Correlations between pick rank and winning percentage
- Key visualization depicting relationship
- Linear regression of draft characteristics against team winning percentage
- Linear regression of draft characteristics against winning percentage differential between adjacent seasons
- Evaluate the performance of the model compared to the results

We will take notes of results, and try to find any stand out correlations between these variables. These will allow us to create visualizations for the models and the results, which will better display the effects a rookie has on the team. 

- Find correlation between draft pick rank and season outcome
- Find whether number of games played by the rookie has an effect on season outcome
- Visualize season outcome vs draft rank with a line plot
- Visualise season outcome vs games played with line plot
- Or add on to previous visualisation by showing games played with color/hues
- Summarize results in report

## Constraints

Data was downloaded and exported legally, as long as basketball-reference.com is properly cited as the owner of the data. Players can be utilized for different purposes during an NBA season. A rookie may not be chosen for their high point percentage, but rather their defensive ability. This is a narrative that can’t be displayed to the naked eye. It can be shown through deeper data analysis, but may not always be shown in the analysis that this project entails. These qualities of a rookie can still contribute to the overall team’s success, so they don’t need to be ruled out. A winning season can also be attributed to multiple factors. It doesn’t always come down to how well the rookie is performing, so there may be slight inconsistencies. Most teams have multiple picks in each draft. This is why rank plays an important role, because a higher draft pick will likely do better for a team than a lower draft pick. We will have to find a way to efficiently display those relationships between the rookie players on the Chicago Bulls, and whether a certain rookie gets more playtime than the other. 

## Gaps

One known gap is that the datasets do not include college performance metrics, more generally the reason why players were drafted at the position they were drafted at. It is hard to contextualize a player’s rank without college performance metrics. Another limitation is the difference in team drafting tendencies, and biases shown by each team. The Chicago Bulls may show patterns in their drafting habits, and that limits the predictive power of any regression models for other teams if trained on data unique to the Chicago Bulls
