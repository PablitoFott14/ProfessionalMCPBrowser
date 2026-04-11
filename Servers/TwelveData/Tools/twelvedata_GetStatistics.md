## twelvedata_GetStatistics

### What this tool is for
GetStatistics returns a snapshot of a company's key financial and valuation metrics, including profitability, margins, debt, valuation ratios, and stock-level statistics. It is used when the user needs a fundamental overview of a company, rather than price movements or technical indicators.

---

### Used parameters

**(1) symbol — Required**  
Default: No default  
Symbol ticker of the instrument.

**(34) figi — Optional**  
Default: null  
Financial Instrument Global Identifier used to uniquely identify the asset.

**(35) isin — Optional**  
Default: null  
International Securities Identification Number of the instrument.

**(36) cusip — Optional**  
Default: null  
CUSIP identifier for the instrument.

**(37) exchange — Optional**  
Default: null  
Exchange where the instrument is traded.

**(38) mic_code — Optional**  
Default: null  
Market Identifier Code following ISO 10383 standard.

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
  "intent": "Fundamental snapshot of a European listed company",
  "params": {
    "symbol": "SAP",
    "exchange": "XETRA"
  }
}

{
  "intent": "Company lookup using ISIN with broader market context",
  "params": {
    "isin": "US5949181045",
    "country": "United States"
  }
}