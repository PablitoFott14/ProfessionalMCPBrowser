## financial-datasets

The financial-datasets server provides access to fundamental and market data for equities and cryptocurrencies. It covers price history, real-time quotes, financial statements, SEC filings, and company news.

### How it works
- Parameters are passed directly as flat key-value pairs — no nested `params` object is required.
- Most tools only need a ticker symbol to return useful data, with optional parameters to refine scope or volume of results.

### Tool categories

**Price data**
- Current and historical stock prices, with configurable interval and multiplier.
- Historical and current crypto prices, with a discovery tool to list available tickers.

**Fundamental data**
- Income statements, balance sheets, and cash flow statements — all supporting annual, quarterly, and TTM periods.

**Corporate data**
- SEC filings filtered by type (10-K, 10-Q, 8-K, etc.).
- Company news for tracking recent developments and market-moving events.

### Best practices
- Use `get_available_crypto_tickers` before querying crypto prices to confirm ticker availability.
- For financial statements, omit `period` and `limit` when the defaults (annual, 4 periods) match the user's intent.
- Prefer `get_current_stock_price` for point-in-time queries and `get_historical_stock_prices` when trend or range analysis is needed.
