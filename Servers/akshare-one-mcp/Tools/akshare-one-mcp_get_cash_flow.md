## akshare-one-mcp_get_cash_flow

### What this tool is for
Company cash flow statement data for a stock. It is useful when the user needs to understand how the business is generating and using cash across operating, investing, and financing activities.

---

### Used parameters

**(1) symbol: Required**  
Default: No default  
Stock symbol or ticker to retrieve cash flow statement data for.

**(7) source: Optional**  
Default: sina  
Uses the fixed supported data source for this tool.

**(9) recent_n: Optional**  
Default: 10  
Limits how many of the most recent cash flow records are returned.

---

### JSON input alternatives

```json
{
  "intent": "Review the most recent cash flow statement data for a mainland China bank stock",
  "params": {
    "symbol": "000001"
  }
}

{
  "intent": "Pull a longer cash flow history for a Hong Kong listed technology company",
  "params": {
    "symbol": "00700",
    "recent_n": 20
  }
}
```
