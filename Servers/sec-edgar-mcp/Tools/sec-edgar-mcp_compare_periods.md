## sec-edgar-mcp_compare_periods

### What this tool is used for
Compares a financial metric across different time periods.

---

### Used parameters

**(2) identifier: Required**
Default: No default
Company ticker symbol or CIK number used to identify the company.

**(11) metric: Required**
Default: No default
Financial metric to compare across periods.

**(12) start_year: Required**
Default: No default
Starting year for the comparison range.

**(13) end_year: Required**
Default: No default
Ending year for the comparison range.

---

### JSON input alternatives

```json
{
  "intent": "Compare NVIDIA revenue across multiple years",
  "params": {
    "identifier": "NVDA",
    "metric": "Revenues",
    "start_year": 2021,
    "end_year": 2024
  }
}
```

```json
{
  "intent": "Compare net income across a date range for a company using its CIK",
  "params": {
    "identifier": "0001045810",
    "metric": "NetIncomeLoss",
    "start_year": 2020,
    "end_year": 2023
  }
}
```
