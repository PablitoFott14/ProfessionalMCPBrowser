## uspto-patent-mcp_ptab_get_decision

### What this tool is used for
Gets details of a specific PTAB decision. Use it when you already know the decision identifier and need the decision record.

---

### Used parameters

**(25) decision_id - Required**
Default: No default
Decision identifier to look up.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve details for a known PTAB decision",
  "params": {
    "decision_id": "DEC-2024-00001"
  }
}
```

```json
{
  "intent": "Look up another PTAB decision by identifier",
  "params": {
    "decision_id": "DEC-2023-01542"
  }
}
```
