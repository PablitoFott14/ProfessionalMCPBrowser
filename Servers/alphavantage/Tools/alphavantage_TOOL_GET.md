## alphavantage_TOOL_GET

### What this tool is for
alphavantage_TOOL_GET retrieves the full schema for one or more Alpha Vantage tools, including their parameters. It is useful after `TOOL_LIST` when the user needs the exact inputs for a specific tool before calling it.

---

### Used parameters

**(1) tool_name — Required**  
Default: No default  
Tool name or list of tool names to retrieve schema for.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve the full schema for a specific Alpha Vantage daily time series tool",
  "params": {
    "tool_name": "TIME_SERIES_DAILY"
  }
}

{
  "intent": "Compare the schemas of multiple Alpha Vantage time series tools before choosing one",
  "params": {
    "tool_name": [
      "TIME_SERIES_DAILY",
      "TIME_SERIES_INTRADAY"
    ]
  }
}
```
