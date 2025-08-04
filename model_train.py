# model_train.py - Ridge Regression for App Subscription Revenue Prediction

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
import pickle
import os

# Load dataset
df = pd.read_csv("app_subscription_data.csv")

# Features (independent variables) and Target (dependent variable)
X = df[["Active_Users", "Ad_Spend", "Churn_Rate", "In_App_Revenue"]]
y = df["Monthly_Revenue"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Ridge Regression Model
model = Ridge(alpha=1.0)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Model Performance
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("Model Performance:")
print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R² Score:", r2)

# Save model
os.makedirs("model", exist_ok=True)
pickle.dump(model, open("model/model.pkl", "wb"))

print("✅ Model saved to model/model.pkl")
