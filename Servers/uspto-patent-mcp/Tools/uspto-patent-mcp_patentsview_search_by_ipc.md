## uspto-patent-mcp_patentsview_search_by_ipc

### What this tool is used for
Searches patents by IPC classification code. The schema notes that the PatentsView API was shut down on March 20, 2026, and suggests using `ppubs_search_patents` with an IPC query as a workaround.

---

### Used parameters

**(33) ipc_code: Required**
Default: No default
IPC code to search for.

**(5) limit: Optional**
Default: 100
Maximum number of patent results to return in this tool. The schema states a maximum of 1000.

---

### JSON input alternatives

```json
{
  "intent": "Search patents for a specific IPC code",
  "params": {
    "ipc_code": "G06F",
    "limit": 25
  }
}
```

```json
{
  "intent": "Search patents for another IPC classification code",
  "params": {
    "ipc_code": "H04L",
    "limit": 100
  }
}
```
