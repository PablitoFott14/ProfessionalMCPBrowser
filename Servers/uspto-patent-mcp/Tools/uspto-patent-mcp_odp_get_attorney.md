## uspto-patent-mcp_odp_get_attorney

### What this tool is used for
Gets the attorney or agent of record for a patent application. Use it when you need the representative information associated with an application.

---

### Used parameters

**(10) app_num: Required**
Default: No default
Application number to look up for this attorney request.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve the attorney or agent of record for a known application",
  "params": {
    "app_num": "14412875"
  }
}
```

```json
{
  "intent": "Check representative information for another application",
  "params": {
    "app_num": "16987654"
  }
}
```
