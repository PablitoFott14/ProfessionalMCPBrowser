## akshare-one-mcp_get_inner_trade_data

### What this tool is for
akshare-one-mcp_get_inner_trade_data retrieves insider trading data for a company. It is useful when the user wants to review disclosed insider buy or sell activity tied to a specific stock.

In practice, it can help add behavioral context around management or insider transactions before looking deeper into price action or fundamentals.

---

### Used parameters

**(1) symbol — Required**  
Default: No default  
Stock symbol or ticker to retrieve insider trading data for.

---

### JSON input alternatives

```json
{
  "intent": "Review insider trading activity for a mainland China bank stock",
  "params": {
    "symbol": "000001"
  }
}
```
