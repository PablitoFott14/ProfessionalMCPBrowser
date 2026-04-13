## alpaca_create_watchlist

### What this tool is for
A new watchlist on Alpaca with a given name and a list of symbols. Use this when the user wants to group a set of instruments for ongoing monitoring without placing trades.

---

### Used parameters

**(21) name: Required**
Default: No default
Name to assign to the new watchlist.

**(9) symbols: Required**
Default: No default
List of ticker symbols to include in the watchlist.

---

### JSON input alternatives

```json
{
  "intent": "Create a watchlist of tech stocks to monitor",
  "params": {
    "name": "Tech Watchlist",
    "symbols": ["AAPL", "MSFT", "NVDA", "GOOGL"]
  }
}
```

```json
{
  "intent": "Set up a watchlist for energy sector stocks",
  "params": {
    "name": "Energy Sector",
    "symbols": ["XOM", "CVX", "SLB", "COP"]
  }
}
```
