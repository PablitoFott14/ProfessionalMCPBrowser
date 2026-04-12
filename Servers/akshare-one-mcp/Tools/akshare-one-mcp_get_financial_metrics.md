## akshare-one-mcp_get_financial_metrics

### What this tool is for
Retrieves key financial metrics derived from the three major financial statements. It is useful when the user wants a compact financial view without reviewing the full balance sheet, income statement, and cash flow statement separately.

---

### Used parameters

**(1) symbol — Required**  
Default: No default  
Stock symbol or ticker to retrieve financial metrics for.

**(9) recent_n — Optional**  
Default: 10  
Limits how many of the most recent metric records are returned.

---

### JSON input alternatives

```json
{
  "intent": "Review recent financial metrics for a mainland China bank stock",
  "params": {
    "symbol": "000001"
  }
}

{
  "intent": "Pull a longer financial metric history for a Hong Kong listed technology company",
  "params": {
    "symbol": "00700",
    "recent_n": 20
  }
}
```
