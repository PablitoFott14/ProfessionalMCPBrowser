## patent-mcp-server_google_search_by_assignee

### What this tool is used for
Google_search_by_assignee searches Google Patents for patents assigned to a specific company or organization. It is used when the user wants to analyze a company's patent portfolio, track filings by a particular assignee, or research patent ownership within a country or date range.

---

### Used parameters

**(42) assignee_name — Required**
Default: No default
Assignee or company name to search for.

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
  "intent": "Find all US patents assigned to a specific company",
  "params": {
    "assignee_name": "Acme Corporation",
    "country": "US",
    "limit": 100
  }
}

{
  "intent": "Search for PCT applications filed by a company in the last five years",
  "params": {
    "assignee_name": "OpenAI",
    "country": "WO",
    "start_date": 20200101,
    "end_date": 20251231
  }
}
```
