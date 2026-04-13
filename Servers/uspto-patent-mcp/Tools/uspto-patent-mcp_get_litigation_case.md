## uspto-patent-mcp_get_litigation_case

### What this tool is used for
Gets details of a specific litigation case. Use it when you already know the case identifier and need the case record.

---

### Used parameters

**(47) case_id - Required**
Default: No default
Case identifier to look up.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve details for a known litigation case",
  "params": {
    "case_id": "CASE-2024-0001"
  }
}
```

```json
{
  "intent": "Look up another litigation case by identifier",
  "params": {
    "case_id": "CASE-2023-0456"
  }
}
```
