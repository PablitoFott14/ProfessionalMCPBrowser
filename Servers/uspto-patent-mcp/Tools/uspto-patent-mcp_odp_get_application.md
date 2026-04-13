## uspto-patent-mcp_odp_get_application

### What this tool is used for
Gets patent application data from the USPTO Open Data Portal. Use it when you need application-level prosecution data including status, dates, and basic metadata.

---

### Used parameters

**(10) app_num - Required**
Default: No default
Application number to look up for this Open Data Portal request.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve application data for a known patent application number",
  "params": {
    "app_num": "14412875"
  }
}
```

```json
{
  "intent": "Check prosecution data and status for another patent application",
  "params": {
    "app_num": "16987654"
  }
}
```
