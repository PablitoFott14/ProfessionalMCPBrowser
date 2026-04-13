## uspto-patent-mcp_odp_get_continuity

### What this tool is used for
Gets patent family and continuity data for an application. Use it when you need to understand parent and child application relationships, including continuations, divisionals, and continuations-in-part.

---

### Used parameters

**(10) app_num - Required**
Default: No default
Application number to look up for this continuity request.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve patent family continuity data for a known application",
  "params": {
    "app_num": "14412875"
  }
}
```

```json
{
  "intent": "Check parent and child application relationships for another application",
  "params": {
    "app_num": "16987654"
  }
}
```
