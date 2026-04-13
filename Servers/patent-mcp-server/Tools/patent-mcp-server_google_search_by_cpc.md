## patent-mcp-server_google_search_by_cpc

### What this tool is used for
Google_search_by_cpc searches Google Patents for patents classified under a specific Cooperative Patent Classification (CPC) code. It is used when the user wants to explore a defined technology area by its classification code rather than by keyword, making it useful for structured prior art searches or technology landscape analysis.

---

### Used parameters

**(43) cpc_code — Required**
Default: No default
Cooperative Patent Classification (CPC) code to search for (e.g., G06N3/08 for neural networks).

**(37) country — Optional**
Default: US
Allowed: US, EP, WO, JP, CN, KR, GB, DE, FR, CA, AU
Country code to scope the patent search.

**(4) limit — Optional**
Default: 100
Maximum number of results to return. Maximum allowed value is 500.

**(14) offset — Optional**
Default: 0
Number of results to skip for pagination.

**(38) start_date — Optional**
Default: null
Start date for filtering by publication date. Integer in YYYYMMDD format (e.g., 20220101).

**(39) end_date — Optional**
Default: null
End date for filtering by publication date. Integer in YYYYMMDD format (e.g., 20251231).

---

### JSON input alternatives

```json
{
  "intent": "Find US patents classified under the neural network CPC code",
  "params": {
    "cpc_code": "G06N3/08",
    "country": "US",
    "limit": 50
  }
}

{
  "intent": "Search for international patents in battery technology published since 2020",
  "params": {
    "cpc_code": "H01M10/0525",
    "country": "WO",
    "start_date": 20200101
  }
}
```
