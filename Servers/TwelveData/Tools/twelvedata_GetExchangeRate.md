## twelvedata_GetExchangeRate

### What this tool is for
Retrieves the real-time exchange rate for a currency pair, including both forex and cryptocurrencies. It is used when the user needs a direct conversion rate at a given moment, rather than time series or indicator data.

---

### Used parameters

**(1) symbol — Required**  
Default: No default  
Currency pair in BASE/QUOTE format (e.g., EUR/USD, BTC/ETH).

**(14) date — Optional**  
Default: null  
Retrieves the exchange rate at a specific date or time.

**(17) format — Optional**  
Default: JSON  
Allowed: JSON, CSV  
Response format.

**(18) delimiter — Optional**  
Default: ;  
Separator used when requesting CSV output.

**(19) dp — Optional**  
Default: 5  
Decimal precision for the returned rate.

**(11) timezone — Optional**  
Default: null  
Controls how datetime is interpreted and returned.

**(6) outputsize — Optional**  
Default: 10 (or max with date filters)  
Number of data points returned.

**(27) apikey — Optional**  
Default: demo  
API authentication key.

---

### JSON input alternatives

```json
{
  "tool": "twelvedata_GetExchangeRate",
  "intent": "Quick check of current forex rate",
  "params": {
    "symbol": "EUR/USD"
  }
}

{
  "tool": "twelvedata_GetExchangeRate",
  "intent": "Retrieve crypto pair rate at a specific moment with controlled precision",
  "params": {
    "symbol": "BTC/ETH",
    "date": "2024-09-01 12:00:00",
    "dp": 6,
    "timezone": "UTC"
  }
}