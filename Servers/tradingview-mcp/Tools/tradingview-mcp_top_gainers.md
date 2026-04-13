## tradingview-mcp_top_gainers

### What this tool is used for
Returns the top gaining instruments for a given exchange and timeframe using Bollinger Band analysis. Use it when scanning for the strongest upside movers on a specific exchange across different timeframes.

---

### Used parameters

**(1) exchange: Optional**
Default: KUCOIN
Exchange to scan for top gainers (e.g., "KUCOIN", "BINANCE", "BYBIT").

**(2) timeframe: Optional**
Default: 15m
Timeframe for the Bollinger Band analysis.
Allowed: 5m, 15m, 1h, 4h, 1D, 1W, 1M

**(3) limit: Optional**
Default: 25
Maximum number of results to return. Maximum allowed: 50 for this tool.

---

### JSON input alternatives

```json
{
  "intent": "Get top gainers on Binance over a 1-hour timeframe",
  "params": {
    "exchange": "BINANCE",
    "timeframe": "1h"
  }
}
```

```json
{
  "intent": "Get the top 10 gainers on Bybit over a daily timeframe",
  "params": {
    "exchange": "BYBIT",
    "timeframe": "1D",
    "limit": 10
  }
}
```
