## patent-mcp-server_google_search_patents

### What this tool is used for
Google_search_patents searches patent titles and abstracts using Google Patents Public Datasets via BigQuery. It returns publication numbers, titles, abstracts, dates, inventors, assignees, and classification codes. It is used when the user needs broad patent discovery across multiple countries using natural language or keyword queries, rather than USPTO-specific search syntax.

---

### Used parameters

**(2) query — Required**
Default: No default
Search query string. Searches patent titles and abstracts.

**(37) country — Optional**
Default: US
Allowed: US, EP, WO, JP, CN, KR, GB, DE, FR, CA, AU
Country code to scope the patent search.

**(4) limit — Optional**
Default: 100
Maximum number of results to return. Maximum allowed value is 500.

**(14) offset — Optional**
Default: 0
Number of results to skip for pagination.

**(38) start_date — Optional**
Default: null
Start date for filtering by publication date. Integer in YYYYMMDD format (e.g., 20220101).

**(39) end_date — Optional**
Default: null
End date for filtering by publication date. Integer in YYYYMMDD format (e.g., 20251231).

---

### JSON input alternatives

```json
{
  "intent": "Search US patents about solid-state battery technology published since 2022",
  "params": {
    "query": "solid state battery electrolyte",
    "country": "US",
    "start_date": 20220101,
    "limit": 50
  }
}

{
  "intent": "Find international PCT applications related to mRNA vaccine delivery mechanisms",
  "params": {
    "query": "mRNA lipid nanoparticle vaccine delivery",
    "country": "WO",
    "start_date": 20200101,
    "end_date": 20251231,
    "limit": 100
  }
}
```
