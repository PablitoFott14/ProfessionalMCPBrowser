## twelvedata_GetTimeSeriesAtr

### What this tool is for
Retrieves the Average True Range (ATR) over time, a volatility indicator that measures the average range of price movement. It is used to assess market volatility, helping identify periods of expansion or contraction in price activity.

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
Default: 10  
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
Allowed: asc, desc  
Sorting order of results.

**(43) prepost — Optional**  
Default: false  
Includes pre and post market data.

**(17) format — Optional**  
Default: JSON  
Allowed: JSON, CSV  
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
Allowed: splits, dividends, all  
Adjustment mode for price data.

**(31) time_period — Optional**  
Default: 14  
Number of periods used to calculate ATR.

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
  "tool": "twelvedata_GetTimeSeriesAtr",
  "intent": "Measure daily volatility of a forex pair",
  "params": {
    "symbol": "USD/CAD",
    "interval": "1day",
    "time_period": 14
  }
}

{
  "tool": "twelvedata_GetTimeSeriesAtr",
  "intent": "Intraday volatility analysis on a crypto asset with time window",
  "params": {
    "symbol": "MATIC/USD",
    "interval": "15min",
    "time_period": 21,
    "start_date": "2024-08-10 00:00:00",
    "end_date": "2024-08-10 12:00:00",
    "timezone": "UTC"
  }
}