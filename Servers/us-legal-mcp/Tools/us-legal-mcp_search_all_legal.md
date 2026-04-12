## us-legal-mcp_search_all_legal

### What this tool is for
Searches across multiple US legal sources, including Congress, the Federal Register, and court opinions. Use this when the user needs a broader legal search rather than searching a single source in isolation.

---

### Used parameters

**(1) query — Required**  
Default: No default  
Search query used across legal sources.

**(3) limit — Optional**  
Default: 10  
Number of results to return per source.

---

### JSON input alternatives

```json
{
  "intent": "Search across US legal sources for immigration-related material",
  "params": {
    "query": "immigration"
  }
}
```

```json
{
  "intent": "Retrieve more cross-source legal results related to healthcare",
  "params": {
    "query": "healthcare",
    "limit": 25
  }
}
```
