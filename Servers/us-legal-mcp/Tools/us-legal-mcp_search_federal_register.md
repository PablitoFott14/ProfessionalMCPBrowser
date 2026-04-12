## us-legal-mcp_search_federal_register

### What this tool is for
Searches for documents in the Federal Register, including regulations, executive orders, and related federal publications. Use this when the user needs to find federal register documents by topic or keyword.

---

### Used parameters

**(1) query — Required**  
Default: No default  
Search query used to find federal register documents.

**(3) limit — Optional**  
Default: 20  
Number of results to return.

---

### JSON input alternatives

```json
{
  "intent": "Search for Federal Register documents related to environmental policy",
  "params": {
    "query": "environmental"
  }
}
```

```json
{
  "intent": "Retrieve more Federal Register documents related to healthcare",
  "params": {
    "query": "healthcare",
    "limit": 30
  }
}
```
