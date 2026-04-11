## twelvedata_GetCryptocurrencies

### What this tool is for
GetCryptocurrencies returns the list of available cryptocurrency pairs and their supported exchanges. It is used when the user needs to discover available crypto instruments or filter them by base, quote, or exchange before performing further analysis.

---

### Used parameters

**(1) symbol — Optional**  
Default: null  
Specific cryptocurrency pair to filter results.

**(37) exchange — Optional**  
Default: null  
Filters results by exchange (e.g., Binance, Coinbase).

**(46) currency_base — Optional**  
Default: null  
Filters results by base currency.

**(47) currency_quote — Optional**  
Default: null  
Filters results by quote currency.

**(17) format — Optional**  
Default: JSON  
Response format.

**(18) delimiter — Optional**  
Default: ;  
Separator used for CSV output.

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
  "intent": "Discover all crypto pairs with BTC as base currency",
  "params": {
    "currency_base": "BTC"
  }
}

{
  "intent": "Filter crypto pairs by exchange and quote currency",
  "params": {
    "exchange": "Binance",
    "currency_quote": "USDT"
  }
}