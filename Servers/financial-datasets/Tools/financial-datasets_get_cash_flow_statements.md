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
Reporting period for the statements (annual, quarterly, ttm).

**(2) limit — Optional**
Default: 4
Number of cash flow statements to return.

---

### JSON input alternatives

```json
{
  "intent": "Get the last 4 annual cash flow statements for Apple",
  "params": {
    "ticker": "AAPL"
  }
}
```

```json
{
  "intent": "Retrieve the last 8 quarterly cash flow statements for Tesla",
  "params": {
    "ticker": "TSLA",
    "period": "quarterly",
    "limit": 8
  }
}
```

### Potential resolution paths

**"Does this company generate real cash or is profitability just on paper?"**
Call `get_cash_flow_statements` alongside `get_income_statements` to compare operating cash flow to net income. A persistent gap between the two often signals accounting-driven earnings.

**"Is cash burn accelerating quarter over quarter?"**
Request `get_cash_flow_statements` with `period` set to quarterly and a higher `limit` to trace operating and free cash flow trends over time.

**"I need a complete view of capital allocation before making an investment decision."**
Use `get_cash_flow_statements` together with `get_balance_sheets` to see how cash generated is being deployed — into debt repayment, capex, or shareholder returns.
