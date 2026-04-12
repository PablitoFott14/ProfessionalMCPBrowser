## TwelveData

The TwelveData server is a broad market intelligence layer for researching instruments, pulling price history, checking current market state, and layering technical indicators over the same symbol and interval. It is especially strong when the goal is to move from discovery to analysis quickly across equities, ETFs, forex, crypto, commodities, and related market metadata.

### How it works
- The server combines instrument discovery tools, quote and price endpoints, reference data, and time series analysis in one place.
- It supports both simple point-in-time checks and deeper workflows such as chart building, trend analysis, and indicator confirmation.
- Requests use a `params` object, but the main value of the server is the breadth of analysis it enables once a symbol or asset class is identified.

### Potential resolution paths
- **Discover, then analyze a market:** Start with symbol lookup or asset-listing tools such as `GetSymbolSearch`, `GetStocks`, `GetEtf`, `GetCryptocurrencies`, or `GetForexPairs`, then move into `GetQuote`, `GetPrice`, or `GetTimeSeries` for the actual market view.
- **Build a richer technical read on a symbol:** Pull `GetTimeSeries`, then add indicators such as `GetTimeSeriesSma`, `GetTimeSeriesEma`, `GetTimeSeriesRsi`, `GetTimeSeriesMacd`, `GetTimeSeriesBBands`, or `GetTimeSeriesAdx` to validate trend, momentum, and volatility from different angles.
- **Move from market context to security context:** Combine `GetMarketState`, `GetProfile`, `GetStatistics`, `GetEarnings`, `GetDividends`, or `GetSplits` to understand not only what a symbol is doing, but also what kind of asset it is and what events may matter around it.

### Best practices
- **Choose tools by intent, not just by endpoint name:** Use discovery tools for finding the right asset first, quote tools for quick checks, and time series plus indicators when the task requires trend or signal analysis.
- **Keep the workflow compact:** In many cases, the best result comes from a short sequence such as symbol discovery, current price check, then historical or indicator follow-up on the same symbol.
