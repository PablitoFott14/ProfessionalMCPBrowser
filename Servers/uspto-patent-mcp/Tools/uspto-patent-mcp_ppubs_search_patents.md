## uspto-patent-mcp_ppubs_search_patents

### What this tool is used for
Searches granted US patents in USPTO Patent Public Search (ppubs.uspto.gov) using full-text USPTO query syntax. Returns normalized results including GUID, title, abstract, dates, inventors, and classification codes. Use when full-text search with daily-updated data is needed, or when the most recent patent filings must be included — PPUBS updates daily versus the periodic update cycle of PatentsView.

---

### Used parameters

**(3) query — Required**
Default: No default
Search query using USPTO syntax. Supports field codes (e.g., TTL/ for title, IN/ for inventor, AN/ for assignee, CPC/ for classification), phrase search with quotes, and boolean operators (AND, OR). Example: `TTL/"neural network" AND CPC/G06N3/08`.

**(4) offset — Optional**
Default: 0
Starting position for pagination through granted-patent results.

**(5) limit — Optional**
Default: 100
Maximum number of granted-patent results to return. Maximum allowed value is 500.

**(6) sort — Optional**
Default: date_publ desc
Sort order for granted-patent results.

---

### JSON input alternatives

```json
{
  "intent": "Search granted patents with neural network in the title",
  "params": {
    "query": "TTL/\"neural network\"",
    "limit": 50
  }
}
```

```json
{
  "intent": "Find granted patents by inventor Smith at IBM in the G06N CPC class",
  "params": {
    "query": "IN/Smith AND AN/IBM AND CPC/G06N",
    "offset": 25,
    "limit": 25
  }
}
```
