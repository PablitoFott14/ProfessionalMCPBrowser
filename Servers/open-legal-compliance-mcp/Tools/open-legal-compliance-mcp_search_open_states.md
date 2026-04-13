## open-legal-compliance-mcp_search_open_states

### What this tool is used for
Searches state legislation across all 50 states via OpenStates with an optional jurisdiction filter. Use it when researching bills or legislative activity in any US state, not limited to the three states supported by the dedicated state law search.

---

### Used parameters

**(1) query: Required**
Default: No default
Search query for state legislation content.

**(9) jurisdiction: Optional**
Default: No default
Filters results to a specific state by abbreviation (e.g., "ca").

---

### JSON input alternatives

```json
{
  "intent": "Search state legislation on a topic across all states",
  "params": {
    "query": "minimum wage increase"
  }
}
```

```json
{
  "intent": "Search legislation in a specific state on a topic",
  "params": {
    "query": "electric vehicle incentives",
    "jurisdiction": "ca"
  }
}
```
