## yahoo-finance_get-ticker-news

### What this tool is for
Recent news articles related to a specific stock symbol, including title, content, and source details. Use this when the user needs recent company-specific news rather than a broader company snapshot.

---

### Used parameters

**(1) symbol: Required**  
Default: No default  
Stock ticker symbol to retrieve news for.

**(2) count: Optional**  
Default: 10  
Number of news articles to fetch.

---

### JSON input alternatives

```json
{
  "intent": "Fetch the latest news articles for Apple",
  "params": {
    "symbol": "AAPL"
  }
}
```

```json
{
  "intent": "Retrieve a larger set of recent news articles for Nvidia",
  "params": {
    "symbol": "NVDA",
    "count": 25
  }
}
```
