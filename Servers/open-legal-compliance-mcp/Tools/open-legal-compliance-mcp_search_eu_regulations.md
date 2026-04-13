## open-legal-compliance-mcp_search_eu_regulations

### What this tool is used for
Searches EU Regulations via EUR-Lex by query string or CELEX number with an optional language filter. Use it when researching European Union regulatory requirements or locating a specific EU regulation by its identifier.

---

### Used parameters

**(1) query: Required**
Default: No default
Search query for EU regulation content, or a CELEX number to retrieve a specific regulation directly.

**(4) language: Optional**
Default: en
Language code for the response.

---

### JSON input alternatives

```json
{
  "intent": "Search EU regulations on a compliance topic",
  "params": {
    "query": "data protection personal data processing"
  }
}
```

```json
{
  "intent": "Retrieve a specific EU regulation by CELEX number in a given language",
  "params": {
    "query": "32016R0679",
    "language": "fr"
  }
}
```
