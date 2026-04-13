## alpaca_get_orders

### What this tool is for
A filtered list of orders from the Alpaca account, including status, fill information, and order details. Use this when the user wants to review pending, completed, or all orders, optionally filtered by symbol, side, or time range.

---

### Used parameters

**(2) status — Optional**
Default: all
Allowed: open, closed, all
Filters orders by status.

**(12) limit — Optional**
Default: 10
Maximum number of orders to return (max: 500).

**(54) after — Optional**
Default: null
Returns orders submitted after this timestamp (ISO format).

**(55) until — Optional**
Default: null
Returns orders submitted up until this timestamp (ISO format).

**(56) direction — Optional**
Default: null
Allowed: asc, desc
Sort direction of results.

**(57) nested — Optional**
Default: null
Whether to roll up multi-leg orders under a legs field.

**(44) side — Optional**
Default: null
Allowed: buy, sell
Filters orders by side.

**(9) symbols — Optional**
Default: null
Filters orders by a list of ticker symbols.

---

### JSON input alternatives

```json
{
  "tool": "alpaca_get_orders",
  "intent": "Get the 20 most recent closed orders",
  "params": {
    "status": "closed",
    "limit": 20
  }
}
```

```json
{
  "tool": "alpaca_get_orders",
  "intent": "Retrieve all open buy orders for Apple and Tesla",
  "params": {
    "status": "open",
    "side": "buy",
    "symbols": ["AAPL", "TSLA"]
  }
}
```
