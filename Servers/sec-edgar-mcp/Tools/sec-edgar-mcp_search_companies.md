## sec-edgar-mcp_search_companies

### What this tool is used for
Searches for companies by name.

---

### Used parameters

**(3) query: Required**
Default: No default
Search query used to find matching company names.

**(4) limit: Optional**
Default: 10
Maximum number of matching companies to return.

---

### JSON input alternatives

```json
{
  "intent": "Search for companies matching NVIDIA",
  "params": {
    "query": "NVIDIA"
  }
}
```

```json
{
  "intent": "Search for Apple-related companies and return more matches",
  "params": {
    "query": "Apple",
    "limit": 25
  }
}
```
