## twelvedata_GetTimeSeriesRsi

### What this tool is for
Retrieves the Relative Strength Index (RSI) over time for a given instrument. It is a momentum oscillator that measures the speed and change of price movements, helping traders identify potential overbought or oversold conditions and trend reversals.

---

### Used parameters

**(1) symbol: Required**  
Default: No default  
Symbol ticker of the instrument.

**(35) isin: Optional**  
Default: null  
International Securities Identification Number.

**(34) figi: Optional**  
Default: null  
Financial Instrument Global Identifier.

**(36) cusip: Optional**  
Default: null  
CUSIP identifier for the instrument.

**(5) interval: Optional**  
Default: 1day  
Defines the timeframe between data points.

**(6) outputsize: Optional**  
Default: 10 (or max with date filters)  
Number of data points returned.

**(7) exchange: Optional**  
Default: null  
Exchange where the instrument is traded.

**(8) mic_code: Optional**  
Default: null  
Market Identifier Code under ISO 10383.

**(9) country: Optional**  
Default: null  
Country where the instrument is traded.

**(10) type: Optional**  
Default: null  
Asset class of the instrument.

**(11) timezone: Optional**  
Default: Exchange  
Controls how datetime values are returned.

**(12) start_date: Optional**  
Default: null  
Start of the analysis window.

**(13) end_date: Optional**  
Default: null  
End of the analysis window.

**(14) date: Optional**  
Default: null  
Retrieves data for a specific date.

**(15) order: Optional**  
Default: desc  
Allowed: asc, desc  
Sorting order of results.

**(16) prepost: Optional**  
Default: false  
Includes pre and post market data.

**(17) format: Optional**  
Default: JSON  
Allowed: JSON, CSV  
Response format.

**(18) delimiter: Optional**  
Default: ;  
Separator used for CSV output.

**(19) dp: Optional**  
Default: -1  
Decimal precision for numeric values.

**(20) previous_close: Optional**  
Default: false  
Includes previous closing price in the response.

**(21) adjust: Optional**  
Default: splits  
Allowed: splits, dividends, all  
Adjustment mode for price data.

**(22) series_type: Optional**  
Default: close  
Allowed: close, open, high, low  
Price field used for RSI calculation.

**(31) time_period: Optional**  
Default: 14  
Number of periods used to calculate RSI.

**(26) include_ohlc: Optional**  
Default: false  
Adds OHLC values to the response.

**(27) apikey: Optional**  
Default: demo  
API authentication key.

---

### JSON input alternatives

```json
{
  "intent": "Check overbought or oversold conditions for a US equity",
  "params": {
    "symbol": "AAPL",
    "interval": "1day",
    "time_period": 14
  }
}

{
  "intent": "Intraday RSI momentum analysis for a crypto asset with custom window",
  "params": {
    "symbol": "ETH/USD",
    "interval": "1h",
    "time_period": 21,
    "start_date": "2024-09-01 00:00:00",
    "end_date": "2024-09-02 00:00:00",
    "timezone": "UTC"
  }
}