## uspto-patent-mcp_patentsview_get_patent

### What this tool is used for
Gets detailed patent information from PatentsView. The schema notes that the PatentsView API was shut down on March 20, 2026, and points users to `ppubs_get_patent_by_number` for patent details.

---

### Used parameters

**(28) patent_id: Required**
Default: No default
Patent ID or number to look up.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve detailed information for a known patent by PatentsView patent ID",
  "params": {
    "patent_id": "7861317"
  }
}
```

```json
{
  "intent": "Look up another patent record by PatentsView patent ID",
  "params": {
    "patent_id": "10000000"
  }
}
```
