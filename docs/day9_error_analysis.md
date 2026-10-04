# SolarGuard AI – Day 9
## Error Analysis – Maintenance Recommendations

### Team Information

- Team Number: 32
- Team Name: Phoneix
- Project Name: SolarGuard AI

---

## 1. Day 9 Objective

The objective of Day 9 is to identify incorrect, incomplete, or potentially unsupported maintenance recommendations produced by the SolarGuard AI assistant.

The analysis focuses on difficult and ambiguous technician queries that may expose limitations in the current maintenance retrieval and response system.

---

## 2. Error Analysis Approach

The assistant was reviewed using normal maintenance queries as well as more complex queries involving multiple faults.

The analysis focused on:

- Incorrect maintenance category
- Missing troubleshooting steps
- Incomplete maintenance guidance
- Missing safety instructions
- Missing escalation guidance
- Ambiguous technician questions
- Multiple faults in a single query

---

## 3. Error Analysis Test Cases

| Test ID | Query | Expected Behaviour | Observation |
|---|---|---|---|
| EA01 | My solar panel is producing low power because of an inverter problem. | Identify low output and inverter-related issue. | Review required |
| EA02 | The panel is dirty and the inverter shows a warning. | Consider both cleaning and inverter warning. | Review required |
| EA03 | My solar panel is not generating power at all. | Provide safe troubleshooting and escalation guidance. | Review required |
| EA04 | The inverter has an unknown error code. | Avoid inventing the meaning of the error code. | Review required |
| EA05 | What should I do about my solar system? | Provide general maintenance guidance. | Review required |

---

## 4. Potential Error Categories

### 4.1 Incorrect Category

A technician question may contain multiple issues, making it difficult for simple keyword-based retrieval to select the correct maintenance category.

### 4.2 Missing Context

A short or ambiguous question may not provide enough information to determine the exact fault.

### 4.3 Unsupported Information

The assistant should not invent equipment-specific information or unknown inverter error-code meanings that are not available in the knowledge base.

### 4.4 Safety Limitations

Electrical faults should be escalated to qualified personnel. The assistant should avoid instructions that require an unqualified technician to work inside electrical equipment.

### 4.5 Multiple Faults

A single technician query may contain more than one maintenance issue. The current prototype may prioritize one matching category instead of handling every issue separately.

---

## 5. Error Analysis Findings

The Day 7 tests successfully handled the predefined maintenance queries.

However, additional edge-case testing identifies areas where the prototype can be improved.

The current maintenance assistant uses keyword-based matching against the maintenance knowledge base. Therefore, queries containing multiple issues, unusual wording, or unknown technical information may require improved retrieval and prompt handling.

---

## 6. Improvement Opportunities

The following improvements are identified for the next development stage:

1. Improve maintenance keyword coverage.
2. Handle multiple maintenance issues in one query.
3. Add stronger context-based retrieval.
4. Improve structured maintenance responses.
5. Add explicit safety and escalation guidance.
6. Prevent unsupported technical assumptions.
7. Improve handling of ambiguous technician questions.

---

## 7. Day 9 Result

The error analysis identified limitations in the current prototype, particularly around ambiguous queries, multiple faults, unsupported information, and keyword-based retrieval.

These findings will be used to improve the maintenance retrieval and prompting approach during Day 10.

### Status

Day 9 Error Analysis Completed