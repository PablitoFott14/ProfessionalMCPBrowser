## uspto-patent-mcp_patentsview_search_patents

### What this tool is used for
Searches US patents with PatentsView full-text search. The schema notes that the PatentsView API was shut down on March 20, 2026, and points users to `ppubs_search_patents` for full-text patent search and `odp_search_datasets` for PatentsView bulk datasets on the USPTO Open Data Portal.

---

### Used parameters

**(3) query: Required**
Default: No default
Search terms for patent titles and abstracts.

**(27) search_type: Optional**
Default: any
Controls the match type for this search.
Allowed: any, all, phrase

**(4) offset: Optional**
Default: 0
Starting position for pagination in this PatentsView search.

**(5) limit: Optional**
Default: 100
Maximum number of patent results to return in this tool. The schema states a maximum of 1000.

---

### JSON input alternatives

```json
{
  "intent": "Search patents by title and abstract terms using phrase matching",
  "params": {
    "query": "neural network accelerator",
    "search_type": "phrase",
    "limit": 25
  }
}
```

```json
{
  "intent": "Search patents using all terms and continue to a later page",
  "params": {
    "query": "battery thermal management",
    "search_type": "all",
    "offset": 100,
    "limit": 100
  }
}
```
