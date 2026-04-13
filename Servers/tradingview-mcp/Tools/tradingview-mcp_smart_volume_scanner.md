## tradingview-mcp_smart_volume_scanner

### What this tool is used for
Combines volume analysis with technical indicators to scan for instruments meeting both volume and price conditions, filtered by RSI state. Use it when identifying setups where volume strength aligns with a specific market condition such as oversold or overbought.

---

### Used parameters

**(1) exchange: Optional**
Default: KUCOIN
Exchange to scan.

**(15) min_volume_ratio: Optional**
Default: 2
Minimum multiple by which current volume must exceed the normal level.

**(16) min_price_change: Optional**
Default: 2
Minimum price change percentage required to include a result.

**(17) rsi_range: Optional**
Default: any
RSI condition to filter by.
Allowed: oversold, overbought, neutral, any

**(3) limit: Optional**
Default: 20
Maximum number of results to return. Maximum allowed: 30 for this tool.

---

### JSON input alternatives

```json
{
  "intent": "Scan Binance for high-volume moves in oversold RSI territory",
  "params": {
    "exchange": "BINANCE",
    "rsi_range": "oversold",
    "min_volume_ratio": 2
  }
}
```

```json
{
  "intent": "Scan for overbought coins with strong volume and a larger price move",
  "params": {
    "exchange": "BYBIT",
    "rsi_range": "overbought",
    "min_volume_ratio": 3,
    "min_price_change": 5,
    "limit": 10
  }
}
```
