## financial-datasets_get_income_statements

### What this tool is for
Retrieves income statements for a company, covering revenue, expenses, and profitability metrics. Use this when the user needs to analyze a company's earnings performance, margins, or growth trends over time.

---

### Used parameters

**(1) ticker — Required**
Default: No default
Ticker symbol of the company (e.g., AAPL, GOOGL).

**(8) period — Optional**
Default: annual
Reporting period for the statements (annual, quarterly, ttm).

**(2) limit — Optional**
Default: 4
Number of income statements to return.

---

### JSON input alternatives

```json
{
  "intent": "Get the last 4 annual income statements for Microsoft",
  "params": {
    "ticker": "MSFT"
  }
}
```

```json
{
  "intent": "Retrieve the last 8 quarterly income statements for Amazon to analyze revenue trends",
  "params": {
    "ticker": "AMZN",
    "period": "quarterly",
    "limit": 8
  }
}
```

### Potential resolution paths

**"Has this company been growing revenue and improving margins?"**
Call `get_income_statements` with enough periods to observe a trend — quarterly with a higher `limit` works well for recent cadence, annual for a longer view.

**"Did the stock price follow earnings growth?"**
Pair `get_income_statements` with `get_historical_stock_prices` over matching periods to compare reported performance with market reaction.

**"I need a full fundamental assessment of this company."**
Use `get_income_statements` together with `get_balance_sheets` and `get_cash_flow_statements` to evaluate profitability, financial position, and cash generation as a set. These three statements cover complementary dimensions of financial health.
