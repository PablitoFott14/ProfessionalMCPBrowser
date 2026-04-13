## alpaca_get_stock_quotes

### What this tool is for
Historical level 1 bid/ask quote data for one or more stocks. Use this when the user needs to analyze spread dynamics, quote activity, or intraday bid/ask behavior over a short time window.

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
Maximum number of quote records to return.

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
  "intent": "Get the last 30 minutes of bid/ask quotes for Apple",
  "params": {
    "symbol": "AAPL",
    "minutes": 30
  }
}
```

```json
{
  "intent": "Retrieve quote data for multiple stocks over a specific intraday window",
  "params": {
    "symbol": ["MSFT", "GOOGL"],
    "start": "2024-06-10T09:30:00",
    "end": "2024-06-10T11:00:00",
    "feed": "sip"
  }
}
```
