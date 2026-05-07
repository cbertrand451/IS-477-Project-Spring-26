# Data Dictionary

This data dictionary describes the varibles used in the project across the raw datasets, cleaned datasets, and final integrated dataset.

---

# Chicago Bulls Draft and Rookie Dataset

**Source:** Basketball Reference  
**Raw Files:** data/raw/chicago_draft_data.csv and data/raw/rookie_stats_data/  
**Cleaned File:** data/processed/draft_data_cleaned.csv

### Variables

| Variable | Type | Description |
|---------|------|-------------|
| Year | int | Year the player was drafted by the Chicago Bulls. |
| Lg | string | League the player was drafted into. |
| Rd | int | Draft round. |
| Pk | int | Overall draft pick number. |
| Player | string | Player name. |
| College | string | College or school listed for the player. |
| Age | float | Player age during rookie season. |
| Pos | string | Player position. |
| G | float | Games played during rookie season. |
| GS | float | Games started during rookie season. |
| MP | float | Minutes played during rookie season. |
| FG | float | Field goals made. |
| FGA | float | Field goals attempted. |
| FG% | float | Field goal percentage. |
| 3P | float | Three pointers made. |
| 3PA | float | Three pointers attempted. |
| 3P% | float | Three point percentage. |
| 2P | float | Two pointers made. |
| 2PA | float | Two pointers attempted. |
| 2P% | float | Two point percentage. |
| eFG% | float | Effective field goal percentage. |
| FT | float | Free throws made. |
| FTA | float | Free throws attempted. |
| FT% | float | Free throw percentage. |
| ORB | float | Offensive rebounds. |
| DRB | float | Defensive rebounds. |
| TRB | float | Total rebounds. |
| AST | float | Assists. |
| STL | float | Steals. |
| BLK | float | Blocks. |
| TOV | float | Turnovers. |
| PF | float | Personal fouls. |
| PTS | float | Points scored. |
| Awards | string | Rookie season awards or award voting notes. |

---

# Chicago Bulls Season Dataset

**Source:** Basketball Reference  
**Raw File:** data/raw/bulls_data.csv  
**Cleaned File:** data/processed/bulls_season_data.csv

### Variables

| Variable | Type | Description |
|---------|------|-------------|
| Season | int | First year of the Bulls season. |
| Team | string | Team name. |
| W | int | Number of wins in the season. |
| L | int | Number of losses in the season. |
| W/L% | float | Bulls win percentage for the season. |
| Finish | int | Division finishing place. |
| SRS | float | Simple Rating System value from Basketball Reference. |
| Pace | float | Team pace for the season. |
| Rel Pace | float | Team pace compared to league average. |
| ORtg | float | Offensive rating. |
| Rel ORtg | float | Offensive rating compared to league average. |
| DRtg | float | Defensive rating. |
| Rel DRtg | float | Defensive rating compared to league average. |
| Playoffs | string | Playoff result for the season. |
| Coaches | string | Bulls coach or coaches for the season. |
| Top WS | string | Player with the top win shares for the Bulls that season. |

---

# Integrated Dataset

**File:** data/processed/final_bulls_data.csv  
**Description:**  
The final intergrated dataset joins the cleaned draft and rookie dataset with the cleaned Bulls season dataset.

The merge connects each drafted player to the Bulls season from the same year.

### Main Integration Variables

| Variable | Type | Description |
|---------|------|-------------|
| Year | int | Draft year from the draft dataset. |
| Season | int | Bulls season year from the season dataset. |

### Variables from Bulls Season Data

| Variable | Type | Description |
|---------|------|-------------|
| Team | string | Team name. |
| W | int | Wins. |
| L | int | Losses. |
| W/L% | float | Win percentage and main modeling target. |
| Finish | int | Division finish. |
| SRS | float | Simple Rating System value. |
| Pace | float | Team pace. |
| Rel Pace | float | Relative pace. |
| ORtg | float | Offensive rating. |
| Rel ORtg | float | Relative offensive rating. |
| DRtg | float | Defensive rating. |
| Rel DRtg | float | Relative defensive rating. |
| Playoffs | string | Playoff result. |
| Coaches | string | Coach or coaches for that season. |
| Top WS | string | Bulls player with the most win shares. |

### Variables from Draft and Rookie Data

| Variable | Type | Description |
|---------|------|-------------|
| Rd | int | Draft round. |
| Pk | int | Overall draft pick number. |
| Player | string | Drafted player name. |
| College | string | College or source school. |
| Age | float | Rookie season age. |
| Pos | string | Player position. |
| G | float | Rookie games played. |
| GS | float | Rookie games started. |
| MP | float | Rookie minutes played. |
| FG | float | Rookie field goals made. |
| FGA | float | Rookie field goals attempted. |
| FG% | float | Rookie field goal percentage. |
| 3P | float | Rookie three pointers made. |
| 3PA | float | Rookie three pointers attempted. |
| 3P% | float | Rookie three point percentage. |
| 2P | float | Rookie two pointers made. |
| 2PA | float | Rookie two pointers attempted. |
| 2P% | float | Rookie two point percentage. |
| eFG% | float | Rookie effective field goal percentage. |
| FT | float | Rookie free throws made. |
| FTA | float | Rookie free throws attempted. |
| FT% | float | Rookie free throw percentage. |
| ORB | float | Rookie offensive rebounds. |
| DRB | float | Rookie defensive rebounds. |
| TRB | float | Rookie total rebounds. |
| AST | float | Rookie assists. |
| STL | float | Rookie steals. |
| BLK | float | Rookie blocks. |
| TOV | float | Rookie turnovers. |
| PF | float | Rookie personal fouls. |
| PTS | float | Rookie points. |
| Awards | string | Rookie awards or voting information. |
| ROY | int | Rookie of the year voting rank pulled from Awards. 0 means no ROY rank. |

---

# Derived Variables

### ROY

ROY was created from the Awards column.

| Value | Definition |
|------|------------|
| 0 | Player had no rookie of the year ranking listed. |
| 1-9 | Player had an ROY ranking listed in Awards. |

### Season

Season was cleaned from a season range into one year. For example, 2023-24 became 2023.

This made it easier to merge with the draft Year column.

---

# Notes on Integration

- Integration is performed by matching Year from the draft data to Season from the Bulls season data.
- The rookie stats were added to the draft data first using player names.
- The final file has 39 rows.
- The final dataset supports analaysis of how draft picks and rookie peformance relate to Bulls season outcomes.

---

# Citation Information

- **Draft Data Source:** basketbal-reference.com Chicago Bulls Draft Register.
- **Rookie Data Source:** Basketball Reference player pages.
- **Season Data Source:** Basketball Reference Chicago Bulls team season page.

---
