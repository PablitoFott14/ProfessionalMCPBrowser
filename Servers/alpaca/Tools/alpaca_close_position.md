## alpaca_close_position

### What this tool is for
Closes an open position for a specific symbol, either fully or partially by quantity or percentage. Use this when the user wants to exit or reduce a holding. Will return an error if no position exists for the given symbol.

---

### Used parameters

**(1) symbol — Required**
Default: No default
Ticker symbol of the position to close (e.g., AAPL, BTC/USD).

**(59) qty — Optional**
Default: null
Number of shares or units to liquidate. If omitted alongside percentage, the full position is closed.

**(63) percentage — Optional**
Default: null
Percentage of the position to liquidate (e.g., "50" for 50%). Must result in at least 1 share.

---

### JSON input alternatives

```json
{
  "tool": "alpaca_close_position",
  "intent": "Close the entire Apple position",
  "params": {
    "symbol": "AAPL"
  }
}
```

```json
{
  "tool": "alpaca_close_position",
  "intent": "Reduce the Tesla position by half",
  "params": {
    "symbol": "TSLA",
    "percentage": "50"
  }
}
```
