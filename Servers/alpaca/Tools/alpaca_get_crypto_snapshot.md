## alpaca_get_crypto_snapshot

### What this tool is for
Returns a comprehensive snapshot for one or more cryptocurrency symbols in a single call, combining the latest quote, latest trade, current minute bar, current daily bar, and previous daily bar. Use this when the user needs a full picture of a crypto pair's current market state without making multiple separate requests.

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
  "intent": "Get a full market snapshot for Bitcoin including quote, trade, and bars",
  "params": {
    "symbol": "BTC/USD"
  }
}
```

```json
{
  "intent": "Retrieve snapshots for Bitcoin and Ethereum simultaneously",
  "params": {
    "symbol": ["BTC/USD", "ETH/USD"]
  }
}
```
