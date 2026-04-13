## open-legal-compliance-mcp_search_case_law

### What this tool is used for
Searches US case law via CourtListener by query string with an optional court filter. Use it when researching legal precedent or locating opinions from a specific court.

---

### Used parameters

**(1) query: Required**
Default: No default
Search query for case law content.

**(3) court: Optional**
Default: No default
Filters results to a specific court by court ID (e.g., "scotus", "ca9").

---

### JSON input alternatives

```json
{
  "intent": "Search case law on a legal topic across all courts",
  "params": {
    "query": "fourth amendment unreasonable search"
  }
}
```

```json
{
  "intent": "Search case law on a topic from a specific court",
  "params": {
    "query": "qualified immunity",
    "court": "ca9"
  }
}
```
