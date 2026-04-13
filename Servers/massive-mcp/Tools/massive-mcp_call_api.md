## massive-mcp_call_api

### What this tool is for
Financial market data from a selected API endpoint path and optionally stores or post-processes the results. Use this after discovering an endpoint and reviewing its documentation, when the user is ready to make the actual data request.

---

### Used parameters

**(4) method - Required**  
Default: No default  
Allowed: GET  
HTTP method used for the request.

**(5) path - Required**  
Default: No default  
API endpoint path used to request data.

**(6) params - Optional**  
Default: null  
Query parameters passed with the API request.

**(7) store_as - Optional**  
Default: null  
Table name used to store the results for later querying.

**(8) apply - Optional**  
Default: null  
List of post-processing function steps to apply to the returned results.

**(9) api_key - Optional**  
Default: null  
API key override used for this request.

---

### JSON input alternatives

```json
{
  "intent": "Fetch daily aggregate data for AAPL over January 2024",
  "params": {
    "method": "GET",
    "path": "/v2/aggs/ticker/AAPL/range/1/day/2024-01-01/2024-01-31"
  }
}
```

```json
{
  "intent": "Fetch aggregate data, store it for later querying, and apply a post-processing function",
  "params": {
    "method": "GET",
    "path": "/v2/aggs/ticker/AAPL/range/1/day/2024-01-01/2024-01-31",
    "params": {
      "adjusted": true
    },
    "store_as": "prices",
    "apply": [
      {
        "function": "returns",
        "inputs": {
          "price": "close"
        },
        "output": "daily_return"
      }
    ]
  }
}
```
