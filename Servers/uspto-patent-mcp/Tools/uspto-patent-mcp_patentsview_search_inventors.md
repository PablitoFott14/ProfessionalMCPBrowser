## uspto-patent-mcp_patentsview_search_inventors

### What this tool is used for
Searches for inventors with disambiguation. The schema notes that the PatentsView API was shut down on March 20, 2026, and suggests `ppubs_search_patents` with an inventor name query such as `IN/"last name"` as a workaround.

---

### Used parameters

**(29) name - Required**
Default: No default
Inventor name to search for.

**(5) limit - Optional**
Default: 100
Maximum number of inventor results to return in this tool. The schema states a maximum of 1000.

---

### JSON input alternatives

```json
{
  "intent": "Search for inventors by last name",
  "params": {
    "name": "Smith",
    "limit": 25
  }
}
```

```json
{
  "intent": "Search for inventors by full name",
  "params": {
    "name": "John Smith",
    "limit": 100
  }
}
```
