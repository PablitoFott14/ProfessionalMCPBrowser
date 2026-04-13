## financial-datasets_get_current_stock_price

### What this tool is for
The current or most recent price for a given stock. Use this when the user needs a quick snapshot of where a stock is trading right now, without historical context.

---

### Used parameters

**(1) ticker: Required**
Default: No default
Ticker symbol of the company (e.g., AAPL, GOOGL).

---

### JSON input alternatives

```json
{
  "intent": "Get the current price of Amazon stock",
  "params": {
    "ticker": "AMZN"
  }
}
```
