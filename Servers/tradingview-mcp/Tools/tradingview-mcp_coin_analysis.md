## tradingview-mcp_coin_analysis

### What this tool is used for
Returns detailed analysis for a specific trading pair on a given exchange and timeframe, including all indicators and metrics. Use it when a deep look at a single instrument is needed after identifying it through a scan or filter tool.

---

### Used parameters

**(6) symbol: Required**
Default: No default
Trading pair symbol to analyze (e.g., "BTCUSDT", "ACEUSDT").

**(1) exchange: Optional**
Default: KUCOIN
Exchange where the symbol is listed (e.g., "BINANCE", "KUCOIN").

**(2) timeframe: Optional**
Default: 15m
Timeframe for the analysis.
Allowed: 5m, 15m, 1h, 4h, 1D, 1W, 1M

---

### JSON input alternatives

```json
{
  "intent": "Get detailed analysis for Bitcoin on Binance on the 1-hour timeframe",
  "params": {
    "symbol": "BTCUSDT",
    "exchange": "BINANCE",
    "timeframe": "1h"
  }
}
```

```json
{
  "intent": "Get full indicator analysis for a trading pair on the daily timeframe",
  "params": {
    "symbol": "ETHUSDT",
    "exchange": "BYBIT",
    "timeframe": "1D"
  }
}
```
