## courtlistener-mcp_search_opinions

### What this tool is used for
Searches case law opinion clusters with nested Opinion documents in CourtListener. Use it when researching precedent, finding opinions by court or judge, or filtering by citation frequency or date range.

---

### Used parameters

**(1) q: Required**
Default: No default
Full-text search query for opinion content.

**(2) court: Optional**
Default: ""
Filters results to a specific court by court ID (e.g., "scotus", "ca9").

**(3) case_name: Optional**
Default: ""
Filters results by case name.

**(4) judge: Optional**
Default: ""
Filters results by judge name.

**(5) filed_after: Optional**
Default: ""
Restricts results to opinions filed after this date (YYYY-MM-DD).

**(6) filed_before: Optional**
Default: ""
Restricts results to opinions filed before this date (YYYY-MM-DD).

**(7) cited_gt: Optional**
Default: 0
Filters to opinions cited more than this number of times.

**(8) cited_lt: Optional**
Default: 0
Filters to opinions cited fewer than this number of times.

**(9) order_by: Optional**
Default: score desc
Sort order for results. Accepted values: score desc, dateFiled desc, dateFiled asc.

---

### JSON input alternatives

```json
{
  "intent": "Search for opinions on a legal topic from a specific court, sorted by relevance",
  "params": {
    "q": "qualified immunity excessive force",
    "court": "ca9",
    "order_by": "score desc"
  }
}
```

```json
{
  "intent": "Find highly cited opinions on a topic filed within a date range",
  "params": {
    "q": "fourth amendment warrant",
    "filed_after": "2015-01-01",
    "filed_before": "2023-12-31",
    "cited_gt": 50,
    "order_by": "dateFiled desc"
  }
}
```
