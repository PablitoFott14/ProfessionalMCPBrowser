## financial-datasets_get_historical_crypto_prices

### What this tool is for
Retrieves historical OHLC price data for a cryptocurrency over a specified date range. Use this when the user needs to analyze past price movements, build charts, or feed crypto data into a strategy or indicator.

The available tickers can be discovered via the `get_available_crypto_tickers` tool.

---

### Used parameters

**(1) ticker — Required**
Default: No default
Ticker symbol of the cryptocurrency (e.g., BTC-USD, ETH-USD).

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
  "intent": "Get daily Bitcoin price history for the year 2023",
  "params": {
    "ticker": "BTC-USD",
    "start_date": "2023-01-01",
    "end_date": "2023-12-31"
  }
}
```

```json
{
  "intent": "Retrieve hourly Ethereum prices for a specific two-week window",
  "params": {
    "ticker": "ETH-USD",
    "start_date": "2024-03-01",
    "end_date": "2024-03-14",
    "interval": "hour"
  }
}
```
