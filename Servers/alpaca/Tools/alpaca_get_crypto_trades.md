## alpaca_get_crypto_trades

### What this tool is for
Historical trade prints for one or more cryptocurrencies, including individual execution price, size, and timestamp. Use this when the user needs tick-level crypto trade activity rather than aggregated bars or quotes.

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
Maximum number of trade records to return.

**(7) start — Optional**
Default: null
Start time in ISO format (e.g., 2023-01-01T09:30:00). Overrides days/hours/minutes lookback.

**(8) end — Optional**
Default: null
End time in ISO format (e.g., 2023-01-01T16:00:00).

**(13) sort — Optional**
Default: null
Allowed: asc, desc
Chronological order of response.

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
  "intent": "Get the last 15 minutes of trade prints for Bitcoin",
  "params": {
    "symbol": "BTC/USD"
  }
}
```

```json
{
  "intent": "Retrieve Solana trade history over a specific time window in UTC",
  "params": {
    "symbol": "SOL/USD",
    "start": "2024-04-01T00:00:00",
    "end": "2024-04-01T04:00:00",
    "sort": "asc",
    "tz": "UTC"
  }
}
```
