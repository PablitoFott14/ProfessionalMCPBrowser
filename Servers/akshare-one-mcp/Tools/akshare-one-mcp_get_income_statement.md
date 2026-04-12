## akshare-one-mcp_get_income_statement

### What this tool is for
Retrieves company income statement data for a stock. It is useful when the user needs revenue, expenses, and profitability information to understand operating performance over recent reporting periods.

---

### Used parameters

**(1) symbol — Required**  
Default: No default  
Stock symbol or ticker to retrieve income statement data for.

**(9) recent_n — Optional**  
Default: 10  
Limits how many of the most recent income statement records are returned.

---

### JSON input alternatives

```json
{
  "tool": "akshare-one-mcp_get_income_statement",
  "intent": "Review the most recent income statement data for a mainland China bank stock",
  "params": {
    "symbol": "000001"
  }
}

{
  "tool": "akshare-one-mcp_get_income_statement",
  "intent": "Pull a longer income statement history for a Hong Kong listed technology company",
  "params": {
    "symbol": "00700",
    "recent_n": 20
  }
}
```
