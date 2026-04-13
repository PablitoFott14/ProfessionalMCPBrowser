## uspto-patent-mcp_odp_get_transactions

### What this tool is used for
Gets prosecution transaction history for a patent application. Use it when you need the timeline of prosecution events, including office actions, responses, and fee payments.

---

### Used parameters

**(10) app_num: Required**
Default: No default
Application number to look up for this transaction-history request.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve prosecution transaction history for a known application",
  "params": {
    "app_num": "14412875"
  }
}
```

```json
{
  "intent": "Check the prosecution timeline for another application",
  "params": {
    "app_num": "16987654"
  }
}
```
