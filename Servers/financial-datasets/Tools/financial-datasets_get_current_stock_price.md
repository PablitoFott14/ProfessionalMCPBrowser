## financial-datasets_get_current_stock_price

### What this tool is for
Returns the current or most recent price for a given stock. Use this when the user needs a quick snapshot of where a stock is trading right now, without historical context.

---

### Used parameters

**(1) ticker — Required**
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

### Potential resolution paths

**"Is the stock moving on news today?"**
Call `get_current_stock_price` for the latest price, then `get_company_news` to check for recent headlines that could explain the move.

**"How does today's price compare to the company's fundamentals?"**
Use `get_current_stock_price` alongside `get_income_statements` to contextualize valuation — for example, comparing price to trailing earnings.

**"Quick price check before deciding whether to look deeper into the company."**
`get_current_stock_price` alone is sufficient for a point-in-time snapshot. If the price warrants further investigation, follow up with `get_historical_stock_prices` for trend context or `get_balance_sheets` for financial health.
