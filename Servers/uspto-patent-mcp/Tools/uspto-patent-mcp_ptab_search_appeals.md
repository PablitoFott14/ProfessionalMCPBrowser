## uspto-patent-mcp_ptab_search_appeals

### What this tool is used for
Searches ex parte appeal decisions. Use it when you need to find appeal outcomes where applicants appealed examiner rejections to the PTAB.

---

### Used parameters

**(3) query - Optional**
Default: null
Full-text search query for appeal decisions.

**(11) application_number - Optional**
Default: null
Filters results by application number.

**(9) patent_number - Optional**
Default: null
Filters results by patent number.

**(23) decision_date_from - Optional**
Default: null
Sets the decision date range start for this appeal search.

**(24) decision_date_to - Optional**
Default: null
Sets the decision date range end for this appeal search.

**(4) offset - Optional**
Default: 0
Starting position for pagination in this appeal search.

**(5) limit - Optional**
Default: 25
Maximum number of appeal decision results to return in this tool.

---

### JSON input alternatives

```json
{
  "intent": "Search appeal decisions for a specific application number",
  "params": {
    "application_number": "14412875",
    "limit": 10
  }
}
```

```json
{
  "intent": "Search appeal decisions within a date range for a patent",
  "params": {
    "patent_number": "7123456",
    "decision_date_from": "2023-01-01",
    "decision_date_to": "2023-12-31",
    "limit": 25
  }
}
```
