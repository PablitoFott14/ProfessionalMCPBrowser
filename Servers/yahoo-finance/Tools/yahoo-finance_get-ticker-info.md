## yahoo-finance_get-ticker-info

### What this tool is for
Comprehensive stock data for a ticker, including company information, financial data, trading metrics, and governance-related fields. Use this when the user needs a broad company snapshot rather than a single price or narrowly scoped metric.

---

### Used parameters

**(1) symbol — Required**  
Default: No default  
Stock ticker symbol to retrieve data for.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve a broad company and trading snapshot for Apple",
  "params": {
    "symbol": "AAPL"
  }
}
```

```json
{
  "intent": "Review company, financial, and governance data for Tesla",
  "params": {
    "symbol": "TSLA"
  }
}
```
