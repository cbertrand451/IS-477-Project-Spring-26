from pathlib import Path

import matplotlib

matplotlib.use("Agg")

# imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


PROJECT_ROOT = Path(__file__).resolve().parents[2]


data_path = PROJECT_ROOT / 'data/processed/final_bulls_data.csv'
df = pd.read_csv(data_path)

print('Loaded dataset with rows:', len(df), 'and columns:', len(df.columns))
print(df.head())

print(df.columns)

df_train = df[['W/L%', 'Rd', 'Pk', 'College', 'Age', 'Pos', 'G', 'GS',
       'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', '2P', '2PA', '2P%',
       'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK',
       'TOV', 'PF', 'PTS', 'ROY']]

df_train["College"] = df_train["College"].fillna("None")

X_train, X_test, y_train, y_test = train_test_split(df_train.drop('W/L%', axis=1), df_train['W/L%'], test_size=0.2, random_state=42)

# create a linear regression pipeline
numeric_features = ['Rd', 'Pk', 'Age', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
categorical_features = ['Pos']

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder

numeric_transformer = Pipeline(steps=[
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

model.fit(X_train, y_train)

import os
folder_name = PROJECT_ROOT / "visuals"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# linear regression plot of predicted vs actual
predictions = model.predict(df_train)
plt.figure(figsize=(8, 6))
sns.scatterplot(x=df_train['W/L%'], y=predictions)
plt.xlabel('Actual W/L%')
plt.ylabel('Predicted W/L%')
plt.title('Linear Regression: Predicted vs Actual W/L%')
plt.plot([df_train['W/L%'].min(), df_train['W/L%'].max()], [df_train['W/L%'].min(), df_train['W/L%'].max()], 'r--')  # line for perfect predictions
plt.savefig(os.path.join(folder_name, "linear_regression_predicted_vs_actual.png"))
plt.tight_layout()
plt.show()

plt.savefig(os.path.join(folder_name, "linear_regression_predicted_vs_actual.png"))

# check coefficients
feature_names = numeric_features + list(model.named_steps['preprocessor'].transformers_[1][1].named_steps['onehot'].get_feature_names_out(categorical_features))
coefficients = model.named_steps['regressor'].coef_
coef_df = pd.DataFrame({'Feature': feature_names, 'Coefficient': coefficients})
coef_df = coef_df.sort_values(by='Coefficient', key=abs, ascending=False)
print(coef_df.head(10))

predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print('Mean Squared Error:', mse)
print('R^2 Score:', r2)

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV


rf_model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(random_state=42))
])

param_grid = {
    'regressor__n_estimators': [100, 200],
    'regressor__max_depth': [None, 10, 20],
    'regressor__min_samples_split': [2, 5],
    'regressor__min_samples_leaf': [1, 2]
}

rf_model = GridSearchCV(rf_model, param_grid, cv=5, n_jobs=-1, scoring='neg_mean_squared_error').fit(X_train, y_train)

# check rf predictions
rf_predictions = rf_model.predict(X_test)
rf_mse = mean_squared_error(y_test, rf_predictions)
rf_r2 = r2_score(y_test, rf_predictions)

print('Random Forest Mean Squared Error:', rf_mse)

# check variable importance
importances = rf_model.best_estimator_.named_steps['regressor'].feature_importances_
feature_names = numeric_features + list(rf_model.best_estimator_.named_steps['preprocessor'].transformers_[1][1].named_steps['onehot'].get_feature_names_out(categorical_features))
importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
importance_df = importance_df.sort_values(by='Importance', ascending=False)
print(importance_df.head(10))

# visualize variable importance
plt.figure(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', data=importance_df.head(10))
plt.title('Top 10 Feature Importances from Random Forest')
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.tight_layout()
plt.savefig(os.path.join(folder_name, "best_regressor_rf_importance.png"))
plt.show()

# visualize best tree
from sklearn.tree import plot_tree
best_rf = rf_model.best_estimator_.named_steps['regressor']
plt.figure(figsize=(20, 10))
plot_tree(best_rf.estimators_[0], filled=True, feature_names=feature_names, max_depth=3, fontsize=10)
plt.savefig(os.path.join(folder_name, "best_regressor_rf_tree.png"))
plt.show()
