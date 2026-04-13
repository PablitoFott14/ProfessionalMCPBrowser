## uspto-patent-mcp_odp_get_application_metadata

### What this tool is used for
Gets detailed metadata for a patent application. Use it when you need comprehensive application metadata including examiner information, art unit, and detailed status.

---

### Used parameters

**(10) app_num - Required**
Default: No default
Application number to look up for this metadata request.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve detailed metadata for a known patent application",
  "params": {
    "app_num": "14412875"
  }
}
```

```json
{
  "intent": "Check examiner and art unit details for another application",
  "params": {
    "app_num": "16987654"
  }
}
```
