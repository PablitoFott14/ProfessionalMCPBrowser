## twelvedata_GetEarliestTimestamp

### What this tool is for
Returns the first available datetime for an instrument at a given interval. It is used when the user needs to understand how far back data is available, which is especially useful before running time series or indicator analysis.

---

### Used parameters

**(1) symbol — Required**  
Default: No default  
Symbol ticker of the instrument.

**(34) figi — Optional**  
Default: null  
Financial Instrument Global Identifier.

**(35) isin — Optional**  
Default: null  
International Securities Identification Number.

**(36) cusip — Optional**  
Default: null  
CUSIP identifier for the instrument.

**(5) interval — Optional**  
Default: 1day  
Interval between data points.

**(37) exchange — Optional**  
Default: null  
Exchange where the instrument is traded.

**(38) mic_code — Optional**  
Default: null  
Market Identifier Code under ISO 10383.

**(11) timezone — Optional**  
Default: Exchange  
Timezone used for the returned datetime.

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
  "intent": "Check earliest available data for a stock",
  "params": {
    "symbol": "IBM"
  }
}

{
  "intent": "Validate historical coverage for intraday crypto analysis",
  "params": {
    "symbol": "LTC/USD",
    "interval": "1h",
    "timezone": "UTC"
  }
}