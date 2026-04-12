## fred-mcp-server_fred_browse

### What this tool is for
Browses the FRED catalog through categories, releases, sources, or series collections. Use this when the user needs to explore the overall FRED structure rather than search directly by keywords or series ID.

---

### Used parameters

**(19) browse_type - Required**  
Default: No default  
Browse mode used to determine what part of the FRED catalog to explore.

**(20) category_id - Optional**  
Default: No default  
Category identifier used for category-based browsing.

**(21) release_id - Optional**  
Default: No default  
Release identifier used for release-based browsing.

**(5) limit - Optional**  
Default: 50  
Maximum number of results to return.

**(6) offset - Optional**  
Default: 0  
Number of results to skip.

**(7) order_by - Optional**  
Default: No default  
Field used to order the results.

**(8) sort_order - Optional**  
Default: No default  
Sort direction used for ordered results.

---

### JSON input alternatives

```json
{
  "tool": "fred-mcp-server_fred_browse",
  "intent": "Browse the top-level FRED categories",
  "params": {
    "browse_type": "categories"
  }
}
```

```json
{
  "tool": "fred-mcp-server_fred_browse",
  "intent": "Retrieve series in a specific FRED category",
  "params": {
    "browse_type": "category_series",
    "category_id": 125,
    "limit": 25
  }
}
```
