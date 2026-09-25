# SolarGuard AI – Day 2
## Solar Energy Forecasting Model and Maintenance Assistant Workflow

### Team Information

- Team Number: 32
- Team Name: Phoneix
- Project Name: SolarGuard AI

---

## 1. Day 2 Objective

The objective of Day 2 is to develop the solar panel energy output forecasting model and define the workflow for the technician maintenance assistant.

The forecasting component predicts solar panel energy output using weather and panel-related parameters.

The maintenance assistant workflow defines how technician questions will be processed and how suitable maintenance guidance will be provided.

---

## 2. Solar Energy Forecasting

The SolarGuard AI forecasting model predicts solar panel energy output based on the following parameters:

- Temperature
- Humidity
- Irradiance
- Cloud Cover
- Wind Speed
- Panel Temperature

### Target Variable

The target variable is:

`energy_output`

The predicted energy output is measured in kWh.

---

## 3. Machine Learning Algorithm

The project uses the:

**Random Forest Regression**

algorithm for solar energy forecasting.

Random Forest Regression combines multiple decision trees to learn the relationship between weather conditions, panel conditions, and energy output.

The trained model is saved as:

```text
model/solar_model.pkl