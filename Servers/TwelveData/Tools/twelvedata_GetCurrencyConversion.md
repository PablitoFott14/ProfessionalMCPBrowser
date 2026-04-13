## twelvedata_GetCurrencyConversion

### What this tool is for
Returns the real-time exchange rate along with the converted amount for a given currency pair. It is used when the user needs to directly convert a specific amount between currencies, rather than just retrieving the rate.

---

### Used parameters

**(1) symbol — Required**  
Default: No default  
Currency pair in BASE/QUOTE format (e.g., EUR/USD, BTC/ETH).

**(50) amount — Required**  
Default: No default  
Amount of base currency to convert into the quote currency.

**(14) date — Optional**  
Default: null  
Retrieves conversion using a specific historical date or time.

**(17) format — Optional**  
Default: JSON  
Allowed: JSON, CSV  
Response format.

**(18) delimiter — Optional**  
Default: ;  
Separator used for CSV output.

**(19) dp — Optional**  
Default: 5  
Decimal precision for the result.

**(11) timezone — Optional**  
Default: null  
Controls how datetime is interpreted and returned.

**(6) outputsize — Optional**  
Default: 10  
Number of data points returned.

**(27) apikey — Optional**  
Default: demo  
API authentication key.

---

### JSON input alternatives

```json
{
  "tool": "twelvedata_GetCurrencyConversion",
  "intent": "Convert a fixed amount from EUR to USD",
  "params": {
    "symbol": "EUR/USD",
    "amount": 250
  }
}

{
  "tool": "twelvedata_GetCurrencyConversion",
  "intent": "Convert crypto amount using historical rate and timezone",
  "params": {
    "symbol": "ETH/BTC",
    "amount": 3.5,
    "date": "2024-08-01 12:00:00",
    "timezone": "UTC",
    "dp": 6
  }
}