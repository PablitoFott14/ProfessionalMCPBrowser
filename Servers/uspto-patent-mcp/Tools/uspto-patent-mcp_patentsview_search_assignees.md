## uspto-patent-mcp_patentsview_search_assignees

### What this tool is used for
Searches for assignees with disambiguation. The schema notes that the PatentsView API was shut down on March 20, 2026, and suggests `ppubs_search_patents` with an assignee name query such as `AN/"company name"` as a workaround.

---

### Used parameters

**(29) name - Required**
Default: No default
Assignee or company name to search for.

**(5) limit - Optional**
Default: 100
Maximum number of assignee results to return in this tool. The schema states a maximum of 1000.

---

### JSON input alternatives

```json
{
  "intent": "Search for assignees matching a company name",
  "params": {
    "name": "IBM",
    "limit": 25
  }
}
```

```json
{
  "intent": "Search for assignees matching a longer organization name",
  "params": {
    "name": "International Business Machines",
    "limit": 100
  }
}
```
