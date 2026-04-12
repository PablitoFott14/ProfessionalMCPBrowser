## akshare-one-mcp_get_hist_data

### What this tool is for
akshare-one-mcp_get_hist_data retrieves historical market data for a stock across multiple time intervals. It is useful when the user needs price history for charting, trend analysis, backtesting, or for adding technical indicators to the same series.

It is also the main history tool for switching between supported data sources, including `eastmoney_direct` for broader A, B, and H share coverage.

---

### Used parameters

**(1) symbol — Required**  
Default: No default  
Stock symbol or ticker to retrieve history for.

**(2) interval — Optional**  
Default: day  
Sets the time resolution of the returned series.

**(3) interval_multiplier — Optional**  
Default: 1  
Expands the selected interval into larger bars.

**(4) start_date — Optional**  
Default: 1970-01-01  
Defines the beginning of the requested date range.

**(5) end_date — Optional**  
Default: 2030-12-31  
Defines the end of the requested date range.

**(6) adjust — Optional**  
Default: none  
Controls whether the series uses adjusted prices.

**(7) source — Optional**  
Default: eastmoney  
Chooses which market data source is used.

**(8) indicators_list — Optional**  
Default: null  
Adds selected technical indicators to the historical series.

**(9) recent_n — Optional**  
Default: 100  
Limits the output to the most recent records.

---

### JSON input alternatives

```json
{
  "intent": "Review the most recent adjusted daily history for a mainland China stock",
  "params": {
    "symbol": "000001",
    "adjust": "qfq",
    "recent_n": 60
  }
}

{
  "intent": "Analyze a shorter hourly window with technical indicators for a Hong Kong listed stock",
  "params": {
    "symbol": "00700",
    "interval": "hour",
    "start_date": "2024-09-01",
    "end_date": "2024-09-20",
    "source": "eastmoney_direct",
    "indicators_list": [
      "SMA",
      "MACD",
      "RSI"
    ],
    "recent_n": 80
  }
}
```
