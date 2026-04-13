## twelvedata_GetTimeSeriesMacd

### What this tool is for
Retrieves the MACD indicator over time for a given instrument. It is used when the user wants to analyze momentum and potential trend reversals, rather than raw price data.

---

### Used parameters

**(1) symbol — Required**  
Default: No default  
Core identifier of the instrument.

**(5) interval — Optional**  
Default: 1day  
Defines the timeframe for MACD calculation.

**(6) outputsize — Optional**  
Default: 10 (or max with date filters)  
Controls how many indicator points are returned.

**(11) timezone — Optional**  
Default: Exchange  
Controls datetime output.

**(12) start_date — Optional**  
Default: null  
Defines the beginning of the analysis window.

**(13) end_date — Optional**  
Default: null  
Defines the end of the analysis window.

**(15) order — Optional**  
Default: desc  
Allowed: asc, desc  
Controls sorting of results.

**(17) format — Optional**  
Default: JSON  
Allowed: JSON, CSV  
Defines response format.

**(19) dp — Optional**  
Default: -1  
Controls decimal precision.

**(22) series_type — Optional**  
Default: close  
Allowed: close, open, high, low  
Defines which price field is used for MACD calculation.

**(23) fast_period — Optional**  
Default: 12  
Fast moving average period.

**(24) slow_period — Optional**  
Default: 26  
Slow moving average period.

**(25) signal_period — Optional**  
Default: 9  
Signal line period.

**(26) include_ohlc — Optional**  
Default: false  
Adds OHLC values alongside indicator output.

**(27) apikey — Optional**  
Default: demo  
API authentication key.

---

### JSON input alternatives

```json
{
  "tool": "twelvedata_GetTimeSeriesMacd",
  "intent": "Analyze medium term momentum for a European bank",
  "params": {
    "symbol": "SAN",
    "exchange": "BME",
    "outputsize": 100
  }
}

{
  "tool": "twelvedata_GetTimeSeriesMacd",
  "intent": "Analyze short term signal for a crypto asset",
  "params": {
    "symbol": "AVAX/USD",
    "interval": "1h",
    "fast_period": 10,
    "slow_period": 30,
    "signal_period": 8,
    "timezone": "UTC"
  }
}