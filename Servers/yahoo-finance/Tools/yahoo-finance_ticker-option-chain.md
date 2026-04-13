## yahoo-finance_ticker-option-chain

### What this tool is for
Option chain data for a ticker, using the most recent available dates or a specific expiration date when provided. Use this when the user needs call, put, or combined option chain data for a stock.

---

### Used parameters

**(1) symbol — Required**  
Default: No default  
Stock ticker symbol to retrieve option chain data for.

**(8) option_type — Optional**  
Default: both  
Allowed: call, put, both  
Type of options to retrieve.

**(9) date — Optional**  
Default: null  
Specific expiration date used to retrieve option chain data.

---

### JSON input alternatives

```json
{
  "tool": "yahoo-finance_ticker-option-chain",
  "intent": "Retrieve the most recent option chain data for Apple",
  "params": {
    "symbol": "AAPL"
  }
}
```

```json
{
  "tool": "yahoo-finance_ticker-option-chain",
  "intent": "Get put option chain data for Tesla for a specific expiration date",
  "params": {
    "symbol": "TSLA",
    "option_type": "put",
    "date": "2025-01-17"
  }
}
```
