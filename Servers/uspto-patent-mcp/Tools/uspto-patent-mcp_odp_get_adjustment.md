## uspto-patent-mcp_odp_get_adjustment

### What this tool is used for
Gets patent term adjustment data for an application. Use it when you need to calculate the actual expiration timing of a patent while accounting for USPTO delays.

---

### Used parameters

**(10) app_num: Required**
Default: No default
Application number to look up for this patent term adjustment request.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve patent term adjustment data for a known application",
  "params": {
    "app_num": "14412875"
  }
}
```

```json
{
  "intent": "Check USPTO delay adjustment data for another application",
  "params": {
    "app_num": "16987654"
  }
}
```
