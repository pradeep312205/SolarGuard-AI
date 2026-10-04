# SolarGuard AI – Day 8
## Evaluation – Forecast and Troubleshooting Accuracy

### Team Information

- Team Number: 32
- Team Name: Phoneix
- Project Name: SolarGuard AI

---

## 1. Day 8 Objective

The objective of Day 8 is to evaluate the solar energy forecasting model and the SolarGuard AI maintenance assistant.

The evaluation focuses on:

- Forecasting performance
- Maintenance query accuracy
- Troubleshooting response relevance
- Safety and escalation guidance

---

## 2. Forecasting Model Evaluation

The SolarGuard AI forecasting model predicts solar energy output using weather and solar-panel parameters.

The input parameters include:

- Temperature
- Humidity
- Irradiance
- Cloud Cover
- Wind Speed
- Panel Temperature

The target value is:

- Energy Output

The forecasting model uses a Random Forest Regression approach.

---

## 3. Forecasting Metrics

The model evaluation uses the following metrics:

### Mean Absolute Error (MAE)

MAE measures the average absolute difference between predicted and actual energy output.

Lower MAE indicates better prediction performance.

### Root Mean Squared Error (RMSE)

RMSE measures the prediction error while giving greater importance to larger errors.

Lower RMSE indicates better prediction performance.

### R² Score

R² indicates how well the model explains the variation in the target energy output.

A value closer to 1 indicates better performance.

---

## 4. Forecasting Evaluation Result

The forecasting metrics are obtained from the trained Random Forest model using the available demonstration dataset.

The dataset is small and is intended for project demonstration and prototype evaluation rather than production deployment.

MAE: To be recorded from model evaluation

RMSE: To be recorded from model evaluation

R² Score: To be recorded from model evaluation

---

## 5. Maintenance Assistant Evaluation

The maintenance assistant was evaluated using the Day 7 test cases.

A total of 8 maintenance and solar-fault queries were tested.

| Evaluation | Result |
|---|---:|
| Total Queries Tested | 8 |
| Correct Responses | 8 |
| Incorrect Responses | 0 |
| Troubleshooting Accuracy | 100% |
| Test Pass Rate | 100% |

---

## 6. Troubleshooting Evaluation

The assistant was tested for:

- Low solar output
- Solar panel cleaning
- Inverter issues
- Solar panel inspection
- General maintenance
- Solar generation problems

The tested queries returned the expected maintenance categories and relevant maintenance guidance.

---

## 7. Safety Evaluation

The maintenance guidance was checked for safety-related instructions.

The assistant provides safety-oriented guidance and recommends escalation to qualified personnel for electrical faults.

The system is designed to avoid unsupported equipment-specific instructions.

---

## 8. Overall Evaluation

The Day 8 evaluation shows that the current SolarGuard AI prototype successfully handles the tested maintenance scenarios.

The forecasting model is evaluated using MAE, RMSE and R² metrics.

The maintenance assistant achieved a 100% pass rate on the eight test cases used during Day 7.

Because the forecasting dataset is small, the model results should be considered prototype-level evaluation results and not production-level performance.

---

## 9. Day 8 Result

SolarGuard AI forecasting and maintenance troubleshooting performance were evaluated using appropriate metrics and test cases.

### Status

Day 8 Evaluation Completed
MAE: 0.676

RMSE: 0.701

R² Score: 0.923
## 4. Forecasting Evaluation Result

The trained Random Forest Regression model was evaluated using the available demonstration dataset.

The obtained evaluation metrics are:

| Metric | Result |
|---|---:|
| MAE | 0.676 |
| RMSE | 0.701 |
| R² Score | 0.923 |

The R² score of 0.923 indicates that the model explains a large portion of the variation in the test data.

The MAE and RMSE represent the prediction error on the available test samples.

Because the dataset is small and intended for project demonstration, these results should be considered prototype-level evaluation results rather than production-level performance.