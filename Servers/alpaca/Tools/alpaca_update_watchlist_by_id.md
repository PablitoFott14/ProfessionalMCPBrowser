## alpaca_update_watchlist_by_id

### What this tool is for
Updates an existing Alpaca watchlist by its UUID. Allows renaming the watchlist, replacing its symbols, or both. Use this when the user wants to modify the contents or label of a specific watchlist.

---

### Used parameters

**(22) watchlist_id — Required**
Default: No default
UUID of the watchlist to update.

**(21) name — Optional**
Default: null
New name to assign to the watchlist.

**(9) symbols — Optional**
Default: null
New list of ticker symbols to replace the current watchlist contents.

---

### JSON input alternatives

```json
{
  "intent": "Rename a watchlist by its ID",
  "params": {
    "watchlist_id": "e7c5b8a2-1234-4f6d-9abc-8e3f1d2c4500",
    "name": "Momentum Picks"
  }
}
```

```json
{
  "intent": "Replace all symbols in a watchlist with a new set of tickers",
  "params": {
    "watchlist_id": "e7c5b8a2-1234-4f6d-9abc-8e3f1d2c4500",
    "symbols": ["META", "NFLX", "AMZN"]
  }
}
```
