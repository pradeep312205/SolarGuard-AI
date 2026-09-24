# SolarGuard AI

SolarGuard AI is a machine-learning-based solar energy forecasting and
technician maintenance assistant system.

The project combines:

- Solar energy output prediction using Machine Learning
- Weather parameter analysis
- Technician conversational maintenance assistance
- Web-based dashboard using Flask

## Project Objective

The objective of this project is to forecast solar panel energy output
using weather and environmental parameters and provide technicians with
step-by-step guidance for common solar panel maintenance situations.

## Features

### 1. Solar Energy Forecasting

The system accepts:

- Temperature
- Humidity
- Solar Irradiance
- Cloud Cover
- Wind Speed
- Panel Temperature

A Random Forest Regression model is used to predict solar energy output.

### 2. Technician Maintenance Assistant

The assistant provides maintenance guidance for situations such as:

- Low solar output
- Dirty solar panels
- Inverter warnings
- Panel inspection
- General maintenance

### 3. Web Dashboard

The application provides a web interface where users can:

- Enter weather parameters
- Predict solar energy output
- View prediction results
- Ask maintenance questions
- View actual vs predicted energy charts

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Flask
- Joblib
- HTML
- CSS
- JavaScript
- JSON
- Matplotlib

## Machine Learning Algorithm

Random Forest Regression is used for solar energy prediction.

### Input Features

```text
Temperature
Humidity
Solar Irradiance
Cloud Cover
Wind Speed
Panel Temperature