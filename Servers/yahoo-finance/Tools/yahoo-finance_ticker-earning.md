## yahoo-finance_ticker-earning

### What this tool is for
Earnings data for a ticker, including annual or quarterly data and upcoming earnings dates when available. Use this when the user needs reported earnings context rather than price or news data.

---

### Used parameters

**(1) symbol — Required**  
Default: No default  
Stock ticker symbol to retrieve earnings data for.

**(6) period — Optional**  
Default: annual  
Allowed: annual, quarterly  
Earnings period to retrieve.

**(9) date — Optional**  
Default: null  
Specific date used to retrieve earnings data when supported.

---

### JSON input alternatives

```json
{
  "tool": "yahoo-finance_ticker-earning",
  "intent": "Retrieve the most recent annual earnings data for Apple",
  "params": {
    "symbol": "AAPL"
  }
}
```

```json
{
  "tool": "yahoo-finance_ticker-earning",
  "intent": "Get quarterly earnings data for Tesla around a specific date",
  "params": {
    "symbol": "TSLA",
    "period": "quarterly",
    "date": "2024-10-23"
  }
}
```
