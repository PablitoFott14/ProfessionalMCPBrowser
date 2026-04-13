## alpaca_get_crypto_quotes

### What this tool is for
Historical bid/ask quote data for one or more cryptocurrencies over a configurable time window. Use this when the user needs to analyze spread dynamics or quote activity for a crypto pair rather than aggregated price bars.

---

### Used parameters

**(1) symbol — Required**
Default: No default
Crypto symbol or list of symbols (e.g., BTC/USD or ["BTC/USD", "ETH/USD"]).

**(25) days — Optional**
Default: 0
Number of days to look back from now. Ignored if start is provided.

**(26) hours — Optional**
Default: 0
Number of hours to look back from now. Ignored if start is provided.

**(27) minutes — Optional**
Default: 15
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
  "tool": "alpaca_get_crypto_quotes",
  "intent": "Get the last 30 minutes of bid/ask quotes for Bitcoin",
  "params": {
    "symbol": "BTC/USD",
    "minutes": 30
  }
}
```

```json
{
  "tool": "alpaca_get_crypto_quotes",
  "intent": "Retrieve crypto quote history for Ethereum over a specific date range",
  "params": {
    "symbol": "ETH/USD",
    "start": "2024-06-01T00:00:00",
    "end": "2024-06-01T06:00:00",
    "tz": "UTC"
  }
}
```
