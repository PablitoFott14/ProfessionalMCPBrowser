## twelvedata_GetProfile

### What this tool is for
Returns general company information, including sector, industry, leadership, and business description. It is used when the user needs a qualitative overview of a company, rather than financial metrics or price data.

---

### Used parameters

**(1) symbol — Required**  
Default: No default  
Symbol ticker of the instrument.

**(34) figi — Optional**  
Default: null  
Financial Instrument Global Identifier used to identify the asset.

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

**(6) outputsize — Optional**  
Default: 10 (or max with date filters)  
Number of data points returned.

**(27) apikey — Optional**  
Default: demo  
API authentication key.

---

### JSON input alternatives

```json
{
  "tool": "twelvedata_GetProfile",
  "intent": "Retrieve general company profile for a European industrial firm",
  "params": {
    "symbol": "SIE",
    "exchange": "XETRA"
  }
}

{
  "tool": "twelvedata_GetProfile",
  "intent": "Identify company using FIGI with geographic filtering",
  "params": {
    "figi": "BBG000BLNNH6",
    "country": "Germany"
  }
}