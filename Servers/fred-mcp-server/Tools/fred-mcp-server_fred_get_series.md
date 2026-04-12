## fred-mcp-server_fred_get_series

### What this tool is for
Retrieves data for a specific FRED series by its ID, with optional date ranges, transformations, frequency changes, and output settings. Use this when the user already knows the series ID and needs the actual observations.

---

### Used parameters

**(11) series_id - Required**  
Default: No default  
FRED series identifier used to retrieve the data.

**(12) observation_start - Optional**  
Default: No default  
Start date used to limit returned observations.

**(13) observation_end - Optional**  
Default: No default  
End date used to limit returned observations.

**(5) limit - Optional**  
Default: No default  
Maximum number of observations to return.

**(6) offset - Optional**  
Default: No default  
Number of observations to skip.

**(8) sort_order - Optional**  
Default: No default  
Sort order of observations by date.

**(14) units - Optional**  
Default: No default  
Data transformation applied to the returned values.

**(15) frequency - Optional**  
Default: No default  
Frequency aggregation applied to the returned observations.

**(16) aggregation_method - Optional**  
Default: No default  
Aggregation method used when changing the observation frequency.

**(17) output_type - Optional**  
Default: No default  
Output format used for the returned observations.

**(18) vintage_dates - Optional**  
Default: No default  
Vintage date or dates used for vintage-aware retrieval.

---

### JSON input alternatives

```json
{
  "tool": "fred-mcp-server_fred_get_series",
  "intent": "Retrieve GDP observations from 2015 onward",
  "params": {
    "series_id": "GDP",
    "observation_start": "2015-01-01"
  }
}
```

```json
{
  "tool": "fred-mcp-server_fred_get_series",
  "intent": "Retrieve recent CPI percent changes in descending date order",
  "params": {
    "series_id": "CPIAUCSL",
    "units": "pch",
    "sort_order": "desc",
    "limit": 24
  }
}
```
