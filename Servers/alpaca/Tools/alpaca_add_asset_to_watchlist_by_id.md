## alpaca_add_asset_to_watchlist_by_id

### What this tool is for
Adds a single asset to an existing Alpaca watchlist identified by its UUID. Use this when the user wants to append one symbol to a watchlist without replacing its existing contents.

---

### Used parameters

**(22) watchlist_id — Required**
Default: No default
UUID of the watchlist to add the asset to.

**(1) symbol — Required**
Default: No default
Ticker symbol of the asset to add (e.g., AAPL, TSLA).

---

### JSON input alternatives

```json
{
  "intent": "Add Nvidia to an existing watchlist",
  "params": {
    "watchlist_id": "e7c5b8a2-1234-4f6d-9abc-8e3f1d2c4500",
    "symbol": "NVDA"
  }
}
```
