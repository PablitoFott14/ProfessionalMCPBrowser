## massive-mcp_search_endpoints

### What this tool is for
Searches for financial market data API endpoints and local finance functions by natural language query. Use this as the starting point when the user needs to discover where to get specific market data or which finance functions are available for a given task.

---

### Used parameters

**(1) query - Required**  
Default: No default  
Natural language search query used to find relevant endpoints or functions.

**(2) scope - Optional**  
Default: null  
Allowed: endpoints, functions  
Search scope used to limit results to endpoints or functions (null for both).

---

### JSON input alternatives

```json
{
  "tool": "massive-mcp_search_endpoints",
  "intent": "Find endpoints related to options data",
  "params": {
    "query": "options data"
  }
}
```

```json
{
  "tool": "massive-mcp_search_endpoints",
  "intent": "Search only local functions related to technical indicators",
  "params": {
    "query": "technical indicators",
    "scope": "functions"
  }
}
```
