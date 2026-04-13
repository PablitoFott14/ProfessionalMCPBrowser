## sec-edgar-mcp_analyze_form4_transactions

### What this tool is used for
Analyzes Form 4 filings and extracts detailed transaction data including insider names, transaction amounts, share counts, prices, and ownership details.

---

### Used parameters

**(2) identifier: Required**
Default: No default
Company ticker symbol or CIK number used to identify the company.

**(7) days: Optional**
Default: 90
Number of days to look back for Form 4 filings in this tool.

**(4) limit: Optional**
Default: 50
Maximum number of filings to analyze in this tool.

---

### JSON input alternatives

```json
{
  "intent": "Analyze recent Form 4 transactions for NVIDIA",
  "params": {
    "identifier": "NVDA"
  }
}
```

```json
{
  "intent": "Analyze Form 4 transactions for a company over the last month",
  "params": {
    "identifier": "AAPL",
    "days": 30,
    "limit": 25
  }
}
```
