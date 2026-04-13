## uspto-patent-mcp_ptab_get_appeal

### What this tool is used for
Gets details of a specific ex parte appeal decision. Use it when you already know the appeal number and need the appeal record.

---

### Used parameters

**(26) appeal_number: Required**
Default: No default
Appeal number to look up.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve details for a known ex parte appeal",
  "params": {
    "appeal_number": "2023-006789"
  }
}
```

```json
{
  "intent": "Look up another ex parte appeal by appeal number",
  "params": {
    "appeal_number": "2024-001234"
  }
}
```
