## us-legal-mcp_search_congress_bills

### What this tool is for
Searches for bills and resolutions in Congress.gov. Use this when the user needs to find congressional legislation by topic or keyword.

---

### Used parameters

**(1) query — Required**  
Default: No default  
Search query used to find bills or resolutions.

**(2) congress — Optional**  
Default: null  
Congress number used to scope the search.

**(3) limit — Optional**  
Default: 20  
Number of results to return.

---

### JSON input alternatives

```json
{
  "intent": "Search for congressional bills related to immigration",
  "params": {
    "query": "immigration"
  }
}
```

```json
{
  "intent": "Retrieve more infrastructure-related bills from the 118th Congress",
  "params": {
    "query": "infrastructure",
    "congress": 118,
    "limit": 30
  }
}
```
