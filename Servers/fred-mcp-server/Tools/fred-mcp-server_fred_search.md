## fred-mcp-server_fred_search

### What this tool is for
Searches for FRED economic data series by keywords, tags, identifiers, or filters. Use this when the user needs to locate relevant economic series before requesting observations or working with a specific series ID.

---

### Used parameters

**(1) search_text - Optional**  
Default: null  
Text used to search for matching series.

**(2) search_type - Optional**  
Default: null  
Search mode used to search by full text or series ID.

**(3) tag_names - Optional**  
Default: null  
Comma-separated list of tag names used to filter results.

**(4) exclude_tag_names - Optional**  
Default: null  
Comma-separated list of tag names used to exclude results.

**(5) limit - Optional**  
Default: 25  
Maximum number of results to return.

**(6) offset - Optional**  
Default: 0  
Number of results to skip for pagination.

**(7) order_by - Optional**  
Default: null  
Field used to order the results.

**(8) sort_order - Optional**  
Default: null  
Sort direction used for ordered results.

**(9) filter_variable - Optional**  
Default: null  
Variable used to filter the results.

**(10) filter_value - Optional**  
Default: null  
Value used for the selected filter variable.

---

### JSON input alternatives

```json
{
  "tool": "fred-mcp-server_fred_search",
  "intent": "Search FRED for unemployment-related series",
  "params": {
    "search_text": "unemployment"
  }
}
```

```json
{
  "tool": "fred-mcp-server_fred_search",
  "intent": "Search FRED for monthly CPI series ordered by popularity",
  "params": {
    "search_text": "CPI",
    "filter_variable": "frequency",
    "filter_value": "Monthly",
    "order_by": "popularity",
    "sort_order": "desc",
    "limit": 20
  }
}
```
