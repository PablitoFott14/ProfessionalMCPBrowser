## sec-edgar-mcp_get_insider_transactions

### What this tool is used for
Gets insider trading transactions for a company from SEC filings.

---

### Used parameters

**(2) identifier: Required**
Default: No default
Company ticker symbol or CIK number used to identify the company.

**(16) form_types: Optional**
Default: null
List of insider filing form types to include.

**(7) days: Optional**
Default: 90
Number of days to look back for insider transactions in this tool.

**(4) limit: Optional**
Default: 50
Maximum number of insider transactions to return in this tool.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve recent insider transactions for NVIDIA",
  "params": {
    "identifier": "NVDA"
  }
}
```

```json
{
  "intent": "Retrieve recent Form 4 insider transactions for a company",
  "params": {
    "identifier": "AAPL",
    "form_types": ["4"],
    "days": 30
  }
}
```
