## twelvedata_GetTimeSeriesBBands

### What this tool is for
Retrieves Bollinger Bands over time for a given instrument. It is used to assess volatility and potential overbought or oversold conditions by comparing price against dynamic upper and lower bands.

---

### Used parameters

**(1) symbol — Required**  
Default: No default  
Instrument identifier.

**(5) interval — Optional**  
Default: 1day  
Defines the timeframe of the indicator.

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
Default: 20  
Number of periods used for the moving average.

**(32) sd — Optional**  
Default: 2  
Number of standard deviations used to build the bands.

**(33) ma_type — Optional**  
Default: SMA  
Type of moving average applied.

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
  "intent": "Assess volatility for a forex pair",
  "params": {
    "symbol": "EUR/GBP",
    "interval": "1day"
  }
}

{
  "intent": "Analyze Bollinger Bands for a crypto asset with custom settings and date range",
  "params": {
    "symbol": "ETH/USD",
    "interval": "1h",
    "time_period": 50,
    "sd": 2.5,
    "ma_type": "EMA",
    "start_date": "2024-09-01 00:00:00",
    "end_date": "2024-09-03 00:00:00",
    "timezone": "UTC"
  }
}