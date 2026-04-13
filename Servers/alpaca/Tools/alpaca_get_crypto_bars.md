## alpaca_get_crypto_bars

### What this tool is for
Historical OHLCV price bars for one or more cryptocurrencies over a configurable timeframe and time range. Supports relative lookback via days/hours/minutes or explicit ISO date ranges. Use this when the user needs crypto bar data for trend analysis, charting, or strategy backtesting.

---

### Used parameters

**(1) symbol — Required**
Default: No default
Crypto symbol or list of symbols (e.g., BTC/USD or ["BTC/USD", "ETH/USD"]).

**(25) days — Optional**
Default: 1
Number of days to look back from now. Ignored if start is provided.

**(26) hours — Optional**
Default: 0
Number of hours to look back from now. Ignored if start is provided.

**(27) minutes — Optional**
Default: 30
Number of minutes to look back from now. Ignored if start is provided.

**(14) timeframe — Optional**
Default: 1Hour
Bar resolution. Supports minute (e.g., 5Min, 15Min), hour (e.g., 1Hour, 4Hour), day (1Day), week (1Week), and month (1Month) formats.

**(12) limit — Optional**
Default: null
Maximum number of bars to return.

**(7) start — Optional**
Default: null
Start time in ISO format (e.g., 2023-01-01 or 2023-01-01T09:30:00). Overrides days/hours/minutes lookback.

**(8) end — Optional**
Default: null
End time in ISO format (e.g., 2023-01-01 or 2023-01-01T16:00:00).

**(28) feed — Optional**
Default: us
Allowed: us
Crypto data feed to retrieve from. Currently only "us" is supported.

**(31) tz — Optional**
Default: America/New_York
Timezone for interpreting naive datetime strings (e.g., UTC, America/New_York).

---

### JSON input alternatives

```json
{
  "tool": "alpaca_get_crypto_bars",
  "intent": "Get the last 7 days of hourly bars for Bitcoin",
  "params": {
    "symbol": "BTC/USD",
    "days": 7
  }
}
```

```json
{
  "tool": "alpaca_get_crypto_bars",
  "intent": "Retrieve 4-hour Ethereum bars for a specific date range",
  "params": {
    "symbol": "ETH/USD",
    "start": "2024-01-01",
    "end": "2024-03-31",
    "timeframe": "4Hour"
  }
}
```
