## tradingview-mcp_rating_filter

### What this tool is used for
Filters instruments by their Bollinger Band rating on a given exchange and timeframe. Use it when scanning for coins that meet a specific signal strength, from strong sell to strong buy.

---

### Used parameters

**(1) exchange: Optional**
Default: KUCOIN
Exchange to scan (e.g., "KUCOIN", "BINANCE", "BYBIT").

**(2) timeframe: Optional**
Default: 5m
Timeframe for the Bollinger Band rating.
Allowed: 5m, 15m, 1h, 4h, 1D, 1W, 1M

**(5) rating: Optional**
Default: 2
Bollinger Band rating to filter by. Range: -3 to +3.
-3 = Strong Sell, -2 = Sell, -1 = Weak Sell, 1 = Weak Buy, 2 = Buy, 3 = Strong Buy.

**(3) limit: Optional**
Default: 25
Maximum number of results to return. Maximum allowed: 50 for this tool.

---

### JSON input alternatives

```json
{
  "intent": "Find strong buy signals on Binance on the 1-hour timeframe",
  "params": {
    "exchange": "BINANCE",
    "timeframe": "1h",
    "rating": 3
  }
}
```

```json
{
  "intent": "Find sell signals on KuCoin on the daily timeframe",
  "params": {
    "exchange": "KUCOIN",
    "timeframe": "1D",
    "rating": -2,
    "limit": 20
  }
}
```
