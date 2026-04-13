## twelvedata_GetQuote

### What this tool is for
Retrieves the latest available market data for a single instrument. It provides a real time snapshot including price, change, volume, and market status, making it the go to option when the user needs current conditions, not historical trends.

---

### Used parameters

**(1) symbol: Required**  
Default: No default  
Core identifier of the instrument to quote.

**(5) interval: Optional**  
Default: 1day  
Controls the interval of the quote returned.

**(7) exchange: Optional**  
Default: null  
Helps disambiguate where the instrument is traded.

**(11) timezone: Optional**  
Default: Exchange  
Controls how output datetime is displayed.

**(17) format: Optional**  
Default: JSON  
Allowed: JSON, CSV  
Sets the response format.

**(19) dp: Optional**  
Default: 5 for this tool  
Sets the number of decimal places in numeric values.

**(28) volume_time_period: Optional**  
Default: 9  
Defines the lookback period used for average volume.

**(29) eod: Optional**  
Default: false  
If enabled, requests data for the closed day.

**(30) rolling_period: Optional**  
Default: 24  
Defines the rolling change period in hours. Especially relevant for crypto outputs.

---

### JSON input alternatives

```json
{
  "intent": "Check current price and market status for a European equity",
  "params": {
    "symbol": "MC",
    "exchange": "EPA"
  }
}

{
  "intent": "Analyze short term crypto performance using rolling change",
  "params": {
    "symbol": "SOL/USD",
    "interval": "1h",
    "rolling_period": 48,
    "timezone": "UTC"
  }
}