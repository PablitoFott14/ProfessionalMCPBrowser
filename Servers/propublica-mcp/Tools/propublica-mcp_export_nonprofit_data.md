## propublica-mcp_export_nonprofit_data

### What this tool is used for
Exports comprehensive data for multiple nonprofit organizations in JSON or CSV format, optionally including financial analysis and filing history. Use it when consolidating data across several nonprofits for analysis or CRM integration.

---

### Used parameters

**(14) eins: Required**
Default: No default
List of EINs to export. Maximum: 10 organizations.

**(15) format: Optional**
Default: json
Output format for the export.
Allowed: json, csv

**(16) include_financials: Optional**
Default: true
Whether to include financial analysis for each organization in the export.

**(17) include_filings: Optional**
Default: false
Whether to include recent Form 990 filings for each organization in the export.

**(18) max_filings_per_org: Optional**
Default: 3
Maximum number of filings to include per organization when include_filings is true.

---

### JSON input alternatives

```json
{
  "intent": "Export financial data for a set of nonprofits in JSON format",
  "params": {
    "eins": ["131655952", "530196605", "941156365"]
  }
}
```

```json
{
  "intent": "Export nonprofit data including filings in CSV format for CRM import",
  "params": {
    "eins": ["131655952", "530196605"],
    "format": "csv",
    "include_financials": true,
    "include_filings": true,
    "max_filings_per_org": 5
  }
}
```
