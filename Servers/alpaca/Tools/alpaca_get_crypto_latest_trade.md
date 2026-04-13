## alpaca_get_crypto_latest_trade

### What this tool is for
The latest trade execution for one or more cryptocurrency symbols, including price, size, and timestamp. Use this when the user needs the most recent transaction price for a crypto pair rather than a quote or aggregated bar.

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
  "intent": "Get the most recent trade execution for Bitcoin",
  "params": {
    "symbol": "BTC/USD"
  }
}
```

```json
{
  "intent": "Get the latest trades for Bitcoin, Ethereum, and Solana simultaneously",
  "params": {
    "symbol": ["BTC/USD", "ETH/USD", "SOL/USD"]
  }
}
```
