## twelvedata_GetPrice

### What this tool is for
GetPrice returns the real-time price of a single instrument. It is a lightweight endpoint used when the user needs just the latest price without any additional time series or indicator data, making it ideal for dashboards, quick checks, or triggering logic.

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

**(17) format — Optional**  
Default: null  
Output format.

**(18) delimiter — Optional**  
Default: null  
Separator used for CSV output.

**(43) prepost — Optional**  
Default: null  
Includes pre and post market data.

**(19) dp — Optional**  
Default: null  
Decimal precision for numeric values.

**(6) outputsize — Optional**  
Default: null  
Number of data points to retrieve.

**(27) apikey — Optional**  
Default: demo  
API authentication key.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve real-time price for a US stock",
  "params": {
    "symbol": "GOOGL"
  }
}

{
  "intent": "Retrieve crypto price with exchange context and precision",
  "params": {
    "symbol": "ADA/USD",
    "exchange": "Binance",
    "dp": 6
  }
}