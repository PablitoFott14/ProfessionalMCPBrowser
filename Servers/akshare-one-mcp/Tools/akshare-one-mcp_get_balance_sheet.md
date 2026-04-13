## akshare-one-mcp_get_balance_sheet

### What this tool is for
Company balance sheet data for a stock. It is useful when the user needs a snapshot of assets, liabilities, and equity to understand financial position and capital structure.

---

### Used parameters

**(1) symbol — Required**  
Default: No default  
Stock symbol or ticker to retrieve balance sheet data for.

**(9) recent_n — Optional**  
Default: 10  
Limits how many of the most recent balance sheet records are returned.

---

### JSON input alternatives

```json
{
  "intent": "Review the most recent balance sheet entries for a mainland China bank stock",
  "params": {
    "symbol": "000001"
  }
}

{
  "intent": "Pull a longer balance sheet history for a Hong Kong listed technology company",
  "params": {
    "symbol": "00700",
    "recent_n": 20
  }
}
```
