## akshare-one-mcp_get_news_data

### What this tool is for
Recent news related to a stock. It is useful when the user wants quick visibility into the latest headlines, developments, or sentiment-driving events around a specific symbol.

---

### Used parameters

**(1) symbol — Required**  
Default: No default  
Stock symbol or ticker to retrieve news for.

**(9) recent_n — Optional**  
Default: 10  
Limits how many of the most recent news records are returned.

---

### JSON input alternatives

```json
{
  "intent": "Review the latest headlines for a mainland China bank stock",
  "params": {
    "symbol": "000001"
  }
}

{
  "intent": "Pull a wider set of recent news items for a large Hong Kong listed technology company",
  "params": {
    "symbol": "00700",
    "recent_n": 25
  }
}
```
