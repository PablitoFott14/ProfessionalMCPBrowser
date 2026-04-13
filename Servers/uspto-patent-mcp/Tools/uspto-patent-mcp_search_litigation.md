## uspto-patent-mcp_search_litigation

### What this tool is used for
Searches patent litigation cases. Use it when you need to research patent enforcement history or find litigation involving specific patents or parties.

---

### Used parameters

**(3) query: Optional**
Default: null
Full-text search query for litigation cases.

**(9) patent_number: Optional**
Default: null
Filters results by patent number.

**(48) plaintiff: Optional**
Default: null
Filters results by plaintiff name.

**(49) defendant: Optional**
Default: null
Filters results by defendant name.

**(50) court: Optional**
Default: null
Filters results by court or district.

**(14) filing_date_from: Optional**
Default: null
Sets the filing date range start for this litigation search.

**(15) filing_date_to: Optional**
Default: null
Sets the filing date range end for this litigation search.

**(4) offset: Optional**
Default: 0
Starting position for pagination in this litigation search.

**(5) limit: Optional**
Default: 25
Maximum number of litigation results to return in this tool.

---

### JSON input alternatives

```json
{
  "intent": "Search litigation involving a specific patent",
  "params": {
    "patent_number": "7861317",
    "limit": 10
  }
}
```

```json
{
  "intent": "Search litigation between named parties within a filing date range",
  "params": {
    "plaintiff": "IBM",
    "defendant": "Apple",
    "filing_date_from": "2023-01-01",
    "filing_date_to": "2023-12-31",
    "limit": 25
  }
}
```
