## twelvedata_GetTimeSeriesSma

### What this tool is for
GetTimeSeriesSma retrieves the Simple Moving Average over time for a given instrument. It is used to identify trend direction and potential support or resistance levels by smoothing price data over a defined period.

---

### Used parameters

**(1) symbol — Required**  
Default: No default  
Symbol ticker of the instrument.

**(35) isin — Optional**  
Default: null  
International Securities Identification Number.

**(34) figi — Optional**  
Default: null  
Financial Instrument Global Identifier.

**(36) cusip — Optional**  
Default: null  
CUSIP identifier for the instrument.

**(5) interval — Optional**  
Default: 1day  
Defines the timeframe between data points.

**(6) outputsize — Optional**  
Default: 10 (or max with date filters)  
Number of data points returned.

**(37) exchange — Optional**  
Default: null  
Exchange where the instrument is traded.

**(38) mic_code — Optional**  
Default: null  
Market Identifier Code under ISO 10383.

**(39) country — Optional**  
Default: null  
Country where the instrument is traded.

**(42) type — Optional**  
Default: null  
Asset class of the instrument.

**(11) timezone — Optional**  
Default: Exchange  
Controls how datetime values are returned.

**(12) start_date — Optional**  
Default: null  
Start of the analysis window.

**(13) end_date — Optional**  
Default: null  
End of the analysis window.

**(14) date — Optional**  
Default: null  
Retrieves data for a specific date.

**(15) order — Optional**  
Default: desc  
Sorting order of results.

**(43) prepost — Optional**  
Default: false  
Includes pre and post market data.

**(17) format — Optional**  
Default: JSON  
Response format.

**(18) delimiter — Optional**  
Default: ;  
Separator used for CSV output.

**(19) dp — Optional**  
Default: -1  
Decimal precision for numeric values.

**(44) previous_close — Optional**  
Default: false  
Includes previous closing price in the response.

**(45) adjust — Optional**  
Default: splits  
Adjustment mode for price data.

**(22) series_type — Optional**  
Default: close  
Price field used for calculation.

**(31) time_period — Optional**  
Default: 9  
Number of periods used for the moving average.

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
  "intent": "Identify medium term trend for a forex pair",
  "params": {
    "symbol": "EUR/CHF",
    "interval": "1day",
    "time_period": 20
  }
}

{
  "intent": "Short term SMA analysis on a crypto asset with adjusted data",
  "params": {
    "symbol": "LINK/USD",
    "interval": "1h",
    "time_period": 50,
    "adjust": "all",
    "start_date": "2024-08-01 00:00:00",
    "end_date": "2024-08-02 00:00:00",
    "timezone": "UTC"
  }
}