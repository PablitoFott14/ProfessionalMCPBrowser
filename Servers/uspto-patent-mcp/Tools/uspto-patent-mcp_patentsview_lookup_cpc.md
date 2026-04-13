## uspto-patent-mcp_patentsview_lookup_cpc

### What this tool is used for
Looks up CPC classification code details. The schema notes that the PatentsView API was shut down on March 20, 2026, and points users to `get_cpc_info` for CPC code descriptions.

---

### Used parameters

**(1) cpc_code - Required**
Default: No default
CPC code to look up.

---

### JSON input alternatives

```json
{
  "intent": "Look up details for a CPC class code",
  "params": {
    "cpc_code": "G06"
  }
}
```

```json
{
  "intent": "Look up details for a more specific CPC group code",
  "params": {
    "cpc_code": "G06N3/08"
  }
}
```
