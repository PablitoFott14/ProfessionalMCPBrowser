## irs-taxpayer-mcp_estimate_quarterly_tax

### What this tool is for
Quarterly federal tax payments for taxpayers who need to make estimated payments. Use this when the user needs a projected quarterly payment schedule based on expected annual income, self-employment income, withholding, and credits.

---

### Used parameters

**(1) taxYear - Required**  
Default: No default  
Tax year used for the estimate.

**(2) filingStatus - Required**  
Default: No default  
Allowed: single, married_filing_jointly, married_filing_separately, head_of_household, qualifying_surviving_spouse  
Filing status used for the estimate.

**(17) expectedAnnualIncome - Required**  
Default: No default  
Expected total annual income used for the estimate.

**(5) selfEmploymentIncome - Optional**  
Default: No default  
Expected self-employment income included in the estimate.

**(18) w2Withholding - Optional**  
Default: No default  
Expected W-2 withholding for the year.

**(19) otherCredits - Optional**  
Default: No default  
Expected other tax credits used in the estimate.

---

### JSON input alternatives

```json
{
  "intent": "Estimate quarterly taxes for a self-employed single filer",
  "params": {
    "taxYear": 2024,
    "filingStatus": "single",
    "expectedAnnualIncome": 120000,
    "selfEmploymentIncome": 120000
  }
}
```

```json
{
  "intent": "Estimate quarterly taxes for a joint filer with withholding and credits",
  "params": {
    "taxYear": 2025,
    "filingStatus": "married_filing_jointly",
    "expectedAnnualIncome": 210000,
    "selfEmploymentIncome": 90000,
    "w2Withholding": 18000,
    "otherCredits": 2000
  }
}
```
