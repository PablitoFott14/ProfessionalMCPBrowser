## uspto-patent-mcp_odp_get_assignment

### What this tool is used for
Gets patent assignment and ownership records for an application. Use it when you need current or historical ownership information.

---

### Used parameters

**(10) app_num - Required**
Default: No default
Application number to look up for this assignment request.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve assignment and ownership records for a known application",
  "params": {
    "app_num": "14412875"
  }
}
```

```json
{
  "intent": "Check historical ownership records for another application",
  "params": {
    "app_num": "16987654"
  }
}
```
