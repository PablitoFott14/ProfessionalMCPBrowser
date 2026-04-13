## alpaca_cancel_order_by_id

### What this tool is for
A specific open order by its UUID. Use this when the user wants to cancel a single order without affecting other open orders on the account.

---

### Used parameters

**(62) order_id — Required**
Default: No default
UUID of the order to cancel.

---

### JSON input alternatives

```json
{
  "intent": "Cancel a specific order by its ID",
  "params": {
    "order_id": "a3f1c2e4-5678-4b9d-8abc-123456789def"
  }
}
```
