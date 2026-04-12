## irs-taxpayer-mcp_compare_state_taxes

### What this tool is for
Compares state income tax across multiple states for the same taxable income. Use this when the user needs a location-based comparison rather than a single-state estimate.

---

### Used parameters

**(55) states - Required**  
Default: No default  
List of state codes used in the comparison.

**(54) taxableIncome - Required**  
Default: No default  
Taxable income used across the state comparison.

---

### JSON input alternatives

```json
{
  "tool": "irs-taxpayer-mcp_compare_state_taxes",
  "intent": "Compare state taxes across several common relocation states",
  "params": {
    "states": ["CA", "TX", "WA", "NY"],
    "taxableIncome": 120000
  }
}
```

```json
{
  "tool": "irs-taxpayer-mcp_compare_state_taxes",
  "intent": "Compare state taxes across northeastern states for the same income",
  "params": {
    "states": ["NY", "NJ", "MA", "CT"],
    "taxableIncome": 185000
  }
}
```
