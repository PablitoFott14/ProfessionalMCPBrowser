## irs-taxpayer-mcp_estimate_state_tax

### What this tool is for
Estimates state income tax for a given state and taxable income using simplified state brackets. Use this when the user needs a state-only estimate rather than combined federal and state tax results.

---

### Used parameters

**(20) stateCode - Required**  
Default: No default  
Two-letter state code used for the estimate.

**(54) taxableIncome - Required**  
Default: No default  
State taxable income used for the estimate.

**(2) filingStatus - Optional**  
Default: single  
Allowed: single, married_filing_jointly, married_filing_separately, head_of_household, qualifying_surviving_spouse  
Filing status used for the state tax estimate.

---

### JSON input alternatives

```json
{
  "tool": "irs-taxpayer-mcp_estimate_state_tax",
  "intent": "Estimate California state income tax for a single filer",
  "params": {
    "stateCode": "CA",
    "taxableIncome": 85000
  }
}
```

```json
{
  "tool": "irs-taxpayer-mcp_estimate_state_tax",
  "intent": "Estimate New York state income tax for a married filer",
  "params": {
    "stateCode": "NY",
    "taxableIncome": 145000,
    "filingStatus": "married"
  }
}
```
