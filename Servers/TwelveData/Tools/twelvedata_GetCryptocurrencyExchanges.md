## twelvedata_GetCryptocurrencyExchanges

### What this tool is for
GetCryptocurrencyExchanges returns the list of supported cryptocurrency exchanges. It is used when the user needs to discover which exchanges are available before querying crypto pairs, prices, or indicators tied to specific platforms.

---

### Used parameters

**(17) format — Optional**  
Default: JSON  
Allowed: JSON, CSV  
Response format.

**(18) delimiter — Optional**  
Default: ;  
Separator used for CSV output.

**(6) outputsize — Optional**  
Default: 10  
Number of data points to retrieve.

**(27) apikey — Optional**  
Default: demo  
API authentication key.

---

### JSON input alternatives

```json
{
  "tool": "twelvedata_GetCryptocurrencyExchanges",
  "intent": "Retrieve list of available cryptocurrency exchanges",
  "params": {}
}

{
  "tool": "twelvedata_GetCryptocurrencyExchanges",
  "intent": "Retrieve exchanges with extended result size for broader coverage",
  "params": {
    "outputsize": 100
  }
}