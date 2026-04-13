## irs-taxpayer-mcp_get_retirement_strategy

### What this tool is for
Detailed information on tax-advantaged retirement strategies. Use this when the user needs strategy-level guidance rather than account-type reference information or a direct tax calculation.

---

### Used parameters

**(50) strategyId: Optional**  
Default: No default  
Specific retirement strategy identifier used to narrow the returned information.

---

### JSON input alternatives

```json
{
  "intent": "List available tax-advantaged retirement strategies",
  "params": {}
}
```

```json
{
  "intent": "Get details for the Backdoor Roth strategy",
  "params": {
    "strategyId": "backdoor_roth"
  }
}
```
