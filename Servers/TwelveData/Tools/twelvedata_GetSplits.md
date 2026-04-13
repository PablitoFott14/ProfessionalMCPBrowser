## twelvedata_GetSplits

### What this tool is for
Returns historical stock split events, including split ratios and dates. It is used when the user needs to understand how share structure has changed over time, which is key for adjusting historical price analysis or interpreting long term performance.

---

### Used parameters

**(1) symbol: Required**  
Default: No default  
Symbol ticker of the instrument.

**(34) figi: Optional**  
Default: null  
Financial Instrument Global Identifier.

**(35) isin: Optional**  
Default: null  
International Securities Identification Number.

**(36) cusip: Optional**  
Default: null  
CUSIP identifier for the instrument.

**(37) exchange: Optional**  
Default: null  
Exchange where the instrument is traded.

**(38) mic_code: Optional**  
Default: null  
Market Identifier Code under ISO 10383.

**(39) country: Optional**  
Default: null  
Country where the instrument is traded.

**(48) range: Optional**  
Default: last  
Range of data to be returned (e.g., last, 1y, 5y, full).

**(12) start_date: Optional**  
Default: null  
The starting date for data selection.

**(13) end_date: Optional**  
Default: null  
The ending date for data selection.

**(6) outputsize: Optional**  
Default: 10  
Number of data points to retrieve.

**(27) apikey: Optional**  
Default: demo  
API authentication key.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve latest available split data",
  "params": {
    "symbol": "TSLA"
  }
}

{
  "intent": "Analyze full split history for long term adjustments",
  "params": {
    "symbol": "AAPL",
    "range": "full"
  }
}