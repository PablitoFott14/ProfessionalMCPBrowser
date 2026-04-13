## uspto-patent-mcp_odp_search_applications

### What this tool is used for
Searches patent applications in the USPTO Open Data Portal. Use it when you need application search filters based on applicant metadata, filing dates, or related identifiers.

---

### Used parameters

**(3) query - Optional**
Default: null
General search query string for this Open Data Portal application search.

**(11) application_number - Optional**
Default: null
Filters results by application number.

**(9) patent_number - Optional**
Default: null
Filters results by patent number.

**(12) inventor_name - Optional**
Default: null
Filters results by inventor name.

**(13) assignee_name - Optional**
Default: null
Filters results by assignee or applicant name.

**(14) filing_date_from - Optional**
Default: null
Sets the filing date range start for this search.

**(15) filing_date_to - Optional**
Default: null
Sets the filing date range end for this search.

**(4) offset - Optional**
Default: 0
Starting position for pagination in this Open Data Portal search.

**(5) limit - Optional**
Default: 25
Maximum number of application results to return in this tool.

---

### JSON input alternatives

```json
{
  "intent": "Search for applications by inventor name within a filing date range",
  "params": {
    "inventor_name": "Smith",
    "filing_date_from": "2020-01-01",
    "filing_date_to": "2020-12-31",
    "limit": 10
  }
}
```

```json
{
  "intent": "Search for applications for a specific assignee and continue to a later page",
  "params": {
    "assignee_name": "IBM",
    "offset": 25,
    "limit": 25
  }
}
```
