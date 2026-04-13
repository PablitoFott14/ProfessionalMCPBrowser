## uspto-patent-mcp_patentsview_search_by_cpc

### What this tool is used for
Searches patents by CPC classification code. The schema notes that the PatentsView API was shut down on March 20, 2026, and suggests `ppubs_search_patents` with a CPC query such as `CPC/"G06N3/08"` as a workaround.

---

### Used parameters

**(1) cpc_code: Required**
Default: No default
CPC code to search for.

**(5) limit: Optional**
Default: 100
Maximum number of patent results to return in this tool. The schema states a maximum of 1000.

---

### JSON input alternatives

```json
{
  "intent": "Search patents for a specific neural network CPC code",
  "params": {
    "cpc_code": "G06N3/08",
    "limit": 25
  }
}
```

```json
{
  "intent": "Search patents for a broader CPC code",
  "params": {
    "cpc_code": "G06N",
    "limit": 100
  }
}
```
