## courtlistener-mcp_search_audio

### What this tool is used for
Searches oral argument audio recordings in CourtListener. Use it when researching how a case was argued, finding recordings from a specific court or judge, or filtering arguments by date range.

---

### Used parameters

**(1) q: Required**
Default: No default
Full-text search query for oral argument audio.

**(2) court: Optional**
Default: ""
Filters results to a specific court by court ID (e.g., "scotus", "ca9").

**(3) case_name: Optional**
Default: ""
Filters results by case name.

**(4) judge: Optional**
Default: ""
Filters results by judge name.

**(27) argued_after: Optional**
Default: ""
Restricts results to arguments heard after this date (YYYY-MM-DD).

**(28) argued_before: Optional**
Default: ""
Restricts results to arguments heard before this date (YYYY-MM-DD).

**(9) order_by: Optional**
Default: score desc
Sort order for results. Accepted values: score desc, dateArgued desc, dateArgued asc.

---

### JSON input alternatives

```json
{
  "intent": "Search for oral arguments on a topic from the Supreme Court",
  "params": {
    "q": "affirmative action",
    "court": "scotus",
    "order_by": "dateArgued desc"
  }
}
```

```json
{
  "intent": "Find oral arguments argued within a specific date range",
  "params": {
    "q": "fourth amendment",
    "argued_after": "2020-01-01",
    "argued_before": "2023-12-31",
    "order_by": "dateArgued asc"
  }
}
```
