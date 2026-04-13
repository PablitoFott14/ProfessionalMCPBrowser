## sec-edgar-mcp_get_recent_filings

### What this tool is used for
Gets recent SEC filings for a company or across all companies.

---

### Used parameters

**(2) identifier: Optional**
Default: null
Company ticker symbol or CIK number to scope the recent filings to one company. If omitted, this tool returns recent filings across all companies.

**(6) form_type: Optional**
Default: null
Specific SEC form type to filter by.

**(7) days: Optional**
Default: 30
Number of days to look back for recent filings.

**(4) limit: Optional**
Default: 40
Maximum number of filings to return in this tool.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve recent SEC filings across all companies from the last month",
  "params": {}
}
```

```json
{
  "intent": "Retrieve recent 10-K filings for NVIDIA from the last two weeks",
  "params": {
    "identifier": "NVDA",
    "form_type": "10-K",
    "days": 14
  }
}
```
