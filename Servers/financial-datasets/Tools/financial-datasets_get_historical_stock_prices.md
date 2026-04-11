## financial-datasets_get_historical_stock_prices

### What this tool is for
Retrieves historical OHLC price data for a stock over a specified date range. Use this when the user needs to analyze past price movements, build charts, or feed equity data into a strategy or indicator.

---

### Used parameters

**(1) ticker — Required**
Default: No default
Ticker symbol of the company (e.g., AAPL, GOOGL).

**(4) start_date — Required**
Default: No default
Start date of the price data range (e.g., 2020-01-01).

**(5) end_date — Required**
Default: No default
End date of the price data range (e.g., 2020-12-31).

**(6) interval — Optional**
Default: day
Granularity of each data point (minute, hour, day, week, month).

**(7) interval_multiplier — Optional**
Default: 1
Multiplier applied to the interval unit (e.g., 2 with interval "hour" yields 2-hour bars).

---

### JSON input alternatives

```json
{
  "intent": "Get daily Apple stock prices for the full year 2023",
  "params": {
    "ticker": "AAPL",
    "start_date": "2023-01-01",
    "end_date": "2023-12-31"
  }
}
```

```json
{
  "intent": "Retrieve 30-minute intraday bars for Nvidia over a specific week",
  "params": {
    "ticker": "NVDA",
    "start_date": "2024-05-06",
    "end_date": "2024-05-10",
    "interval": "minute",
    "interval_multiplier": 30
  }
}
```

### Potential resolution paths

**"Did the stock react to an earnings release or major announcement?"**
Use `get_historical_stock_prices` over the period surrounding the event, and pair it with `get_income_statements` or `get_sec_filings` to identify the announcement dates and correlate price movement.

**"Show the price trend alongside recent news."**
Call `get_historical_stock_prices` for the relevant date range, then `get_company_news` to overlay significant headlines on the price series.

**"Build a complete picture of a company before making a decision."**
Combine `get_historical_stock_prices` with `get_income_statements`, `get_balance_sheets`, and `get_cash_flow_statements` to assess both market behavior and fundamental performance over the same time horizon.
