## tradingview-mcp_volume_confirmation_analysis

### What this tool is used for
Performs detailed volume confirmation analysis for a specific trading pair on a given exchange and timeframe. Use it when evaluating whether a price move for a specific instrument is supported by volume, after identifying it through a scan.

---

### Used parameters

**(6) symbol: Required**
Default: No default
Trading pair symbol to analyze (e.g., "BTCUSDT").

**(1) exchange: Optional**
Default: KUCOIN
Exchange where the symbol is listed.

**(2) timeframe: Optional**
Default: 15m
Timeframe for the volume confirmation analysis.
Allowed: 5m, 15m, 1h, 4h, 1D, 1W, 1M

---

### JSON input alternatives

```json
{
  "intent": "Analyze volume confirmation for Bitcoin on Binance on the 1-hour timeframe",
  "params": {
    "symbol": "BTCUSDT",
    "exchange": "BINANCE",
    "timeframe": "1h"
  }
}
```

```json
{
  "intent": "Check volume confirmation for a specific coin on the daily timeframe",
  "params": {
    "symbol": "SOLUSDT",
    "exchange": "BYBIT",
    "timeframe": "1D"
  }
}
```
