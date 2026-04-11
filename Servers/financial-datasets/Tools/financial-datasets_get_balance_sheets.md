## financial-datasets_get_balance_sheets

### What this tool is for
Retrieves balance sheets for a company, covering assets, liabilities, and shareholders' equity. Use this when the user needs to evaluate a company's financial position, solvency, or capital structure at a point in time.

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
Number of balance sheets to return.

---

### JSON input alternatives

```json
{
  "intent": "Get the last 4 annual balance sheets for Google",
  "params": {
    "ticker": "GOOGL"
  }
}
```

```json
{
  "intent": "Retrieve the last 6 quarterly balance sheets for JPMorgan",
  "params": {
    "ticker": "JPM",
    "period": "quarterly",
    "limit": 6
  }
}
```

### Potential resolution paths

**"Is this company financially healthy?"**
Combine `get_balance_sheets` with `get_income_statements` and `get_cash_flow_statements` to assess leverage, profitability, and cash generation together. No single statement gives the full picture.

**"Has the company taken on significantly more debt recently?"**
Call `get_balance_sheets` with `period` set to quarterly and a higher `limit` to trace debt levels across multiple reporting periods.

**"I want to review the annual report and then validate the balance sheet numbers."**
Fetch `get_sec_filings` filtered to `10-K` first for the qualitative context, then call `get_balance_sheets` to confirm the reported figures.
