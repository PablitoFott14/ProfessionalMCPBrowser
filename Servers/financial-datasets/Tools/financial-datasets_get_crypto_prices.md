## financial-datasets_get_crypto_prices

### What this tool is for
Retrieves historical price data for a cryptocurrency over a specified date range. Functionally equivalent to `get_historical_crypto_prices` — use this as the standard tool for fetching crypto OHLC data when no special discovery step is needed.

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
  "tool": "financial-datasets_get_crypto_prices",
  "intent": "Get daily Solana prices for Q1 2024",
  "params": {
    "ticker": "SOL-USD",
    "start_date": "2024-01-01",
    "end_date": "2024-03-31"
  }
}
```

```json
{
  "tool": "financial-datasets_get_crypto_prices",
  "intent": "Retrieve 4-hour Ripple price bars for a specific month",
  "params": {
    "ticker": "XRP-USD",
    "start_date": "2024-06-01",
    "end_date": "2024-06-30",
    "interval": "hour",
    "interval_multiplier": 4
  }
}
```
