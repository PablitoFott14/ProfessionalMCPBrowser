## tradingview-mcp_bollinger_scan

### What this tool is used for
Scans for instruments with low Bollinger Band Width to detect volatility squeezes. Use it when identifying coins that are consolidating and may be approaching a breakout, filtered by a maximum BBW threshold.

---

### Used parameters

**(1) exchange: Optional**
Default: KUCOIN
Exchange to scan (e.g., "KUCOIN", "BINANCE", "BYBIT").

**(2) timeframe: Optional**
Default: 4h
Timeframe for the Bollinger Band Width scan.
Allowed: 5m, 15m, 1h, 4h, 1D, 1W, 1M

**(4) bbw_threshold: Optional**
Default: 0.04
Maximum Bollinger Band Width value to include in results. Lower values return only tighter squeezes.

**(3) limit: Optional**
Default: 50
Maximum number of results to return. Maximum allowed: 100.

---

### JSON input alternatives

```json
{
  "intent": "Scan Binance for coins in a volatility squeeze on the 4-hour timeframe",
  "params": {
    "exchange": "BINANCE",
    "timeframe": "4h"
  }
}
```

```json
{
  "intent": "Scan KuCoin for tight squeezes on the daily timeframe with a stricter threshold",
  "params": {
    "exchange": "KUCOIN",
    "timeframe": "1D",
    "bbw_threshold": 0.02,
    "limit": 20
  }
}
```
