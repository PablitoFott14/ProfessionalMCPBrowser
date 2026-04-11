## financial-datasets_get_sec_filings

### What this tool is for
Retrieves SEC filings submitted by a company to the U.S. Securities and Exchange Commission. Useful when the user needs to review regulatory disclosures, financial reports, or material event announcements for a given company.

---

### Used parameters

**(1) ticker — Required**
Default: No default
Ticker symbol of the company whose filings are being retrieved.

**(2) limit — Optional**
Default: 10
Controls how many filings are returned.

**(3) filing_type — Optional**
Default: null
Filters results to a specific filing type (e.g., 10-K for annual reports, 10-Q for quarterly reports, 8-K for material events).

---

### JSON input alternatives

```json
{
  "intent": "Get the most recent annual reports filed by Apple",
  "params": {
    "ticker": "AAPL",
    "filing_type": "10-K"
  }
}
```

```json
{
  "intent": "Retrieve the last 20 SEC filings for Tesla across all types",
  "params": {
    "ticker": "TSLA",
    "limit": 20
  }
}
```

### Potential resolution paths

**"I want to review the annual report before pulling the financial statements."**
Use `get_sec_filings` filtered to `10-K` to retrieve the most recent annual report, then call `get_income_statements`, `get_balance_sheets`, and `get_cash_flow_statements` to verify and explore the reported figures in detail.

**"Were there any material events that could explain a recent price move?"**
Fetch `get_sec_filings` filtered to `8-K` to surface material event filings, then cross-reference with `get_company_news` and `get_historical_stock_prices` over the same period.

**"What has the company disclosed in the most recent quarter?"**
Call `get_sec_filings` filtered to `10-Q` for the latest quarterly filing, then use `get_income_statements` with `period` set to quarterly to review the underlying financial data in parallel.
