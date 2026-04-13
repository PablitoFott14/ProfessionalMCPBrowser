## tradingview-mcp

The `tradingview-mcp` server provides access to TradingView market data and technical analysis for cryptocurrency trading pairs. It covers exchange-wide scanning (top movers, Bollinger Band squeezes, rating filters, candle patterns, volume breakouts), symbol-specific analysis (indicators, volume confirmation), and multi-agent structured trade decisions. It is useful when screening for trading opportunities, validating technical setups, or producing a comprehensive assessment of a specific instrument.

### How it works
- The server is organized around two entry points: scan tools that return lists of candidates from an exchange, and analysis tools that take a specific symbol and return deep per-instrument output.
- Scan tools (`top_gainers`, `top_losers`, `bollinger_scan`, `rating_filter`, `consecutive_candles_scan`, `advanced_candle_pattern`, `volume_breakout_scanner`, `smart_volume_scanner`) accept an exchange and timeframe and return ranked or filtered lists of symbols.
- Analysis tools (`coin_analysis`, `volume_confirmation_analysis`, `multi_agent_analysis`) require a `symbol` and return detailed output for that instrument alone.
- All tools default to the KUCOIN exchange and the 15m timeframe unless otherwise specified. `bollinger_scan` defaults to 4h.
- `multi_agent_analysis` runs Technical, Sentiment, and Risk perspectives as a structured debate before producing a final trading decision.

### Potential resolution paths
- **Find top movers on an exchange:** Use `top_gainers` or `top_losers` with the desired exchange and timeframe to get the highest-performing or worst-performing coins in the period.
- **Identify breakout candidates:** Use `bollinger_scan` to find instruments in a volatility squeeze, then `coin_analysis` on selected symbols to review their full indicator picture.
- **Filter by bullish or bearish rating:** Use `rating_filter` to retrieve coins meeting a specific Bollinger Band rating threshold, then `coin_analysis` to drill into candidates.
- **Detect candle momentum setups:** Use `consecutive_candles_scan` for streaks of same-direction candles, or `advanced_candle_pattern` for multi-timeframe candle expansion patterns, then validate with `coin_analysis`.
- **Identify volume-driven moves:** Use `volume_breakout_scanner` or `smart_volume_scanner` to find instruments with abnormal volume, then use `volume_confirmation_analysis` to verify whether volume supports the price move on a specific symbol.
- **Produce a structured trade decision:** Use `multi_agent_analysis` directly on a known symbol when a comprehensive multi-dimensional assessment is needed.

### Best practices
- **Use scan tools to identify candidates before calling analysis tools:** `coin_analysis`, `volume_confirmation_analysis`, and `multi_agent_analysis` require a known `symbol`. Use any scan tool first to narrow the universe before calling these.
- **Set the exchange explicitly when not using KuCoin:** All tools default to KUCOIN. Pass `exchange` explicitly (e.g., "BINANCE", "BYBIT") when scanning a different market.
- **Match the timeframe to the trading context:** Shorter timeframes (5m, 15m) suit intraday setups; 4h and 1D are more appropriate for swing analysis. `bollinger_scan` defaults to 4h, which is suitable for breakout detection.
- **Use `multi_agent_analysis` for final decisions, not initial screening:** It provides the most comprehensive output but is scoped to a single symbol. Use it after a candidate has already been identified through scanning.
