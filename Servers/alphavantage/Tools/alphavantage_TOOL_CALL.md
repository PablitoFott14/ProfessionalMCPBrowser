## alphavantage_TOOL_CALL

### What this tool is for
An Alpha Vantage tool by name using the provided arguments. It is useful after `TOOL_GET` when the user already knows the exact schema and is ready to make the actual tool call.

---

### Used parameters

**(1) tool_name — Required**  
Default: No default  
The name of the tool to execute.

**(2) arguments — Required**  
Default: No default  
Dictionary of arguments matching the selected tool's parameter schema.

---

### JSON input alternatives

```json
{
  "intent": "Call a daily time series tool after confirming its schema",
  "params": {
    "tool_name": "TIME_SERIES_DAILY",
    "arguments": {
      "symbol": "IBM"
    }
  }
}

{
  "intent": "Execute an intraday time series request with a specific interval after schema review",
  "params": {
    "tool_name": "TIME_SERIES_INTRADAY",
    "arguments": {
      "symbol": "MSFT",
      "interval": "5min"
    }
  }
}
```
