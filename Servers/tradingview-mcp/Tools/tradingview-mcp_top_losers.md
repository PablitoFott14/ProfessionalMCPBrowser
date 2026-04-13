## tradingview-mcp_top_losers

### What this tool is used for
Returns the top losing instruments for a given exchange and timeframe using Bollinger Band analysis. Use it when scanning for the weakest or most oversold instruments on a specific exchange across different timeframes.

---

### Used parameters

**(1) exchange: Optional**
Default: KUCOIN
Exchange to scan for top losers (e.g., "KUCOIN", "BINANCE", "BYBIT").

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
  "intent": "Get top losers on Binance over a 4-hour timeframe",
  "params": {
    "exchange": "BINANCE",
    "timeframe": "4h"
  }
}
```

```json
{
  "intent": "Get the top 10 losers on KuCoin over a weekly timeframe",
  "params": {
    "exchange": "KUCOIN",
    "timeframe": "1W",
    "limit": 10
  }
}
```
