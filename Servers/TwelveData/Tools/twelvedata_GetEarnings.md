## twelvedata_GetEarnings

### What this tool is for
GetEarnings returns historical and upcoming earnings data, including EPS estimates and actual results. It is used when the user needs to analyze company performance, earnings surprises, or upcoming earnings events.

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

**(42) type — Optional**  
Default: null  
Asset class of the instrument.

**(49) period — Optional**  
Default: null  
Specifies type of earnings to retrieve (e.g., latest, next). Overrides dates and outputsize.

**(6) outputsize — Optional**  
Default: 10  
Number of data points returned.

**(17) format — Optional**  
Default: JSON  
Allowed: JSON, CSV  
Response format.

**(18) delimiter — Optional**  
Default: ;  
Separator used for CSV output.

**(12) start_date — Optional**  
Default: null  
Start date for earnings data.

**(13) end_date — Optional**  
Default: null  
End date for earnings data.

**(19) dp — Optional**  
Default: 2  
Decimal precision for numeric values.

**(27) apikey — Optional**  
Default: demo  
API authentication key.

---

### JSON input alternatives

```json
{
  "tool": "twelvedata_GetEarnings",
  "intent": "Retrieve latest earnings for a US company",
  "params": {
    "symbol": "NVDA",
    "period": "latest"
  }
}

{
  "tool": "twelvedata_GetEarnings",
  "intent": "Analyze earnings history within a defined time window",
  "params": {
    "symbol": "ASML",
    "start_date": "2023-01-01",
    "end_date": "2024-01-01",
    "outputsize": 50
  }
}