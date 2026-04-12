## us-regulations-mcp_search_regulations

### What this tool is for
Searches across supported US federal and state regulations to find relevant regulation text on a topic. Use this as the primary discovery tool when the user needs to locate regulation sections before moving to a specific provision.

---

### Used parameters

**(1) query - Required**  
Default: No default  
Search query used to find relevant regulation text.

**(2) regulations - Optional**  
Default: null  
List of regulation identifiers used to limit the search scope.

**(3) limit - Optional**  
Default: 10  
Maximum number of results to return.

**(4) offset - Optional**  
Default: 0  
Number of results to skip for pagination.

---

### JSON input alternatives

```json
{
  "tool": "us-regulations-mcp_search_regulations",
  "intent": "Search regulations for breach notification requirements",
  "params": {
    "query": "breach notification requirements"
  }
}
```

```json
{
  "tool": "us-regulations-mcp_search_regulations",
  "intent": "Search HIPAA and CCPA regulation text related to safeguards with pagination",
  "params": {
    "query": "safeguards",
    "regulations": ["HIPAA", "CCPA"],
    "limit": 25,
    "offset": 25
  }
}
```
