## uspto-patent-mcp_patentsview_search_attorneys

### What this tool is used for
Searches for patent attorneys or agents. The schema notes that the PatentsView API was shut down on March 20, 2026, and points users to `odp_get_attorney` with a specific application number to look up attorney information per application.

---

### Used parameters

**(29) name: Required**
Default: No default
Attorney, agent, or firm name to search for.

**(5) limit: Optional**
Default: 100
Maximum number of attorney results to return in this tool. The schema states a maximum of 1000.

---

### JSON input alternatives

```json
{
  "intent": "Search for patent attorneys by last name",
  "params": {
    "name": "Smith",
    "limit": 25
  }
}
```

```json
{
  "intent": "Search for a patent law firm by name",
  "params": {
    "name": "Wilson Sonsini",
    "limit": 100
  }
}
```
