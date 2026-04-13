## twelvedata_GetFunds

### What this tool is for
Returns the list of available funds, including metadata such as identifiers, exchange, and classification. It is used when the user needs to discover funds or filter them based on identifiers, geography, or exchange before deeper financial analysis.

---

### Used parameters

**(1) symbol: Optional**  
Default: null  
The ticker symbol of an instrument.

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
Exchange where the fund is traded.

**(39) country: Optional**  
Default: null  
Country where the fund is located.

**(17) format: Optional**  
Default: JSON  
Allowed: JSON, CSV  
Response format.

**(18) delimiter: Optional**  
Default: ;  
Separator used for CSV output.

**(41) show_plan: Optional**  
Default: false  
Includes plan availability information.

**(54) page: Optional**  
Default: 1  
Page number of the results to fetch.

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
  "intent": "Discover funds available in the US",
  "params": {
    "country": "United States"
  }
}

{
  "intent": "Retrieve funds from a specific exchange with pagination",
  "params": {
    "exchange": "NYSE",
    "page": 2
  }
}