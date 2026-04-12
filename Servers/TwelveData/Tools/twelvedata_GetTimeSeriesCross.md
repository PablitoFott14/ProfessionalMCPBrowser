## twelvedata_GetTimeSeriesCross

### What this tool is for
GetTimeSeriesCross returns time series data for a cross between two instruments, including OHLC values. It is used when the user needs to analyze price relationships between two assets, such as forex pairs, crypto crosses, or synthetic comparisons across markets.

---

### Used parameters

**(55) base — Required**  
Default: No default  
Base instrument or currency.

**(56) quote — Required**  
Default: No default  
Quote instrument or currency.

**(57) base_type — Optional**  
Default: null  
Type of the base instrument.

**(58) base_exchange — Optional**  
Default: null  
Exchange of the base instrument.

**(59) base_mic_code — Optional**  
Default: null  
MIC code of the base instrument.

**(60) quote_type — Optional**  
Default: null  
Type of the quote instrument.

**(61) quote_exchange — Optional**  
Default: null  
Exchange of the quote instrument.

**(62) quote_mic_code — Optional**  
Default: null  
MIC code of the quote instrument.

**(5) interval — Optional**  
Default: null  
Interval between data points.

**(6) outputsize — Optional**  
Default: null  
Number of data points to retrieve.

**(17) format — Optional**  
Default: null  
Response format.

**(18) delimiter — Optional**  
Default: null  
Separator used for CSV output.

**(43) prepost — Optional**  
Default: null  
Includes pre and post market data.

**(12) start_date — Optional**  
Default: null  
Start date for the time series.

**(13) end_date — Optional**  
Default: null  
End date for the time series.

**(45) adjust — Optional**  
Default: null  
Allowed: splits, dividends, all  
Specifies whether data should be adjusted.

**(19) dp — Optional**  
Default: null  
Decimal precision for numeric values.

**(11) timezone — Optional**  
Default: null  
Timezone used for the returned datetime.

**(27) apikey — Optional**  
Default: demo  
API authentication key.

---

### JSON input alternatives

```json
{
  "tool": "twelvedata_GetTimeSeriesCross",
  "intent": "Analyze forex cross between two major currencies",
  "params": {
    "base": "EUR",
    "quote": "JPY",
    "interval": "1day"
  }
}

{
  "tool": "twelvedata_GetTimeSeriesCross",
  "intent": "Crypto cross analysis with exchange specific context",
  "params": {
    "base": "ETH",
    "quote": "BTC",
    "base_exchange": "Binance",
    "quote_exchange": "Coinbase",
    "interval": "1h",
    "start_date": "2024-08-01 00:00:00",
    "end_date": "2024-08-02 00:00:00",
    "timezone": "UTC"
  }
}