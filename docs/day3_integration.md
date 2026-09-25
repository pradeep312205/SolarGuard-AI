# SolarGuard AI – Day 3
## Energy Output and Maintenance Integration

### Team Information

- Team Number: 32
- Team Name: Phoneix
- Project Name: SolarGuard AI

---

## 1. Day 3 Objective

The objective of Day 3 is to connect the predicted solar energy output with relevant maintenance information.

When the forecasting model produces an energy output prediction, SolarGuard AI evaluates the result and provides maintenance guidance.

---

## 2. Day 3 Integration Workflow

```text
Weather and Panel Parameters
            |
            v
     Random Forest Model
            |
            v
    Predicted Energy Output
            |
            v
     Output Level Check
            |
       +----+----+
       |         |
    Low Output  Normal Output
       |         |
       v         v
Maintenance    Routine
Attention      Maintenance
       |         |
       +----+----+
            |
            v
   Maintenance Guidance