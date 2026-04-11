## twelvedata_GetSymbolSearch

### What this tool is for
GetSymbolSearch is used to find the correct instrument identifier based on partial inputs like company name, ticker, ISIN, or FIGI. It returns the most relevant matches first, making it useful as a discovery or validation step before calling other tools.

---

### Used parameters

**(1) symbol — Required**  
Default: No default  
Search input, which can be a ticker, company name, ISIN, or FIGI.

**(6) outputsize — Optional**  
Default: 10  
Number of matches returned.

**(41) show_plan — Optional**  
Default: false  
Includes information about plan availability for each symbol.

**(27) apikey — Optional**  
Default: demo  
API authentication key.

---

### JSON input alternatives

```json
{
  "intent": "Search for a company using partial name",
  "params": {
    "symbol": "Siemens"
  }
}

{
  "intent": "Identify instrument using ISIN with extended results",
  "params": {
    "symbol": "US0231351067",
    "outputsize": 20,
    "show_plan": true
  }
}