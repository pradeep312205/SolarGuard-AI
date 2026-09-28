# SolarGuard AI – Day 6
## Functional Solar Maintenance Assistant

### Team Information

- Team Number: 32
- Team Name: Phoneix
- Project Name: SolarGuard AI

---

## 1. Day 6 Objective

The objective of Day 6 is to develop the functional solar maintenance assistant.

The assistant allows technicians to enter maintenance-related questions and receive relevant troubleshooting and maintenance guidance.

---

## 2. Assistant Workflow

Technician Question
        |
        v
SolarGuard AI Assistant
        |
        v
Maintenance Knowledge Base
        |
        v
Issue Identification
        |
        v
Relevant Maintenance Guidance
        |
        v
Technician Response

---

## 3. Supported Maintenance Areas

The prototype provides guidance for:

- Low solar energy output
- Solar panel dust and cleaning
- Inverter issues
- Solar panel inspection
- General solar maintenance

---

## 4. Backend Integration

The technician's question is sent from the web interface to the Flask backend through the `/chat` endpoint.

The backend searches the maintenance knowledge base for matching keywords.

The relevant maintenance category is selected and the corresponding maintenance steps are returned to the frontend.

---

## 5. Frontend Integration

The web interface provides:

- Technician question input
- Ask Assistant button
- Maintenance response area

JavaScript sends the question to the `/chat` API and displays the returned maintenance guidance.

---

## 6. Example

### Technician Question

```text
Why is my solar output low?