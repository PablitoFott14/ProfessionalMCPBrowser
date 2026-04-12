## twelvedata_GetEtf

### What this tool is for
GetEtf returns the list of available ETFs along with their metadata, including identifiers, exchange, and classification. It is used when the user needs to discover ETFs or filter them based on identifiers, exchange, or geography before deeper analysis.

---

### Used parameters

**(1) symbol — Optional**  
Default: null  
The ticker symbol of an instrument.

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
Exchange where the ETF is traded.

**(38) mic_code — Optional**  
Default: null  
Market Identifier Code under ISO 10383.

**(39) country — Optional**  
Default: null  
Country where the ETF is located.

**(17) format — Optional**  
Default: null  
Allowed: JSON, CSV  
Response format.

**(18) delimiter — Optional**  
Default: null  
Separator used for CSV output.

**(41) show_plan — Optional**  
Default: null  
Includes plan availability information.

**(52) include_delisted — Optional**  
Default: null  
Includes delisted ETF identifiers in the results.

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
  "tool": "twelvedata_GetEtf",
  "intent": "Discover ETFs listed in the US",
  "params": {
    "country": "United States"
  }
}

{
  "tool": "twelvedata_GetEtf",
  "intent": "Filter ETFs by exchange including delisted instruments",
  "params": {
    "exchange": "NYSE",
    "include_delisted": true
  }
}