## alpaca_get_open_position

### What this tool is for
Retrieves details for a specific open position in the Alpaca portfolio by symbol. Use this when the user wants to inspect a single holding's quantity, market value, entry price, current price, and P/L without pulling the full portfolio.

---

### Used parameters

**(1) symbol — Required**
Default: No default
Ticker symbol of the asset to retrieve the position for (e.g., AAPL, MSFT).

---

### JSON input alternatives

```json
{
  "tool": "alpaca_get_open_position",
  "intent": "Check the current position details and P/L for Apple",
  "params": {
    "symbol": "AAPL"
  }
}
```
