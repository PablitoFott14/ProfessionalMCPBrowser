## open-legal-compliance-mcp_search_fda_events

### What this tool is used for
Searches FDA adverse events or food enforcement records by type and query string. Use it when researching drug or device adverse event reports, or food enforcement actions from the FDA.

---

### Used parameters

**(11) type: Required**
Default: No default
Category of FDA data to search.
Allowed: drug, device, food

**(1) query: Required**
Default: No default
Search query for FDA event or enforcement content.

---

### JSON input alternatives

```json
{
  "intent": "Search FDA adverse event reports for a specific drug",
  "params": {
    "type": "drug",
    "query": "ibuprofen gastrointestinal bleeding"
  }
}
```

```json
{
  "intent": "Search FDA food enforcement actions for a product",
  "params": {
    "type": "food",
    "query": "listeria contamination recall"
  }
}
```
