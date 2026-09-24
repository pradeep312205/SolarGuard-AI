import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# 1. Load dataset
data = pd.read_csv("data/solar_data.csv")

print("Dataset loaded successfully!")
print("Dataset shape:", data.shape)


# 2. Select input features
features = [
    "temperature",
    "humidity",
    "irradiance",
    "cloud_cover",
    "wind_speed",
    "panel_temperature"
]

X = data[features]

# Target variable
y = data["energy_output"]


# 3. Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))


# 4. Create Random Forest model
model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)


# 5. Train model
model.fit(X_train, y_train)

print("Model training completed!")


# 6. Make predictions
predictions = model.predict(X_test)


# 7. Evaluate model
mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
rmse = mse ** 0.5
r2 = r2_score(y_test, predictions)


print("\nModel Performance")
print("---------------------------")
print("MAE  :", round(mae, 3))
print("RMSE :", round(rmse, 3))
print("R2   :", round(r2, 3))


# 8. Save trained model
joblib.dump(model, "model/solar_model.pkl")

print("\nModel saved successfully!")
print("Location: model/solar_model.pkl")