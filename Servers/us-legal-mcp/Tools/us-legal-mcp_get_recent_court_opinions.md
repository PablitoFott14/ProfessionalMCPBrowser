## us-legal-mcp_get_recent_court_opinions

### What this tool is for
The most recently published court opinions from CourtListener. Use this when the user needs a current view of new court opinions rather than a keyword-based case law search.

---

### Used parameters

**(4) court - Optional**  
Default: null  
Court identifier used to limit results to a specific court.

**(3) limit - Optional**  
Default: 20  
Number of results to return.

---

### JSON input alternatives

```json
{
  "tool": "us-legal-mcp_get_recent_court_opinions",
  "intent": "Get the most recently published court opinions",
  "params": {}
}
```

```json
{
  "tool": "us-legal-mcp_get_recent_court_opinions",
  "intent": "Retrieve recent Supreme Court opinions",
  "params": {
    "court": "scotus",
    "limit": 15
  }
}
```
