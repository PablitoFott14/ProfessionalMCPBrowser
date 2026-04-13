## alpaca_get_stock_bars

### What this tool is for
Historical OHLCV price bars for one or more stocks over a configurable timeframe and time range. Supports flexible lookback via relative offsets (days, hours, minutes) or explicit ISO date ranges. Use this when the user needs bar data to analyze price history, build charts, or run strategies.

---

### Used parameters

**(1) symbol — Required**
Default: No default
Stock ticker symbol or list of symbols (e.g., AAPL or ["AAPL", "MSFT"]).

**(25) days — Optional**
Default: 5
Number of days to look back from now. Ignored if start is provided.

**(26) hours — Optional**
Default: 0
Number of hours to look back from now. Ignored if start is provided.

**(27) minutes — Optional**
Default: 30
Number of minutes to look back from now. Ignored if start is provided.

**(14) timeframe — Optional**
Default: 1Day
Bar resolution. Supports minute (e.g., 5Min, 15Min), hour (e.g., 1Hour, 4Hour), day (1Day), week (1Week), and month (1Month, 3Month, etc.) formats.

**(12) limit — Optional**
Default: 1000
Maximum number of bars to return.

**(7) start — Optional**
Default: null
Start time in ISO format (e.g., 2023-01-01 or 2023-01-01T09:30:00). Overrides days/hours/minutes lookback.

**(8) end — Optional**
Default: null
End time in ISO format (e.g., 2023-01-01 or 2023-01-01T16:00:00).

**(13) sort — Optional**
Default: asc
Allowed: asc, desc
Chronological order of response.

**(28) feed — Optional**
Default: null
Allowed: iex, sip, delayed_sip, otc
Market data feed to retrieve from.

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
  "tool": "alpaca_get_stock_bars",
  "intent": "Get the last 10 days of daily bars for Apple and Microsoft",
  "params": {
    "symbol": ["AAPL", "MSFT"],
    "days": 10,
    "timeframe": "1Day"
  }
}
```

```json
{
  "tool": "alpaca_get_stock_bars",
  "intent": "Retrieve 15-minute bars for Nvidia over a specific date range",
  "params": {
    "symbol": "NVDA",
    "start": "2024-03-01",
    "end": "2024-03-15",
    "timeframe": "15Min"
  }
}
```
