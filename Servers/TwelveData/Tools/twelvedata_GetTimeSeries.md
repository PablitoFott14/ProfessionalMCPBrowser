## twelvedata_GetTimeSeries

### What this tool is for
GetTimeSeries retrieves historical OHLC data over time for a given instrument. It is used when the user needs price evolution across a period, not just the latest value.

In practice, this is the go to tool for analyzing trends, comparing price movements across dates, or feeding data into indicators or strategies.

---

### Used parameters

**(1) symbol — Required**  
Default: No default  
Core identifier of the instrument.

**(5) interval — Optional**  
Default: 1day  
Defines the granularity of the time series (e.g., intraday vs daily).

**(6) outputsize — Optional**  
Default: 10 (or max when using date filters)  
Controls how many data points are returned.

**(7) exchange — Optional**  
Default: null  
Helps specify the trading venue if needed.

**(11) timezone — Optional**  
Default: Exchange  
Controls how datetime values are returned.

**(12) start_date — Optional**  
Default: null  
Defines the beginning of the time range.

**(13) end_date — Optional**  
Default: null  
Defines the end of the time range.

**(14) date — Optional**  
Default: null  
Used to retrieve data for a specific date.

**(15) order — Optional**  
Default: desc  
Controls sorting of the time series.

**(16) prepost — Optional**  
Default: false  
Includes pre market and post market data when applicable.

**(17) format — Optional**  
Default: JSON  
Defines response format.

**(19) dp — Optional**  
Default: -1  
Controls decimal precision (auto by default).

**(20) previous_close — Optional**  
Default: false  
Adds previous close value to each data point.

**(21) adjust — Optional**  
Default: splits  
Controls how prices are adjusted (e.g., splits, dividends).

**(27) apikey — Optional**  
Default: demo  
API authentication key.

---

### JSON input alternatives

```json
{
  "intent": "Analyze recent intraday price trend for a European utility stock",
  "params": {
    "symbol": "IBE",
    "exchange": "BME",
    "interval": "15min",
    "outputsize": 120,
    "timezone": "Europe/Madrid"
  }
}

{
  "intent": "Retrieve forex price movements for a specific date range",
  "params": {
    "symbol": "GBP/NZD",
    "interval": "1h",
    "start_date": "2024-10-01 00:00:00",
    "end_date": "2024-10-03 00:00:00",
    "timezone": "UTC"
  }
}