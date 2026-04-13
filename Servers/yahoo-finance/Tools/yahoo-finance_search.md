## yahoo-finance_search

### What this tool is for
Yahoo Finance for stocks, ETFs, and other financial instruments. Use this when the user needs to discover possible symbols or instruments before requesting ticker-specific data.

---

### Used parameters

**(3) query: Required**  
Default: No default  
Search query used to find matching instruments.

**(2) count: Optional**  
Default: 10  
Number of search results to return.

---

### JSON input alternatives

```json
{
  "intent": "Search for results related to Apple",
  "params": {
    "query": "Apple"
  }
}
```

```json
{
  "intent": "Retrieve a broader set of search results for semiconductor ETFs",
  "params": {
    "query": "semiconductor ETF",
    "count": 20
  }
}
```
