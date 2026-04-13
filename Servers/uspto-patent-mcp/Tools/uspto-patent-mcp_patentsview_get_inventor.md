## uspto-patent-mcp_patentsview_get_inventor

### What this tool is used for
Gets detailed inventor information by disambiguated ID. The schema notes that the PatentsView API was shut down on March 20, 2026, that no direct replacement exists for disambiguated inventor lookups, and that `odp_search_datasets` can be used to find PatentsView bulk datasets.

---

### Used parameters

**(31) inventor_id - Required**
Default: No default
Disambiguated inventor ID to look up.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve detailed information for a disambiguated inventor ID",
  "params": {
    "inventor_id": "inv_123456"
  }
}
```

```json
{
  "intent": "Look up another inventor record by disambiguated ID",
  "params": {
    "inventor_id": "inv_789012"
  }
}
```
