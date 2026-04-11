## financial-datasets_get_company_news

### What this tool is for
Retrieves recent news articles for a given company. Use this when the user wants to stay informed about a company's latest developments, press releases, or market-moving events.

---

### Used parameters

**(1) ticker — Required**
Default: No default
Ticker symbol of the company to retrieve news for (e.g., AAPL, GOOGL).

---

### JSON input alternatives

```json
{
  "intent": "Get the latest news for Microsoft",
  "params": {
    "ticker": "MSFT"
  }
}
```

### Potential resolution paths

**"What's behind this stock's recent price move?"**
Fetch `get_company_news` to surface recent events, then call `get_historical_stock_prices` over a matching date range to correlate price action with specific headlines.

**"Are there any developments I should be aware of before analyzing the financials?"**
Run `get_company_news` first to identify material events, then decide which financial statements are most relevant — for example, an acquisition announcement would prompt a closer look at `get_balance_sheets` and `get_cash_flow_statements`.

**"Did any news come out around the time of the company's last SEC filing?"**
Call `get_sec_filings` to find recent filing dates, then use `get_company_news` to check for related coverage around those same periods.
