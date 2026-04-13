## uspto-patent-mcp_patentsview_get_attorney

### What this tool is used for
Gets detailed attorney information by ID. The schema notes that the PatentsView API was shut down on March 20, 2026, and points users to `odp_get_attorney` with a specific application number to look up attorney information per application.

---

### Used parameters

**(32) attorney_id: Required**
Default: No default
Attorney ID to look up.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve detailed information for an attorney by ID",
  "params": {
    "attorney_id": "att_123456"
  }
}
```

```json
{
  "intent": "Look up another attorney record by ID",
  "params": {
    "attorney_id": "att_789012"
  }
}
```
