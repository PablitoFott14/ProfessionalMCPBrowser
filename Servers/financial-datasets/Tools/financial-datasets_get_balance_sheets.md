## financial-datasets_get_balance_sheets

### What this tool is for
Balance sheets for a company, covering assets, liabilities, and shareholders' equity. Use this when the user needs to evaluate a company's financial position, solvency, or capital structure at a point in time.

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
Number of balance sheets to return.

---

### JSON input alternatives

```json
{
  "tool": "financial-datasets_get_balance_sheets",
  "intent": "Get the last 4 annual balance sheets for Google",
  "params": {
    "ticker": "GOOGL"
  }
}
```

```json
{
  "tool": "financial-datasets_get_balance_sheets",
  "intent": "Retrieve the last 6 quarterly balance sheets for JPMorgan",
  "params": {
    "ticker": "JPM",
    "period": "quarterly",
    "limit": 6
  }
}
```
