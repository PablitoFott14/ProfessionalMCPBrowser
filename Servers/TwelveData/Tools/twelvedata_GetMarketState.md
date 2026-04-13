## twelvedata_GetMarketState

### What this tool is for
Returns the current status of stock exchanges, including whether they are open or closed and the time remaining until opening or closing. It is used when the user needs to understand market availability or trading windows, either globally or for a specific exchange.

---

### Used parameters

**(37) exchange — Optional**  
Default: null  
Name of the exchange to filter results.

**(40) code — Optional**  
Default: null  
Market Identifier Code (MIC) of the exchange.

**(39) country — Optional**  
Default: null  
Country where the exchange is located.

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
  "intent": "Check if a major US exchange is currently open",
  "params": {
    "exchange": "NYSE"
  }
}

{
  "intent": "Monitor market state using MIC code with country filtering",
  "params": {
    "code": "XNAS",
    "country": "United States"
  }
}