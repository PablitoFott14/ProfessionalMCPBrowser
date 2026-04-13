## tradingview-mcp_consecutive_candles_scan

### What this tool is used for
Scans for instruments showing a pattern of consecutive growing or shrinking candles on a given exchange and timeframe. Use it when identifying instruments with sustained directional momentum across a sequence of candles.

---

### Used parameters

**(1) exchange: Optional**
Default: KUCOIN
Exchange to scan (e.g., "KUCOIN", "BINANCE").

**(2) timeframe: Optional**
Default: 15m
Timeframe for the candle pattern scan.
Allowed: 5m, 15m, 1h, 4h

**(7) pattern_type: Optional**
Default: bullish
Direction of the consecutive candle pattern to detect.
Allowed: bullish, bearish

**(8) candle_count: Optional**
Default: 3
Number of consecutive candles to check. Range: 2 to 5.

**(9) min_growth: Optional**
Default: 2
Minimum growth percentage required for each candle in the pattern.

**(3) limit: Optional**
Default: 20
Maximum number of results to return.

---

### JSON input alternatives

```json
{
  "intent": "Scan Binance for coins with 3 consecutive bullish candles on the 1-hour timeframe",
  "params": {
    "exchange": "BINANCE",
    "timeframe": "1h",
    "pattern_type": "bullish",
    "candle_count": 3
  }
}
```

```json
{
  "intent": "Scan KuCoin for bearish consecutive candle patterns with a stricter growth threshold",
  "params": {
    "exchange": "KUCOIN",
    "timeframe": "4h",
    "pattern_type": "bearish",
    "candle_count": 4,
    "min_growth": 3
  }
}
```
