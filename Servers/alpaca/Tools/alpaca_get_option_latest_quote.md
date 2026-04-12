## alpaca_get_option_latest_quote

### What this tool is for
Retrieves the latest real-time bid/ask quote for one or more option contracts, including prices, sizes, exchange information, and timestamp. Use this when the user needs current market pricing for a specific options position or wants to evaluate spread before trading.

Option contract symbols follow the OCC format (e.g., AAPL230616C00150000). Use `get_option_contracts` first to discover available contract symbols.

---

### Used parameters

**(32) symbol_or_symbols — Required**
Default: No default
Option contract symbol or list of symbols (e.g., AAPL230616C00150000 or ["AAPL230616C00150000", "MSFT230616P00300000"]).

**(42) feed (options) — Optional**
Default: null (opra if subscribed, indicative otherwise)
Allowed: opra, indicative
Options data feed source. OPRA requires a subscription.

---

### JSON input alternatives

```json
{
  "tool": "alpaca_get_option_latest_quote",
  "intent": "Get the latest quote for a specific Apple call option",
  "params": {
    "symbol_or_symbols": "AAPL230616C00150000"
  }
}
```

```json
{
  "tool": "alpaca_get_option_latest_quote",
  "intent": "Retrieve latest quotes for multiple option contracts using indicative feed",
  "params": {
    "symbol_or_symbols": ["AAPL230616C00150000", "MSFT230616P00300000"],
    "feed": "indicative"
  }
}
```
