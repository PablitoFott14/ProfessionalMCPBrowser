## uspto-patent-mcp_odp_search_datasets

### What this tool is used for
Searches USPTO bulk data products and datasets. Use it when you need to find bulk download datasets for large-scale analysis.

---

### Used parameters

**(3) query - Optional**
Default: null
Search query for dataset names or descriptions.

**(4) offset - Optional**
Default: 0
Starting position for pagination in this dataset search.

**(5) limit - Optional**
Default: 25
Maximum number of dataset results to return in this tool.

---

### JSON input alternatives

```json
{
  "intent": "Search for USPTO bulk datasets related to patent assignments",
  "params": {
    "query": "assignment",
    "limit": 10
  }
}
```

```json
{
  "intent": "Continue browsing bulk datasets related to prosecution data",
  "params": {
    "query": "prosecution",
    "offset": 25,
    "limit": 25
  }
}
```
