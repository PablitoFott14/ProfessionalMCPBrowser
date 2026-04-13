## alpaca_get_option_chain

### What this tool is for
The full option chain for an underlying symbol, including latest quote, trade, implied volatility, and Greeks for each contract. Use this when the user wants to browse all available contracts for a given stock or ETF and evaluate them across strikes and expirations in one call.

---

### Used parameters

**(43) underlying_symbol — Required**
Default: No default
Single underlying asset symbol to retrieve the option chain for (e.g., AAPL, SPY).

**(42) feed (options) — Optional**
Default: null (opra if subscribed, indicative otherwise)
Allowed: opra, indicative
Options data feed source. OPRA requires a subscription.

**(40) contract_type — Optional**
Default: null
Allowed: call, put
Filters by contract type (null for both).

**(38) strike_price_gte — Optional**
Default: null
Minimum strike price to include in results.

**(39) strike_price_lte — Optional**
Default: null
Maximum strike price to include in results.

**(34) expiration_date — Optional**
Default: null
Filters to a specific expiration date (YYYY-MM-DD).

**(35) expiration_date_gte — Optional**
Default: null
Minimum expiration date for the filter range (YYYY-MM-DD).

**(36) expiration_date_lte — Optional**
Default: null
Maximum expiration date for the filter range (YYYY-MM-DD).

**(41) root_symbol — Optional**
Default: null
Filters contracts by root symbol.

**(12) limit — Optional**
Default: null (max 1000)
Maximum number of contract snapshots to return.

---

### JSON input alternatives

```json
{
  "tool": "alpaca_get_option_chain",
  "intent": "Get the full options chain for SPY showing all calls and puts",
  "params": {
    "underlying_symbol": "SPY"
  }
}
```

```json
{
  "tool": "alpaca_get_option_chain",
  "intent": "Retrieve near-the-money Apple call options expiring within the next month",
  "params": {
    "underlying_symbol": "AAPL",
    "contract_type": "call",
    "strike_price_gte": 190,
    "strike_price_lte": 220,
    "expiration_date_gte": "2025-05-01",
    "expiration_date_lte": "2025-05-31"
  }
}
```
