## uspto-patent-mcp_patentsview_get_description

### What this tool is used for
Gets patent detailed description text. The schema notes that the PatentsView API was shut down on March 20, 2026, and points users to `ppubs_get_full_document` to retrieve the full patent specification.

---

### Used parameters

**(28) patent_id - Required**
Default: No default
Patent ID or number to look up.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve the detailed description text for a known patent",
  "params": {
    "patent_id": "7861317"
  }
}
```

```json
{
  "intent": "Look up specification text for another patent by PatentsView patent ID",
  "params": {
    "patent_id": "10000000"
  }
}
```
