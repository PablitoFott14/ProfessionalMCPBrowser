## twelvedata_GetCommodities

### What this tool is for
Returns the list of available commodity instruments, including their symbols, categories, and descriptions. It is used when the user needs to discover tradable commodities or filter them by type, before performing pricing or indicator analysis.

---

### Used parameters

**(1) symbol — Optional**  
Default: null  
The ticker symbol of a commodity instrument.

**(53) category — Optional**  
Default: null  
Filters commodities by category (e.g., Precious Metal, Energy).

**(17) format — Optional**  
Default: JSON  
Allowed: JSON, CSV  
Response format.

**(18) delimiter — Optional**  
Default: ;  
Separator used for CSV output.

**(6) outputsize — Optional**  
Default: null  
Number of data points to retrieve.

**(27) apikey — Optional**  
Default: demo  
API authentication key.

---

### JSON input alternatives

```json
{
  "tool": "twelvedata_GetCommodities",
  "intent": "Discover all precious metal commodities",
  "params": {
    "category": "Precious Metal"
  }
}

{
  "tool": "twelvedata_GetCommodities",
  "intent": "Retrieve specific commodity pair information",
  "params": {
    "symbol": "XAG/USD"
  }
}