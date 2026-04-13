## twelvedata_GetIpoCalendar

### What this tool is for
Returns past, current, or upcoming IPO events, including company details and pricing ranges. It is used when the user needs to track new market listings, analyze IPO pipelines, or review historical IPO activity.

---

### Used parameters

**(37) exchange: Optional**  
Default: null  
Exchange where the company is listed.

**(38) mic_code: Optional**  
Default: null  
Market Identifier Code under ISO 10383.

**(39) country: Optional**  
Default: null  
Country where the IPO is taking place.

**(12) start_date: Optional**  
Default: null  
The earliest IPO date to include.

**(13) end_date: Optional**  
Default: null  
The latest IPO date to include.

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
  "intent": "Retrieve upcoming IPOs in the US",
  "params": {
    "country": "United States"
  }
}

{
  "intent": "Analyze IPO activity on a specific exchange within a time window",
  "params": {
    "exchange": "NASDAQ",
    "start_date": "2024-01-01",
    "end_date": "2024-06-30"
  }
}