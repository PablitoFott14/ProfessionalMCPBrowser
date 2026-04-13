## octagon-mcp_prediction_markets_history

### What this tool is for
Historical data for a prediction market event by its event ticker. Use this when the user needs historical records for a specific prediction market, optionally with pagination, a bounded time window, or analysis fields included.

---

### Used parameters

**(2) event_ticker - Required**  
Default: No default  
Event ticker used to identify the prediction market event.

**(3) limit - Optional**  
Default: null  
Maximum number of history records to return.

**(4) cursor - Optional**  
Default: null  
Pagination cursor used to continue from a previous response.

**(5) captured_from - Optional**  
Default: null  
Start of the historical window used to filter records.

**(6) captured_to - Optional**  
Default: null  
End of the historical window used to filter records.

**(7) include_analysis - Optional**  
Default: null  
Flag indicating whether analysis columns should be included.

---

### JSON input alternatives

```json
{
  "tool": "octagon-mcp_prediction_markets_history",
  "intent": "Retrieve recent history for a specific prediction market event",
  "params": {
    "event_ticker": "KXBTCY-27JAN0100"
  }
}
```

```json
{
  "tool": "octagon-mcp_prediction_markets_history",
  "intent": "Retrieve a bounded historical window for a prediction market event with analysis columns",
  "params": {
    "event_ticker": "KXBTCY-27JAN0100",
    "captured_from": "2025-01-01T00:00:00Z",
    "captured_to": "2025-01-31T23:59:59Z",
    "limit": 100,
    "include_analysis": true
  }
}
```
