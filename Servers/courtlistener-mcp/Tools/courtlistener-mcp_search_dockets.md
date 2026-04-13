## courtlistener-mcp_search_dockets

### What this tool is used for
Searches federal case dockets from PACER via CourtListener. Use it when researching litigation by case name, docket number, party, or court, or when a docket ID is needed for use with other tools.

---

### Used parameters

**(1) q: Required**
Default: No default
Full-text search query for docket text.

**(2) court: Optional**
Default: ""
Filters results to a specific court by court ID (e.g., "scotus", "ca9").

**(3) case_name: Optional**
Default: ""
Filters results by case name.

**(29) docket_number: Optional**
Default: ""
Filters results to a specific docket number.

**(33) date_filed_after: Optional**
Default: ""
Restricts results to dockets filed after this date (YYYY-MM-DD).

**(34) date_filed_before: Optional**
Default: ""
Restricts results to dockets filed before this date (YYYY-MM-DD).

**(32) party_name: Optional**
Default: ""
Filters results by party name.

**(9) order_by: Optional**
Default: score desc
Sort order for results. Accepted values: score desc, dateFiled desc, dateFiled asc.

---

### JSON input alternatives

```json
{
  "intent": "Search for dockets involving a named party in a specific court",
  "params": {
    "q": "patent infringement",
    "court": "dcd",
    "party_name": "Apple",
    "order_by": "dateFiled desc"
  }
}
```

```json
{
  "intent": "Find dockets by case name filed within a date range",
  "params": {
    "q": "securities fraud",
    "case_name": "United States v.",
    "date_filed_after": "2022-01-01",
    "date_filed_before": "2023-12-31"
  }
}
```
