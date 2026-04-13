## twelvedata_GetTimeSeriesEma

### What this tool is for
Retrieves the Exponential Moving Average over time for a given instrument. It is used to track trend direction with higher sensitivity to recent price changes, making it useful for identifying momentum shifts and potential entry or exit points.

---

### Used parameters

**(1) symbol — Required**  
Default: No default  
Instrument identifier.

**(5) interval — Optional**  
Default: 1day  
Defines the timeframe of the EMA.

**(6) outputsize — Optional**  
Default: 10 (or max with date filters)  
Number of data points returned.

**(11) timezone — Optional**  
Default: Exchange  
Controls how datetime values are returned.

**(12) start_date — Optional**  
Default: null  
Start of the analysis window.

**(13) end_date — Optional**  
Default: null  
End of the analysis window.

**(15) order — Optional**  
Default: desc  
Allowed: asc, desc  
Sorting order of results.

**(17) format — Optional**  
Default: JSON  
Allowed: JSON, CSV  
Response format.

**(19) dp — Optional**  
Default: -1  
Decimal precision for numeric values.

**(22) series_type — Optional**  
Default: close  
Allowed: close, open, high, low  
Price field used for calculation.

**(31) time_period — Optional**  
Default: 9  
Number of periods used to calculate the EMA.

**(26) include_ohlc — Optional**  
Default: false  
Adds OHLC values to the response.

**(27) apikey — Optional**  
Default: demo  
API authentication key.

---

### JSON input alternatives

```json
{
  "intent": "Short term trend check on a forex pair",
  "params": {
    "symbol": "GBP/JPY",
    "interval": "1day"
  }
}

{
  "intent": "Crypto momentum analysis with custom EMA window and timeframe",
  "params": {
    "symbol": "ADA/USD",
    "interval": "1h",
    "time_period": 21,
    "series_type": "close",
    "start_date": "2024-09-01 00:00:00",
    "end_date": "2024-09-02 12:00:00",
    "timezone": "UTC"
  }
}