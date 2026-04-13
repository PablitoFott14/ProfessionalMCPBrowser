## sec-edgar-mcp_analyze_8k

### What this tool is used for
Analyzes an 8-K filing for specific events and items.

---

### Used parameters

**(2) identifier: Required**
Default: No default
Company ticker symbol or CIK number used to identify the company.

**(5) accession_number: Required**
Default: No default
Accession number of the 8-K filing to analyze.

---

### JSON input alternatives

```json
{
  "intent": "Analyze a specific 8-K filing for NVIDIA",
  "params": {
    "identifier": "NVDA",
    "accession_number": "0001045810-24-000123"
  }
}
```

```json
{
  "intent": "Analyze a specific 8-K filing using a company CIK and accession number",
  "params": {
    "identifier": "0001045810",
    "accession_number": "0001045810-24-000123"
  }
}
```
