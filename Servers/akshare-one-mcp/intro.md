## akshare-one-mcp

The akshare-one-mcp server is a stock-focused market research server that combines price data, company news, insider trading disclosures, and core financial statement coverage in one place. It is useful when the goal is to move from a quick market check into a broader company-level review without switching across separate data sources or workflows.

### How it works
- The server centers on stock symbols and supports both point-in-time checks and broader historical review.
- It combines market-facing tools such as real-time and historical data with company-facing tools such as news, insider trading, financial statements, and summary metrics.
- Most tools take a `symbol`, with optional filters such as date range, source, interval, or recent record count depending on the endpoint.

### Potential resolution paths
- **Check a stock quickly, then expand into context:** Start with `get_realtime_data` for the latest market snapshot, use `get_time_info` to anchor the timing, then pull `get_news_data` if the user needs recent developments behind the move.
- **Move from price action into deeper analysis:** Use `get_hist_data` to review the trend over time, optionally add indicators for a more technical read, then compare that behavior with `get_news_data` or `get_inner_trade_data` to add event and insider context.
- **Run a focused financial review:** Pull `get_financial_metrics` for a compact overview, then drill into `get_balance_sheet`, `get_income_statement`, and `get_cash_flow` when the user needs the underlying detail behind solvency, profitability, or cash generation.

### Best practices
- **Start with the narrowest tool that matches the question:** Use `get_realtime_data` or `get_time_info` for quick checks, and only expand into history, news, or statements when the user needs more context.
- **Use summary before detail when doing financial review:** `get_financial_metrics` is a good first pass, then the individual statement tools can be used when the user needs the supporting detail behind the headline numbers.
