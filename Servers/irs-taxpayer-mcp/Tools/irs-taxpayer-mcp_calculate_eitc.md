## irs-taxpayer-mcp_calculate_eitc

### What this tool is for
Calculates the exact Earned Income Tax Credit amount. Use this when the user needs a specific EITC result rather than a broader credit eligibility screen.

---

### Used parameters

**(1) taxYear - Required**  
Default: No default  
Tax year used for the EITC calculation.

**(2) filingStatus - Required**  
Default: No default  
Allowed: single, married_filing_jointly, married_filing_separately, head_of_household, qualifying_surviving_spouse  
Filing status used for the EITC calculation.

**(51) earnedIncome - Required**  
Default: No default  
Earned income used for the EITC calculation.

**(33) agi - Required**  
Default: No default  
Adjusted Gross Income used for the EITC calculation.

**(52) qualifyingChildren - Required**  
Default: No default  
Number of qualifying children used for the EITC calculation.

**(53) investmentIncome - Optional**  
Default: No default  
Investment income used in EITC eligibility and amount calculation.

---

### JSON input alternatives

```json
{
  "tool": "irs-taxpayer-mcp_calculate_eitc",
  "intent": "Calculate EITC for a single filer with no qualifying children",
  "params": {
    "taxYear": 2024,
    "filingStatus": "single",
    "earnedIncome": 18000,
    "agi": 18000,
    "qualifyingChildren": 0
  }
}
```

```json
{
  "tool": "irs-taxpayer-mcp_calculate_eitc",
  "intent": "Calculate EITC for a head of household filer with two qualifying children",
  "params": {
    "taxYear": 2025,
    "filingStatus": "head_of_household",
    "earnedIncome": 32000,
    "agi": 31500,
    "qualifyingChildren": 2,
    "investmentIncome": 500
  }
}
```
