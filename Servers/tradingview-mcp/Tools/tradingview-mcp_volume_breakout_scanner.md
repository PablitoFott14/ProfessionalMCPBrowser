## tradingview-mcp_volume_breakout_scanner

### What this tool is used for
Detects instruments showing simultaneous volume and price breakouts on a given exchange and timeframe. Use it when scanning for coins where an abnormal volume spike accompanies a significant price move, indicating a potential high-conviction breakout.

---

### Used parameters

**(1) exchange: Optional**
Default: KUCOIN
Exchange to scan (e.g., "KUCOIN", "BINANCE", "BYBIT").

**(2) timeframe: Optional**
Default: 15m
Timeframe for the breakout scan.
Allowed: 5m, 15m, 1h, 4h, 1D, 1W, 1M

**(13) volume_multiplier: Optional**
Default: 2
Minimum multiple by which current volume must exceed the normal level to qualify.

**(14) price_change_min: Optional**
Default: 3
Minimum price change percentage required for a result to be included.

**(3) limit: Optional**
Default: 25
Maximum number of results to return. Maximum allowed: 50 for this tool.

---

### JSON input alternatives

```json
{
  "intent": "Scan Binance for volume and price breakouts on the 1-hour timeframe",
  "params": {
    "exchange": "BINANCE",
    "timeframe": "1h"
  }
}
```

```json
{
  "intent": "Scan for high-conviction breakouts with stricter volume and price thresholds",
  "params": {
    "exchange": "BYBIT",
    "timeframe": "4h",
    "volume_multiplier": 3,
    "price_change_min": 5,
    "limit": 15
  }
}
```
