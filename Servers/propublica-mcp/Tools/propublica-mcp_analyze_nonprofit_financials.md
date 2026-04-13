## propublica-mcp_analyze_nonprofit_financials

### What this tool is used for
Analyzes financial trends and key metrics for a nonprofit organization over a specified number of recent years. Use it when evaluating the financial health, revenue trajectory, or spending patterns of a specific nonprofit.

---

### Used parameters

**(7) ein: Required**
Default: No default
Employer Identification Number of the nonprofit to analyze (9 digits, with or without hyphen).

**(8) years: Optional**
Default: 3
Number of recent years to include in the analysis. Maximum: 10.

---

### JSON input alternatives

```json
{
  "intent": "Analyze the financial trends for a nonprofit over the default 3-year period",
  "params": {
    "ein": "131655952"
  }
}
```

```json
{
  "intent": "Analyze a nonprofit's financial history over a longer period",
  "params": {
    "ein": "131655952",
    "years": 7
  }
}
```
