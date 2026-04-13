## uspto-patent-mcp_odp_get_foreign_priority

### What this tool is used for
Gets foreign priority claims for a patent application. Use it when you need to identify priority claims to foreign applications that may affect the effective filing date.

---

### Used parameters

**(10) app_num - Required**
Default: No default
Application number to look up for this foreign priority request.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve foreign priority claims for a known application",
  "params": {
    "app_num": "14412875"
  }
}
```

```json
{
  "intent": "Check foreign priority claims for another application",
  "params": {
    "app_num": "16987654"
  }
}
```
