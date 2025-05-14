import pandas as pd
import numpy as np

# Machine Learning Models
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, r2_score
import xgboost as xgb

# -----------------------------
# 1. Simulate Merged Dataset
# -----------------------------
# In real usage, replace this with your actual merged dataset
# e.g., df = pd.read_csv("merged_traffic_weather.csv")
np.random.seed(42)
df = pd.DataFrame({
    'rainfall': np.random.uniform(0, 20, 500),
    'temperature': np.random.uniform(10, 35, 500),
    'wind_speed': np.random.uniform(0, 50, 500),
    'traffic_volume': np.random.uniform(100, 1000, 500)
})

# -----------------------------
# 2. Define Features and Target
# -----------------------------
X = df[['rainfall', 'temperature', 'wind_speed']]  # Weather features
y = df['traffic_volume']                           # Target variable

# -----------------------------
# 3. Train-Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Dictionary to store results
results = {}

# -----------------------------
# 4. Linear Regression Model
# -----------------------------
lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)

results['Linear Regression'] = {
    'R^2 Score': r2_score(y_test, y_pred_lr),
    'MSE': mean_squared_error(y_test, y_pred_lr)
}

# -----------------------------
# 5. Random Forest Regression
# -----------------------------
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)

results['Random Forest'] = {
    'R^2 Score': r2_score(y_test, y_pred_rf),
    'MSE': mean_squared_error(y_test, y_pred_rf)
}

# -----------------------------
# 6. Gradient Boosting (XGBoost)
# -----------------------------
xgbr = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, seed=42)
xgbr.fit(X_train, y_train)
y_pred_xgb = xgbr.predict(X_test)

results['XGBoost'] = {
    'R^2 Score': r2_score(y_test, y_pred_xgb),
    'MSE': mean_squared_error(y_test, y_pred_xgb)
}

# -----------------------------
# 7. Support Vector Regression (SVR)
# -----------------------------
svr = SVR(kernel='rbf', C=100, epsilon=0.1)
svr.fit(X_train, y_train)
y_pred_svr = svr.predict(X_test)

results['Support Vector Regression'] = {
    'R^2 Score': r2_score(y_test, y_pred_svr),
    'MSE': mean_squared_error(y_test, y_pred_svr)
}

# -----------------------------
# 8. Multilayer Perceptron (MLP)
# -----------------------------
mlp = MLPRegressor(hidden_layer_sizes=(64, 32), max_iter=500, random_state=42)
mlp.fit(X_train, y_train)
y_pred_mlp = mlp.predict(X_test)

results['Multilayer Perceptron'] = {
    'R^2 Score': r2_score(y_test, y_pred_mlp),
    'MSE': mean_squared_error(y_test, y_pred_mlp)
}

# -----------------------------
# 9. Display Results
# -----------------------------
results_df = pd.DataFrame(results).T
print("Model Evaluation Results:")
print(results_df)