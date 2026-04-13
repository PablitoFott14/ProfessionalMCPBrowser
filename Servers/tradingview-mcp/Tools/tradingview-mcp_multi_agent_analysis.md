## tradingview-mcp_multi_agent_analysis

### What this tool is used for
Runs a multi-agent debate across Technical, Sentiment, and Risk perspectives for a specific trading pair, producing a structured final trading decision. Use it when a comprehensive, multi-dimensional assessment of a specific instrument is needed beyond standard indicator output.

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
Timeframe for the analysis.
Allowed: 5m, 15m, 1h, 4h, 1D, 1W, 1M

---

### JSON input alternatives

```json
{
  "intent": "Run a multi-agent debate analysis for Bitcoin on Binance on the 4-hour timeframe",
  "params": {
    "symbol": "BTCUSDT",
    "exchange": "BINANCE",
    "timeframe": "4h"
  }
}
```

```json
{
  "intent": "Get a structured multi-agent trading decision for a specific coin on the daily timeframe",
  "params": {
    "symbol": "ETHUSDT",
    "exchange": "BYBIT",
    "timeframe": "1D"
  }
}
```
