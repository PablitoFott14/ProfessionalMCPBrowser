## alpaca_get_stock_trades

### What this tool is for
Retrieves historical trade-level data for one or more stocks, including individual executions with price, size, and timestamp. Use this when the user needs tick-level trade activity rather than aggregated bars or quotes.

---

### Used parameters

**(1) symbol — Required**
Default: No default
Stock ticker symbol or list of symbols (e.g., AAPL or ["AAPL", "MSFT"]).

**(25) days — Optional**
Default: 0
Number of days to look back from now. Ignored if start is provided.

**(26) hours — Optional**
Default: 0
Number of hours to look back from now. Ignored if start is provided.

**(27) minutes — Optional**
Default: 20
Number of minutes to look back from now. Ignored if start is provided.

**(12) limit — Optional**
Default: null
Maximum number of trade records to return.

**(7) start — Optional**
Default: null
Start time in ISO format (e.g., 2023-01-01 or 2023-01-01T09:30:00). Overrides days/hours/minutes lookback.

**(8) end — Optional**
Default: null
End time in ISO format (e.g., 2023-01-01 or 2023-01-01T16:00:00).

**(13) sort — Optional**
Default: asc
Chronological order of response (asc or desc).

**(28) feed — Optional**
Default: null
Market data feed to retrieve from (iex, sip, delayed_sip, otc).

**(29) currency — Optional**
Default: null (USD)
Currency for price values (e.g., USD, EUR, GBP).

**(30) asof — Optional**
Default: null
As-of date for symbol resolution in YYYY-MM-DD format.

**(31) tz — Optional**
Default: America/New_York
Timezone for interpreting naive datetime strings (e.g., UTC, America/New_York).

---

### JSON input alternatives

```json
{
  "intent": "Get the last 30 minutes of individual trades for Tesla",
  "params": {
    "symbol": "TSLA",
    "minutes": 30
  }
}
```

```json
{
  "intent": "Retrieve trade history for Apple and Nvidia over a specific morning session",
  "params": {
    "symbol": ["AAPL", "NVDA"],
    "start": "2024-05-15T09:30:00",
    "end": "2024-05-15T12:00:00",
    "feed": "sip",
    "sort": "asc"
  }
}
```
