## akshare-one-mcp_get_realtime_data

### What this tool is for
Live market data for stocks from the supported real-time sources. It is useful when the user needs a current market snapshot instead of historical bars.

It can be used either to check a specific symbol or to pull broader real-time market coverage, depending on how the server implements the optional `symbol` filter.

---

### Used parameters

**(1) symbol — Optional**  
Default: null  
Stock symbol or ticker to retrieve real-time data for.

**(7) source — Optional**  
Default: eastmoney_direct  
Chooses which real-time market data source is used.

---

### JSON input alternatives

```json
{
  "tool": "akshare-one-mcp_get_realtime_data",
  "intent": "Check the latest real-time data for a specific mainland China stock",
  "params": {
    "symbol": "000001"
  }
}

{
  "tool": "akshare-one-mcp_get_realtime_data",
  "intent": "Retrieve live data for a Hong Kong listed stock using a different source",
  "params": {
    "symbol": "00700",
    "source": "xueqiu"
  }
}
```
