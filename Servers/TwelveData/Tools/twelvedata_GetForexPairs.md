## twelvedata_GetForexPairs

### What this tool is for
GetForexPairs returns the list of available forex pairs, including their base and quote currencies. It is used when the user needs to discover available currency pairs or filter them based on specific currencies before performing further analysis.

---

### Used parameters

**(1) symbol — Optional**  
Default: null  
Specific forex pair to filter results.

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
  "tool": "twelvedata_GetForexPairs",
  "intent": "Retrieve all forex pairs with EUR as base currency",
  "params": {
    "currency_base": "EUR"
  }
}

{
  "tool": "twelvedata_GetForexPairs",
  "intent": "Filter forex pairs combining base and quote currencies",
  "params": {
    "currency_base": "AUD",
    "currency_quote": "JPY"
  }
}