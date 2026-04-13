## patent-mcp-server_google_search_by_inventor

### What this tool is used for
Searches Google Patents for patents where a specified inventor is listed. It is used when the user wants to find all patents associated with a particular inventor, track an inventor's portfolio, or research their patenting activity within a country or date range.

---

### Used parameters

**(41) inventor_name: Required**
Default: No default
Inventor name to search for.

**(37) country: Optional**
Default: US
Allowed: US, EP, WO, JP, CN, KR, GB, DE, FR, CA, AU
Country code to scope the patent search.

**(4) limit: Optional**
Default: 100
Maximum number of results to return. Maximum allowed value is 500.

**(14) offset: Optional**
Default: 0
Number of results to skip for pagination.

**(38) start_date: Optional**
Default: null
Start date for filtering by publication date. Integer in YYYYMMDD format (e.g., 20220101).

**(39) end_date: Optional**
Default: null
End date for filtering by publication date. Integer in YYYYMMDD format (e.g., 20251231).

---

### JSON input alternatives

```json
{
  "intent": "Find all US patents listed under a specific inventor",
  "params": {
    "inventor_name": "Jane Smith",
    "country": "US",
    "limit": 50
  }
}

{
  "intent": "Search for PCT applications by an inventor published between 2018 and 2023",
  "params": {
    "inventor_name": "John Doe",
    "country": "WO",
    "start_date": 20180101,
    "end_date": 20231231
  }
}
```
