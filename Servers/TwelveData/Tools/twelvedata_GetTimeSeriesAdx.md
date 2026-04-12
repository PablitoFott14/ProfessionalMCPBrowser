## twelvedata_GetTimeSeriesAdx

### What this tool is for
GetTimeSeriesAdx returns the Average Directional Index (ADX) over time, a technical indicator used to measure the strength of a trend regardless of direction. It is commonly used to determine whether a market is trending or ranging before applying directional strategies.

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
Default: null  
Interval between data points.

**(6) outputsize — Optional**  
Default: null  
Number of data points to retrieve.

**(37) exchange — Optional**  
Default: null  
Exchange where instrument is traded.

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
Default: null  
Timezone used for the returned datetime.

**(12) start_date — Optional**  
Default: null  
Start date for the time series.

**(13) end_date — Optional**  
Default: null  
End date for the time series.

**(14) date — Optional**  
Default: null  
Specific date to retrieve data for.

**(15) order — Optional**  
Default: null  
Allowed: asc, desc  
Sorting order of the output.

**(43) prepost — Optional**  
Default: null  
Includes pre and post market data.

**(17) format — Optional**  
Default: null  
Allowed: JSON, CSV  
Response format.

**(18) delimiter — Optional**  
Default: null  
Separator used for CSV output.

**(19) dp — Optional**  
Default: null  
Decimal precision for numeric values.

**(44) previous_close — Optional**  
Default: null  
Includes previous closing price in the response.

**(45) adjust — Optional**  
Default: null  
Allowed: splits, dividends, all  
Specifies whether data should be adjusted.

**(31) time_period — Optional**  
Default: null  
Number of periods used to calculate ADX.

**(26) include_ohlc — Optional**  
Default: null  
Adds OHLC values to the response.

**(27) apikey — Optional**  
Default: demo  
API authentication key.

---

### JSON input alternatives

```json
{
  "tool": "twelvedata_GetTimeSeriesAdx",
  "intent": "Evaluate trend strength for a US equity",
  "params": {
    "symbol": "MSFT",
    "interval": "1day",
    "time_period": 14
  }
}

{
  "tool": "twelvedata_GetTimeSeriesAdx",
  "intent": "Intraday trend strength analysis for a crypto pair",
  "params": {
    "symbol": "SOL/USD",
    "interval": "15min",
    "time_period": 20,
    "start_date": "2024-08-20 00:00:00",
    "end_date": "2024-08-20 12:00:00",
    "timezone": "UTC"
  }
}