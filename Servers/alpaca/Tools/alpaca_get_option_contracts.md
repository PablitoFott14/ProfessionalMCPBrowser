## alpaca_get_option_contracts

### What this tool is for
Option contracts for one or more underlying assets, with flexible filtering by expiration date, strike price range, and contract type. Use this when the user needs to discover available options chains or find specific contracts before placing an options trade.

---

### Used parameters

**(33) underlying_symbols — Required**
Default: No default
Underlying asset symbol or list of symbols (e.g., SPY or ["SPY", "AAPL"]).

**(34) expiration_date — Optional**
Default: null
Filters to a specific expiration date (YYYY-MM-DD).

**(35) expiration_date_gte — Optional**
Default: null
Minimum expiration date for the filter range (YYYY-MM-DD).

**(36) expiration_date_lte — Optional**
Default: null
Maximum expiration date for the filter range (YYYY-MM-DD).

**(37) expiration_expression — Optional**
Default: null
Natural language expiration expression (e.g., "week of September 2, 2025").

**(38) strike_price_gte — Optional**
Default: null
Minimum strike price to include in results.

**(39) strike_price_lte — Optional**
Default: null
Maximum strike price to include in results.

**(40) contract_type — Optional**
Default: null
Allowed: call, put
Filters by contract type.

**(2) status — Optional**
Default: null
Allowed: active, inactive
Filters by asset status.

**(41) root_symbol — Optional**
Default: null
Filters contracts by root symbol.

**(12) limit — Optional**
Default: null
Maximum number of contracts to return.

---

### JSON input alternatives

```json
{
  "tool": "alpaca_get_option_contracts",
  "intent": "Get all active call options for Nvidia expiring in a specific week",
  "params": {
    "underlying_symbols": "NVDA",
    "expiration_expression": "week of September 2, 2025",
    "contract_type": "call"
  }
}
```

```json
{
  "tool": "alpaca_get_option_contracts",
  "intent": "Find SPY put options expiring within a date range with strikes near current price",
  "params": {
    "underlying_symbols": "SPY",
    "expiration_date_gte": "2025-09-01",
    "expiration_date_lte": "2025-09-30",
    "contract_type": "put",
    "strike_price_gte": "500",
    "strike_price_lte": "560"
  }
}
```
