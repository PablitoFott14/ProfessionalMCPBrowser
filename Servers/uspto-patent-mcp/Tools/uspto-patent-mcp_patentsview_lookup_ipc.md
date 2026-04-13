## uspto-patent-mcp_patentsview_lookup_ipc

### What this tool is used for
Looks up IPC classification code details. The schema notes that the PatentsView API was shut down on March 20, 2026, that no direct replacement exists for IPC lookups, and that `odp_search_datasets` can be used to find PatentsView bulk datasets containing IPC data.

---

### Used parameters

**(33) ipc_code - Required**
Default: No default
IPC code to look up.

---

### JSON input alternatives

```json
{
  "intent": "Look up details for an IPC code",
  "params": {
    "ipc_code": "G06F"
  }
}
```

```json
{
  "intent": "Look up details for another IPC classification code",
  "params": {
    "ipc_code": "H04L"
  }
}
```
