## yahoo-finance_get-price-history

### What this tool is for
Fetches historical price data for a stock symbol over a specified period and interval. Use this when the user needs past price movement rather than a current snapshot.

---

### Used parameters

**(1) symbol — Required**  
Default: No default  
Stock ticker symbol to retrieve price history for.

**(6) period — Optional**  
Default: 1y  
Allowed: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max  
Period of historical price data to fetch.

**(7) interval — Optional**  
Default: 1d  
Allowed: 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo  
Data interval used for the historical price series.

---

### JSON input alternatives

```json
{
  "tool": "yahoo-finance_get-price-history",
  "intent": "Fetch the default price history for Apple",
  "params": {
    "symbol": "AAPL"
  }
}
```

```json
{
  "tool": "yahoo-finance_get-price-history",
  "intent": "Retrieve six months of hourly price history for Tesla",
  "params": {
    "symbol": "TSLA",
    "period": "6mo",
    "interval": "1h"
  }
}
```
