# Analysis and Modeling

This document explains the EDA and modeling steps used in the project.

---

# EDA Steps

The EDA was done using the final cleaned dataset:

**data/processed/final_bulls_data.csv**

The goal of the EDA was to understand the data before building models.

The first step was to print basic dataset information, including:

- Number of rows and columns
- Column names
- Data types
- Missing values
- Numeric summaries
- Season range
- Player count
- Playoff value counts

This helped check that the final dataset was ready for analaysis.

---

# EDA Visuals

The EDA script created several visuals to look for patterns in the data.

These visuals were saved in the **visuals** folder.

The visuals helped compare draft position, rookie peformance, and Bulls season results

---

# Modeling Goal

The modeling goal was to see if rookie draft pick information could help predict the Bulls season win percentage.

The target variable was:

**W/L%** (win vs lose percentage)

The model used draft and rookie features such as:

- Round
- Pick number
- Age
- Position
- Games played
- Games started
- Minutes
- Shooting stats
- Rebounds
- Assists
- Steals
- Blocks
- Turnovers
- Points
- Rookie of the year rank

College was filled when missing, but the main model features focused on the numeric rookie stats and player position.

---

# Linear Regression Model

The first model was a linear regression model.

Before fitting the model:

- Numeric features were standardized
- Position was one-hot encoded
- The data was split into training and testing data

The linear regression model was used as a simple baseline model.

The model created a predicted vs actual plot so we could compare the real Bulls win percentage to the predicted win percentage.

The output visual was:

**visuals/linear_regression_predicted_vs_actual.png**

---

# Random Forest Model

The second model was a random forest regressor.

This model was used because it can find more complex relationships than linear regression.

Grid search was used to test different random forest settings, including:

- Number of trees
- Tree depth
- Minimum samples needed to split
- Minimum samples in a leaf

The random forest model was then evaluated using mean squared error.

The model also created feature importance results, which showed which variables mattered most in the model.

The random forest outputs were:

**visuals/best_regressor_rf_importance.png**

**visuals/best_regressor_rf_tree.png**

---

# Final Notes

The models were useful for exploring possible relationships between Bulls draft picks and season success.

The random forest model performed better than the linear regression model, but the dataset is still small.

---
