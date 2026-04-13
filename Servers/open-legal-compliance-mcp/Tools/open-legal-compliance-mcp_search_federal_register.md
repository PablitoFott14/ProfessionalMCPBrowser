## open-legal-compliance-mcp_search_federal_register

### What this tool is used for
Searches Federal Register documents by query string with an optional result count. Use it when researching proposed or final rules, agency notices, and other regulatory actions published in the Federal Register.

---

### Used parameters

**(1) query: Required**
Default: No default
Search query for Federal Register document content.

**(7) perPage: Optional**
Default: No default
Number of results to return per page.

---

### JSON input alternatives

```json
{
  "intent": "Search the Federal Register for documents on a regulatory topic",
  "params": {
    "query": "financial institution reporting requirements"
  }
}
```

```json
{
  "intent": "Search the Federal Register with a limited result count",
  "params": {
    "query": "workplace safety standards",
    "perPage": 10
  }
}
```
