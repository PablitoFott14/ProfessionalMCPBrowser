## twelvedata_GetLogo

### What this tool is for
GetLogo returns the logo associated with a financial instrument, including stocks, cryptocurrencies, or forex pairs. It is used when the user needs to visually represent an asset, for example in dashboards, reports, or UI components tied to financial data.

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
Country where the instrument is traded.

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
  "intent": "Retrieve logo for a publicly traded company",
  "params": {
    "symbol": "AAPL"
  }
}

{
  "intent": "Retrieve logos for a forex pair with exchange context",
  "params": {
    "symbol": "EUR/USD",
    "exchange": "FX"
  }
}