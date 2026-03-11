Overview: 

The overall goal of this project is to determine how teams’ draft strategies and behaviors influence team success in their upcoming season. With the NBA lottery and the  variability in player stats and build coming out of high school and college, general managers for NBA teams want to get any type of drafting advantage they can to maximize wins. In this project, we’ll look at the Chicago Bulls as a case study, and examine their drafting habits characterized by the player and pick in the draft, and examine the relationship between them and the success of the team from 2000 to 2025. We’ll pull data regarding the Chicago Bulls season statistics, specifically highlighting wins and win-percentage as the response variable. We’ll also look at a dataset that holds draft players and picks as each observation, including features such as games played, pick number, player name, and rookie year metrics performance metrics. We plan to explore this relationship using a linear regression model with draft features as explanatory variables, and either wins or win percentages as the response variable. We’ll also use statistical models to determine whether the draft pick made a significant impact on the change in winning percentage for the following season compared to the last season. To examine the overall effect, we’ll use the differential in winning percentage between each year as a response variable, and draft characteristics as features.

Team:

Colin: In charge of scraping and curating the NBA Draft datasets. The current scraper downloads each season draft as an individual csv, so they will need to be combined with the index being the year. After being filtered for Chicago Bulls players, Colin will also scrape the data from each rookie’s year to get their stats from that specific season. Those stats will be added to the rookie’s information. Colin will be in charge of curating and cleaning that dataset. 

Reed: In charge of cleaning the Chicago Bulls season-by-season dataset and preparing dataset for further analysis. The data will need to be exported from the source website, and will hold each season dating back to 1967 as an observation. Reed will filter for seasons playing after 1999, and create a new response variable that takes the differential of adjacent seasons’ win percentages.

When both datasets are cleaned and curated, Colin and Reed will work collaboratively to analyze the statistics from each season. 

Research or Business Question(s):

- How does a team's draft pick affect the team's season outcome? 
- Do the number of games played by that rookie affect how well the team does?
- Did the draft pick improve the win percentage from the previous year?


