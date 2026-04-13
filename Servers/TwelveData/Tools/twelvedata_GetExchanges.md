## twelvedata_GetExchanges

### What this tool is for
Returns the list of available stock and ETF exchanges, including metadata such as country, MIC code, and timezone. It is used when the user needs to discover or validate exchanges before querying instruments or market data.

---

### Used parameters

**(42) type — Optional**  
Default: null  
Filters exchanges by asset class (e.g., ETF, Common Stock).

**(51) name — Optional**  
Default: null  
Filters results by exchange name.

**(40) code — Optional**  
Default: null  
Market Identifier Code (MIC) of the exchange.

**(39) country — Optional**  
Default: null  
Filters exchanges by country.

**(17) format — Optional**  
Default: JSON  
Allowed: JSON, CSV  
Response format.

**(18) delimiter — Optional**  
Default: ;  
Separator used for CSV output.

**(41) show_plan — Optional**  
Default: false  
Includes plan availability information.

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
  "tool": "twelvedata_GetExchanges",
  "intent": "Retrieve exchanges for US stock markets",
  "params": {
    "country": "United States",
    "type": "Common Stock"
  }
}

{
  "tool": "twelvedata_GetExchanges",
  "intent": "Find exchange using MIC code with plan visibility",
  "params": {
    "code": "XNGS",
    "show_plan": true
  }
}