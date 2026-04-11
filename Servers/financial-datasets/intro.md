## financial-datasets

The financial-datasets server provides fundamental and market data for public equities and cryptocurrencies. Parameters are passed as flat key-value pairs — no wrapping object is required.

### How it works
- Most tools require only a ticker symbol. Optional parameters refine the period, granularity, or volume of results.
- Financial statement tools default to annual reporting and 4 periods when those parameters are omitted.
- Crypto price tools require a date range. The list of supported tickers can be retrieved before querying.

### Potential resolution paths
- **Full fundamental analysis:** Retrieve `get_income_statements`, `get_balance_sheets`, and `get_cash_flow_statements` together to cover profitability, leverage, and cash generation in one pass.
- **Research before investing:** Start with `get_company_news` to surface recent events, then pull `get_sec_filings` for the relevant filing type, and follow up with the financial statements that the filing references.
- **Crypto exploration:** Call `get_available_crypto_tickers` to confirm the symbol, then use `get_historical_crypto_prices` or `get_crypto_prices` for the target date range and granularity.
- **Price reaction to earnings:** Combine `get_historical_stock_prices` with `get_income_statements` over matching periods to evaluate how the market responded to reported results.

### Best practices
- Use `get_available_crypto_tickers` to confirm a ticker is supported before querying crypto price data.
- Prefer `get_current_stock_price` for a real-time snapshot and `get_historical_stock_prices` when trend or range context is needed.
- For financial statements, only specify `period` and `limit` when the defaults do not match the user's intent.
