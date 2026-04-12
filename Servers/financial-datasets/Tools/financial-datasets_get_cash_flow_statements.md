## financial-datasets_get_cash_flow_statements

### What this tool is for
Retrieves cash flow statements for a company, covering operating, investing, and financing activities. Use this when the user needs to assess a company's liquidity, capital allocation, or free cash flow generation over time.

---

### Used parameters

**(1) ticker — Required**
Default: No default
Ticker symbol of the company (e.g., AAPL, GOOGL).

**(8) period — Optional**
Default: annual
Allowed: annual, quarterly, ttm
Reporting period for the statements.

**(2) limit — Optional**
Default: 4
Number of cash flow statements to return.

---

### JSON input alternatives

```json
{
  "tool": "financial-datasets_get_cash_flow_statements",
  "intent": "Get the last 4 annual cash flow statements for Apple",
  "params": {
    "ticker": "AAPL"
  }
}
```

```json
{
  "tool": "financial-datasets_get_cash_flow_statements",
  "intent": "Retrieve the last 8 quarterly cash flow statements for Tesla",
  "params": {
    "ticker": "TSLA",
    "period": "quarterly",
    "limit": 8
  }
}
```
