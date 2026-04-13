## sec-edgar-mcp_analyze_insider_sentiment

### What this tool is used for
Analyzes insider trading sentiment and trends over time.

---

### Used parameters

**(2) identifier: Required**
Default: No default
Company ticker symbol or CIK number used to identify the company.

**(17) months: Optional**
Default: 6
Number of months of insider trading activity to analyze.

---

### JSON input alternatives

```json
{
  "intent": "Analyze insider trading sentiment for NVIDIA",
  "params": {
    "identifier": "NVDA"
  }
}
```

```json
{
  "intent": "Analyze insider trading sentiment for a company over the last year",
  "params": {
    "identifier": "AAPL",
    "months": 12
  }
}
```
