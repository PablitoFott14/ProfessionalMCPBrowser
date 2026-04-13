## financial-datasets_get_sec_filings

### What this tool is for
SEC filings submitted by a company to the U.S. Securities and Exchange Commission. Useful when the user needs to review regulatory disclosures, financial reports, or material event announcements for a given company.

---

### Used parameters

**(1) ticker — Required**
Default: No default
Ticker symbol of the company whose filings are being retrieved.

**(2) limit — Optional**
Default: 10
Controls how many filings are returned.

**(3) filing_type — Optional**
Default: null
Allowed: 10-K, 10-Q, 8-K, 4, DEF 14A, S-1
Filters results to a specific filing type.

---

### JSON input alternatives

```json
{
  "tool": "financial-datasets_get_sec_filings",
  "intent": "Get the most recent annual reports filed by Apple",
  "params": {
    "ticker": "AAPL",
    "filing_type": "10-K"
  }
}
```

```json
{
  "tool": "financial-datasets_get_sec_filings",
  "intent": "Retrieve the last 20 SEC filings for Tesla across all types",
  "params": {
    "ticker": "TSLA",
    "limit": 20
  }
}
```
