## us-legal-mcp_search_court_opinions

### What this tool is for
Court opinions and decisions from CourtListener across federal and state courts. Use this when the user needs case law results rather than legislative or regulatory materials.

---

### Used parameters

**(1) query - Required**  
Default: No default  
Search query used to find relevant court opinions.

**(4) court - Optional**  
Default: null  
Court identifier used to limit the search to a specific court.

**(3) limit - Optional**  
Default: 20  
Number of court opinion results to return.

---

### JSON input alternatives

```json
{
  "tool": "us-legal-mcp_search_court_opinions",
  "intent": "Search court opinions related to copyright disputes",
  "params": {
    "query": "copyright"
  }
}
```

```json
{
  "tool": "us-legal-mcp_search_court_opinions",
  "intent": "Search Supreme Court opinions related to constitutional issues",
  "params": {
    "query": "constitutional",
    "court": "scotus",
    "limit": 15
  }
}
```
