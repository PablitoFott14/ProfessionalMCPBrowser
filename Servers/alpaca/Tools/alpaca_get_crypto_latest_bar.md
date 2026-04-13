## alpaca_get_crypto_latest_bar

### What this tool is for
The latest minute bar for one or more cryptocurrency symbols. Use this when the user needs the most recent OHLCV snapshot for a crypto pair without pulling historical data.

---

### Used parameters

**(1) symbol — Required**
Default: No default
Crypto symbol or list of symbols (e.g., BTC/USD or ["BTC/USD", "ETH/USD"]).

**(28) feed — Optional**
Default: us
Allowed: us
Crypto data feed to retrieve from. Currently only "us" is supported.

---

### JSON input alternatives

```json
{
  "intent": "Get the latest minute bar for Ethereum",
  "params": {
    "symbol": "ETH/USD"
  }
}
```

```json
{
  "intent": "Get the latest bars for Bitcoin and Solana simultaneously",
  "params": {
    "symbol": ["BTC/USD", "SOL/USD"]
  }
}
```
