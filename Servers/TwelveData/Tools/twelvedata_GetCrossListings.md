## twelvedata_GetCrossListings

### What this tool is for
GetCrossListings returns all cross-listed versions of a given instrument across different exchanges. It is used when the user needs to identify where the same security is traded globally, which is useful for liquidity analysis, arbitrage opportunities, or regional access considerations.

---

### Used parameters

**(1) symbol — Required**  
Default: No default  
The ticker symbol of the instrument.

**(37) exchange — Optional**  
Default: null  
Exchange where the instrument is traded.

**(38) mic_code — Optional**  
Default: null  
Market Identifier Code under ISO 10383.

**(39) country — Optional**  
Default: null  
Country of the exchange.

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
  "intent": "Retrieve cross listings for a major US stock",
  "params": {
    "symbol": "NVDA"
  }
}

{
  "intent": "Filter cross listings by country",
  "params": {
    "symbol": "RDSA",
    "country": "United Kingdom"
  }
}