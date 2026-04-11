## alpaca_get_watchlist_by_id

### What this tool is for
Retrieves the details of a specific Alpaca watchlist by its UUID, including its name, ID, timestamps, and the symbols it contains. Use this when the user wants to inspect a particular watchlist after retrieving its ID from `get_watchlists`.

---

### Used parameters

**(22) watchlist_id — Required**
Default: No default
UUID of the watchlist to retrieve.

---

### JSON input alternatives

```json
{
  "intent": "Get the full details and symbol list of a specific watchlist",
  "params": {
    "watchlist_id": "e7c5b8a2-1234-4f6d-9abc-8e3f1d2c4500"
  }
}
```
