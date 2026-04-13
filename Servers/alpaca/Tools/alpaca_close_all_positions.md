## alpaca_close_all_positions

### What this tool is for
All open positions on the Alpaca account in a single call. Optionally cancels all open orders first to prevent conflicts during liquidation. Use this when the user wants to fully exit the market or reset the portfolio.

---

### Used parameters

**(64) cancel_orders: Optional**
Default: false
If true, cancels all open orders before liquidating positions.

---

### JSON input alternatives

```json
{
  "intent": "Close all open positions immediately",
  "params": {}
}
```

```json
{
  "intent": "Cancel all open orders and then close all positions",
  "params": {
    "cancel_orders": true
  }
}
```
