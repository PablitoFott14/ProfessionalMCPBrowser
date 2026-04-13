## sec-edgar-mcp_get_financials

### What this tool is used for
Gets financial statements for a company from SEC EDGAR filings, including income statement, balance sheet, cash flow statement, or all available statements.

---

### Used parameters

**(2) identifier: Required**
Default: No default
Company ticker symbol or CIK number used to identify the company.

**(8) statement_type: Optional**
Default: all
Type of financial statement to retrieve from the SEC filing.
Allowed: income, balance, cash, all

---

### JSON input alternatives

```json
{
  "intent": "Retrieve all available financial statements for NVIDIA from SEC filings",
  "params": {
    "identifier": "NVDA"
  }
}
```

```json
{
  "intent": "Retrieve the cash flow statement for a company from SEC filings",
  "params": {
    "identifier": "AAPL",
    "statement_type": "cash"
  }
}
```
