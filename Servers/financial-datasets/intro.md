## financial-datasets

The `financial-datasets` server is designed for research-heavy workflows. It brings together company financial statements, SEC filings, market prices, company news, and crypto price history so users can move from a quick market question into a more complete fundamental or event-driven analysis without leaving the same server context.

### How it works
- The server covers both fundamentals and market behavior, making it useful for linking financial performance, disclosures, headlines, and price movement.
- It supports equity research workflows especially well, since statements, filings, news, and historical prices can be combined around the same company.
- Inputs are generally simple, but the real strength is in combining several tools to answer broader investment or research questions.

### Potential resolution paths
- **Run a full company research pass:** Combine `get_income_statements`, `get_balance_sheets`, and `get_cash_flow_statements` to understand profitability, financial position, and cash generation together.
- **Link narrative to numbers:** Use `get_company_news` and `get_sec_filings` to identify important developments, then review the related statements or price history to see how those events connect to fundamentals and market reaction.
- **Move between current view and historical context:** Start with `get_current_stock_price` for a quick check, then expand into `get_historical_stock_prices`, `get_crypto_prices`, or `get_historical_crypto_prices` when the user needs trend, volatility, or event-window analysis.

### Best practices
- **Treat the server as a research bundle, not a set of isolated endpoints:** Its value increases when `get_sec_filings`, `get_company_news`, `get_income_statements`, `get_balance_sheets`, `get_cash_flow_statements`, `get_current_stock_price`, and `get_historical_stock_prices` are read together.
- **Match the tool to the depth of the question:** Use `get_current_stock_price` or `get_crypto_prices` for quick checks, `get_historical_stock_prices` or `get_historical_crypto_prices` for trend analysis, and `get_income_statements`, `get_balance_sheets`, `get_cash_flow_statements`, or `get_sec_filings` when the user is really asking about business quality or disclosure.
