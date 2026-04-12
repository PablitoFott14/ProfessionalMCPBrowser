## alpaca_remove_asset_from_watchlist_by_id

### What this tool is for
Removes a single asset from an existing Alpaca watchlist identified by its UUID. Use this when the user wants to delete one symbol from a watchlist without affecting the rest of its contents.

---

### Used parameters

**(22) watchlist_id — Required**
Default: No default
UUID of the watchlist to remove the asset from.

**(1) symbol — Required**
Default: No default
Ticker symbol of the asset to remove (e.g., AAPL, TSLA).

---

### JSON input alternatives

```json
{
  "tool": "alpaca_remove_asset_from_watchlist_by_id",
  "intent": "Remove Tesla from an existing watchlist",
  "params": {
    "watchlist_id": "e7c5b8a2-1234-4f6d-9abc-8e3f1d2c4500",
    "symbol": "TSLA"
  }
}
```
