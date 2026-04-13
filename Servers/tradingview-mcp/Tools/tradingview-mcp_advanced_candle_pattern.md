## tradingview-mcp_advanced_candle_pattern

### What this tool is used for
Analyzes multi-timeframe candle data to detect instruments showing a progressive increase in candle size across consecutive periods. Use it when identifying coins with accelerating momentum indicated by expanding candle bodies.

---

### Used parameters

**(1) exchange: Optional**
Default: KUCOIN
Exchange to scan (e.g., "KUCOIN", "BINANCE").

**(10) base_timeframe: Optional**
Default: 15m
Base timeframe for the candle size analysis.
Allowed: 5m, 15m, 1h, 4h

**(11) pattern_length: Optional**
Default: 3
Number of consecutive periods to analyze. Range: 2 to 4.

**(12) min_size_increase: Optional**
Default: 10
Minimum percentage increase in candle size between consecutive periods.

**(3) limit: Optional**
Default: 15
Maximum number of results to return.

---

### JSON input alternatives

```json
{
  "intent": "Scan Binance for coins with accelerating candle size over 3 periods on the 1-hour timeframe",
  "params": {
    "exchange": "BINANCE",
    "base_timeframe": "1h",
    "pattern_length": 3
  }
}
```

```json
{
  "intent": "Scan for coins with aggressive candle expansion over 4 periods with a higher size threshold",
  "params": {
    "exchange": "KUCOIN",
    "base_timeframe": "4h",
    "pattern_length": 4,
    "min_size_increase": 20,
    "limit": 10
  }
}
```
