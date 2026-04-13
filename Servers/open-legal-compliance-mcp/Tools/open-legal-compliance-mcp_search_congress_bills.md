## open-legal-compliance-mcp_search_congress_bills

### What this tool is used for
Searches US Congress bills by query string with an optional congress number filter. Use it when researching pending or enacted legislation or tracking bills relevant to a compliance topic.

---

### Used parameters

**(1) query: Required**
Default: No default
Search query for congressional bill content.

**(6) congress: Optional**
Default: No default
Filters results to a specific Congress number (e.g., 118).

---

### JSON input alternatives

```json
{
  "intent": "Search congressional bills on a legislative topic",
  "params": {
    "query": "artificial intelligence regulation"
  }
}
```

```json
{
  "intent": "Search bills from a specific Congress on a topic",
  "params": {
    "query": "data privacy",
    "congress": 118
  }
}
```
