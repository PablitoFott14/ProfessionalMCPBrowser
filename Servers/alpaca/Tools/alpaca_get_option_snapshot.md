## alpaca_get_option_snapshot

### What this tool is for
A comprehensive snapshot for one or more option contracts, combining the latest quote, latest trade, implied volatility, and Greeks (delta, gamma, theta, vega, rho) in a single call. Use this when the user needs a full picture of an option contract's current market state and risk metrics.

Option contract symbols follow the OCC format (e.g., AAPL250613P00205000). Use `get_option_contracts` first to discover available contract symbols.

---

### Used parameters

**(32) symbol_or_symbols — Required**
Default: No default
Option contract symbol or list of symbols (e.g., AAPL250613P00205000 or ["AAPL250613P00205000", "MSFT250613C00400000"]).

**(42) feed (options) — Optional**
Default: null (opra if subscribed, indicative otherwise)
Allowed: opra, indicative
Options data feed source. OPRA requires a subscription.

---

### JSON input alternatives

```json
{
  "intent": "Get a full snapshot including Greeks and IV for a specific Apple put option",
  "params": {
    "symbol_or_symbols": "AAPL250613P00205000"
  }
}
```

```json
{
  "intent": "Retrieve snapshots for multiple option contracts using the indicative feed",
  "params": {
    "symbol_or_symbols": ["AAPL250613P00205000", "MSFT250613C00400000"],
    "feed": "indicative"
  }
}
```
