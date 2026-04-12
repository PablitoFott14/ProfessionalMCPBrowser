## twelvedata_GetStocks

### What this tool is for
GetStocks returns an array of stock symbols available at Twelve Data API. This list is updated daily and is used when the user needs to discover available instruments or filter them by exchange, country, type, or identifier before performing further analysis.

---

### Used parameters

**(1) symbol — Optional**  
Default: null  
The ticker symbol of an instrument to filter results.

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
Filter by exchange name.

**(38) mic_code — Optional**  
Default: null  
Market Identifier Code under ISO 10383.

**(39) country — Optional**  
Default: null  
Filter by country name or alpha code (e.g., United States or US).

**(42) type — Optional**  
Default: null  
Asset class of the instrument (e.g., Common Stock, ETF, REIT).

**(17) format — Optional**  
Default: JSON  
Allowed: JSON, CSV  
Response format.

**(18) delimiter — Optional**  
Default: ;  
Separator used for CSV output.

**(41) show_plan — Optional**  
Default: false  
Adds info on which plan the symbol is available.

**(52) include_delisted — Optional**  
Default: false  
Includes delisted identifiers in the results.

**(6) outputsize — Optional**  
Default: 10  
Number of data points to retrieve.

**(27) apikey — Optional**  
Default: demo  
API authentication key.

---

### JSON input alternatives

```json
{
  "tool": "twelvedata_GetStocks",
  "intent": "Discover stocks listed on a specific exchange",
  "params": {
    "exchange": "NASDAQ",
    "type": "Common Stock"
  }
}

{
  "tool": "twelvedata_GetStocks",
  "intent": "Filter stocks by country including delisted instruments",
  "params": {
    "country": "United States",
    "include_delisted": true,
    "outputsize": 50
  }
}