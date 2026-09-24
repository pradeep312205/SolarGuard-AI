import joblib
import pandas as pd

# Load the trained model
model = joblib.load("model/solar_model.pkl")

# New weather conditions
new_data = pd.DataFrame({
    "temperature": [30],
    "humidity": [60],
    "irradiance": [800],
    "cloud_cover": [15],
    "wind_speed": [4],
    "panel_temperature": [40]
})

# Make prediction
prediction = model.predict(new_data)

print("Weather Parameters")
print("----------------------------")
print("Temperature:", new_data["temperature"].iloc[0], "°C")
print("Humidity:", new_data["humidity"].iloc[0], "%")
print("Irradiance:", new_data["irradiance"].iloc[0], "W/m²")
print("Cloud Cover:", new_data["cloud_cover"].iloc[0], "%")
print("Wind Speed:", new_data["wind_speed"].iloc[0], "m/s")
print("Panel Temperature:", new_data["panel_temperature"].iloc[0], "°C")

print("\nPredicted Solar Energy Output:")
print(round(prediction[0], 2), "kWh")