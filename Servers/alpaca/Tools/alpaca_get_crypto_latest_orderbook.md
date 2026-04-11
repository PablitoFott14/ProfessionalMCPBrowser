## alpaca_get_crypto_latest_orderbook

### What this tool is for
Returns the latest orderbook (depth of market) for one or more cryptocurrency symbols, showing current bid and ask levels with sizes. Use this when the user needs to assess market depth or liquidity for a crypto pair beyond a single best bid/ask quote.

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
  "intent": "Get the current orderbook depth for Bitcoin",
  "params": {
    "symbol": "BTC/USD"
  }
}
```

```json
{
  "intent": "Retrieve the latest orderbook for Bitcoin and Ethereum to compare liquidity",
  "params": {
    "symbol": ["BTC/USD", "ETH/USD"]
  }
}
```
