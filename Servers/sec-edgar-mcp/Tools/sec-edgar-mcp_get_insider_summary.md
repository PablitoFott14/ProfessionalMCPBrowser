## sec-edgar-mcp_get_insider_summary

### What this tool is used for
Gets a summary of insider trading activity for a company from SEC filings.

---

### Used parameters

**(2) identifier: Required**
Default: No default
Company ticker symbol or CIK number used to identify the company.

**(7) days: Optional**
Default: 180
Number of days of insider trading activity to analyze in this tool.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve an insider trading summary for NVIDIA",
  "params": {
    "identifier": "NVDA"
  }
}
```

```json
{
  "intent": "Retrieve an insider trading summary for a company over the last year",
  "params": {
    "identifier": "AAPL",
    "days": 365
  }
}
```
