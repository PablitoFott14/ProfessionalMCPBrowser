## open-legal-compliance-mcp_search_canlii_cases

### What this tool is used for
Searches Canadian case law via CanLII by query string with an optional database filter. Use it when researching Canadian legal precedent or locating decisions from a specific court or tribunal database.

---

### Used parameters

**(1) query: Required**
Default: No default
Search query for Canadian case law content.

**(10) databaseId: Optional**
Default: csc-scc
CanLII database identifier to restrict the search to a specific court or tribunal.

---

### JSON input alternatives

```json
{
  "intent": "Search Canadian case law on a legal topic using the default Supreme Court database",
  "params": {
    "query": "reasonable expectation of privacy"
  }
}
```

```json
{
  "intent": "Search a specific CanLII database for cases on a topic",
  "params": {
    "query": "wrongful dismissal",
    "databaseId": "onca"
  }
}
```
