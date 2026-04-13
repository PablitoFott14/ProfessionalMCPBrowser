## uspto-patent-mcp_patentsview_get_assignee

### What this tool is used for
Gets detailed assignee information by disambiguated ID. The schema notes that the PatentsView API was shut down on March 20, 2026, that no direct replacement exists for disambiguated assignee lookups, and that `odp_search_datasets` can be used to find PatentsView bulk datasets.

---

### Used parameters

**(30) assignee_id - Required**
Default: No default
Disambiguated assignee ID to look up.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve detailed information for a disambiguated assignee ID",
  "params": {
    "assignee_id": "org_123456"
  }
}
```

```json
{
  "intent": "Look up another assignee record by disambiguated ID",
  "params": {
    "assignee_id": "org_789012"
  }
}
```
