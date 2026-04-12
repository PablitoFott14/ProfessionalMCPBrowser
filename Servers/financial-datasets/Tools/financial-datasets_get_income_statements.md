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
