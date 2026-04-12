## us-legal-mcp_get_recent_bills

### What this tool is for
Gets the most recently introduced bills in Congress. Use this when the user needs a current view of recently introduced congressional legislation rather than a keyword search.

---

### Used parameters

**(2) congress — Optional**  
Default: null  
Congress number used to scope the results.

**(3) limit — Optional**  
Default: 20  
Number of results to return.

---

### JSON input alternatives

```json
{
  "tool": "us-legal-mcp_get_recent_bills",
  "intent": "Get the most recent bills introduced in Congress",
  "params": {}
}
```

```json
{
  "tool": "us-legal-mcp_get_recent_bills",
  "intent": "Retrieve more recently introduced bills from the 118th Congress",
  "params": {
    "congress": 118,
    "limit": 30
  }
}
```
