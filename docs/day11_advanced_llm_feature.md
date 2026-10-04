# SolarGuard AI – Day 11
## Advanced LLM Feature

### Team Information

- Team Number: 32
- Team Name: Phoneix
- Project Name: SolarGuard AI

---

## 1. Day 11 Objective

The objective of Day 11 is to add advanced features for fault diagnosis and maintenance scheduling.

The SolarGuard AI assistant is extended to identify possible solar-panel faults and provide maintenance guidance.

A simple maintenance scheduling feature is also added to help technicians plan maintenance activities.

---

## 2. Fault Diagnosis

The fault diagnosis feature analyzes the technician's reported problem.

The system identifies the relevant maintenance category using the available maintenance knowledge base.

Supported fault categories include:

- Low energy output
- Solar panel cleaning
- Inverter problems
- Panel inspection
- General maintenance

The assistant provides:

1. Identified fault
2. Possible cause
3. Recommended inspection
4. Maintenance action
5. Safety guidance

---

## 3. Maintenance Scheduling

A simple maintenance scheduling feature is included.

The technician can provide a maintenance date and maintenance activity.

The system returns a confirmation message containing:

- Maintenance activity
- Scheduled date
- Technician reminder

---

## 4. Fault Diagnosis Workflow

Technician Question
        |
        v
Fault Diagnosis
        |
        v
Maintenance Knowledge Base
        |
        v
Fault Category
        |
        v
Recommended Maintenance Action
        |
        v
Technician Response

---

## 5. Scheduling Workflow

Maintenance Activity
        |
        v
Maintenance Date
        |
        v
Schedule Confirmation
        |
        v
Technician Reminder

---

## 6. Example Fault Diagnosis

### Technician Question

```text
My solar panel output is very low.