## twelvedata_GetDividends

### What this tool is for
GetDividends returns historical dividend payments for an instrument, covering multiple years. It is used when the user needs to analyze income generation, dividend history, or payout consistency of a stock or similar asset.

---

### Used parameters

**(1) symbol — Required**  
Default: No default  
Symbol ticker of the instrument.

**(34) figi — Optional**  
Default: null  
Financial Instrument Global Identifier.

**(35) isin — Optional**  
Default: null  
International Securities Identification Number.

**(36) cusip — Optional**  
Default: null  
CUSIP identifier for the instrument.

**(37) exchange — Optional**  
Default: null  
Exchange where the instrument is traded.

**(38) mic_code — Optional**  
Default: null  
Market Identifier Code under ISO 10383.

**(39) country — Optional**  
Default: null  
Country where the instrument is traded.

**(48) range — Optional**  
Default: last  
Time range for dividend data (e.g., 1y, 5y, full). Takes precedence over dates.

**(12) start_date — Optional**  
Default: null  
Start date for dividend data.

**(13) end_date — Optional**  
Default: null  
End date for dividend data.

**(45) adjust — Optional**  
Default: true  
Specifies whether dividend values should be adjusted.

**(6) outputsize — Optional**  
Default: 10  
Number of data points returned.

**(27) apikey — Optional**  
Default: demo  
API authentication key.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve latest dividend payment for a US stock",
  "params": {
    "symbol": "JNJ",
    "range": "last"
  }
}

{
  "intent": "Analyze dividend history over multiple years",
  "params": {
    "symbol": "PG",
    "range": "5y",
    "adjust": true
  }
}