(1) exchange
Exchange name to query (e.g., "KUCOIN", "BINANCE", "BYBIT").
Optional. Default: KUCOIN.

(2) timeframe
Timeframe for the analysis.
Optional. Default: 15m.
Allowed: 5m, 15m, 1h, 4h, 1D, 1W, 1M.

(3) limit
Maximum number of rows to return.
Optional. Default and maximum vary by tool.

(4) bbw_threshold
Maximum Bollinger Band Width value to filter by (squeeze detection threshold).
Optional. Default: 0.04.

(5) rating
Bollinger Band rating to filter by. Range: -3 to +3. -3=Strong Sell, -2=Sell, -1=Weak Sell, 1=Weak Buy, 2=Buy, 3=Strong Buy.
Optional. Default: 2.

(6) symbol
Trading pair symbol (e.g., "BTCUSDT", "ACEUSDT").
Required. No default value.

(7) pattern_type
Candle pattern direction to scan for.
Optional. Default: bullish.
Allowed: bullish, bearish.

(8) candle_count
Number of consecutive candles to check. Range: 2 to 5.
Optional. Default: 3.

(9) min_growth
Minimum growth percentage required for each candle in the pattern.
Optional. Default: 2.

(10) base_timeframe
Base timeframe for multi-timeframe candle pattern analysis.
Optional. Default: 15m.
Allowed: 5m, 15m, 1h, 4h.

(11) pattern_length
Number of consecutive periods to analyze. Range: 2 to 4.
Optional. Default: 3.

(12) min_size_increase
Minimum percentage increase in candle size between consecutive periods.
Optional. Default: 10.

(13) volume_multiplier
Minimum multiple by which volume must exceed the normal level.
Optional. Default: 2.

(14) price_change_min
Minimum price change percentage required for the breakout.
Optional. Default: 3.

(15) min_volume_ratio
Minimum volume multiplier relative to normal level.
Optional. Default: 2.

(16) min_price_change
Minimum price change percentage to include a result.
Optional. Default: 2.

(17) rsi_range
RSI condition filter.
Optional. Default: any.
Allowed: oversold, overbought, neutral, any.
