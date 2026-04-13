## alpaca_delete_watchlist_by_id

### What this tool is for
Deletes a specific Alpaca watchlist by its UUID. Use this when the user wants to remove a watchlist entirely from the account.

---

### Used parameters

**(22) watchlist_id — Required**
Default: No default
UUID of the watchlist to delete.

---

### JSON input alternatives

```json
{
  "tool": "alpaca_delete_watchlist_by_id",
  "intent": "Delete a watchlist that is no longer needed",
  "params": {
    "watchlist_id": "e7c5b8a2-1234-4f6d-9abc-8e3f1d2c4500"
  }
}
```
