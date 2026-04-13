## irs-taxpayer-mcp_calculate_w4_withholding

### What this tool is for
Recommended W-4 withholding settings and estimates per-paycheck federal withholding. Use this when the user wants guidance on paycheck withholding configuration rather than an annual tax liability result alone.

---

### Used parameters

**(1) taxYear: Required**  
Default: No default  
Tax year used for the withholding estimate.

**(2) filingStatus: Required**  
Default: No default  
Allowed: single, married_filing_jointly, married_filing_separately, head_of_household, qualifying_surviving_spouse  
Filing status used for the withholding estimate.

**(21) annualSalary: Required**  
Default: No default  
Annual salary from the job used for the withholding estimate.

**(22) payFrequency: Required**  
Default: No default  
Allowed: weekly, biweekly, semimonthly, monthly  
Pay frequency used to estimate per-paycheck withholding.

**(23) otherIncome: Optional**  
Default: No default  
Other annual income included in the estimate.

**(24) deductions: Optional**  
Default: No default  
Expected deductions used in the estimate if greater than the standard deduction.

**(12) dependents: Optional**  
Default: No default  
Number of qualifying child dependents.

**(25) spouseWorks: Optional**  
Default: No default  
Flag indicating whether the taxpayer's spouse also works.

**(26) multipleJobs: Optional**  
Default: No default  
Flag indicating whether the taxpayer holds multiple jobs simultaneously.

---

### JSON input alternatives

```json
{
  "intent": "Estimate W-4 withholding for a single salaried employee paid biweekly",
  "params": {
    "taxYear": 2024,
    "filingStatus": "single",
    "annualSalary": 90000,
    "payFrequency": "biweekly"
  }
}
```

```json
{
  "intent": "Estimate W-4 settings for a joint filer with dependents, other income, and a working spouse",
  "params": {
    "taxYear": 2025,
    "filingStatus": "married_filing_jointly",
    "annualSalary": 130000,
    "payFrequency": "semimonthly",
    "otherIncome": 12000,
    "dependents": 2,
    "spouseWorks": true
  }
}
```
