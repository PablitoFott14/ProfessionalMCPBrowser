## alpaca_get_crypto_latest_quote

### What this tool is for
Returns the latest bid/ask quote for one or more cryptocurrency symbols. Use this when the user needs the current spread or most recent quote snapshot for a crypto pair without pulling historical data.

---

### Used parameters

**(1) symbol — Required**
Default: No default
Crypto symbol or list of symbols (e.g., BTC/USD or ["BTC/USD", "ETH/USD"]).

**(28) feed — Optional**
Default: us
Crypto data feed to retrieve from. Currently only "us" is supported.

---

### JSON input alternatives

```json
{
  "tool": "alpaca_get_crypto_latest_quote",
  "intent": "Get the latest bid/ask quote for Bitcoin",
  "params": {
    "symbol": "BTC/USD"
  }
}
```

```json
{
  "tool": "alpaca_get_crypto_latest_quote",
  "intent": "Get the latest quotes for Bitcoin and Ethereum simultaneously",
  "params": {
    "symbol": ["BTC/USD", "ETH/USD"]
  }
}
```
