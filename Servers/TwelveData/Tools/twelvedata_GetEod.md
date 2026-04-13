## twelvedata_GetEod

### What this tool is for
Returns the latest end-of-day (EOD) price for an instrument. It is used when the user needs the most recent official closing price, typically for reporting, valuation, or daily performance tracking.

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

**(42) type: Optional**  
Default: null  
Asset class of the instrument (e.g., ETF, Common Stock, Digital Currency).

**(14) date: Optional**  
Default: null  
Retrieves EOD price for a specific date.

**(43) prepost: Optional**  
Default: false  
Includes pre and post market data for supported intervals.

**(19) dp: Optional**  
Default: 5  
Decimal precision for returned values.

**(6) outputsize: Optional**  
Default: 10 (or max with date filters)  
Number of data points returned.

**(27) apikey: Optional**  
Default: demo  
API authentication key.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve latest closing price for a US stock",
  "params": {
    "symbol": "MSFT"
  }
}

{
  "intent": "Historical EOD price for a crypto asset with precision control",
  "params": {
    "symbol": "SOL/USD",
    "date": "2024-08-15",
    "dp": 6,
    "type": "Digital Currency"
  }
}