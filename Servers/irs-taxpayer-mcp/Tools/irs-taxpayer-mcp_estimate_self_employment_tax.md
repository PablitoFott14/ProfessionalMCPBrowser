## irs-taxpayer-mcp_estimate_self_employment_tax

### What this tool is for
Provides a detailed self-employment tax estimate, including Schedule C profit, self-employment tax, QBI deduction, and recommended quarterly payments. Use this when the user needs a business-income-focused estimate rather than a general tax calculation.

---

### Used parameters

**(1) taxYear - Required**  
Default: No default  
Tax year used for the estimate.

**(2) filingStatus - Required**  
Default: No default  
Filing status used for the estimate.

**(69) grossRevenue - Required**  
Default: No default  
Total business revenue used for the estimate.

**(70) businessExpenses - Required**  
Default: No default  
Total business expenses used for the estimate.

**(71) otherW2Income - Optional**  
Default: No default  
W-2 income from other jobs.

**(72) retirementContributions - Optional**  
Default: No default  
SEP IRA or Solo 401(k) contributions included in the estimate.

**(73) healthInsurancePremiums - Optional**  
Default: No default  
Self-employed health insurance premiums included in the estimate.

**(12) dependents - Optional**  
Default: No default  
Number of qualifying dependents used in the estimate.

---

### JSON input alternatives

```json
{
  "tool": "irs-taxpayer-mcp_estimate_self_employment_tax",
  "intent": "Estimate self-employment tax for a single filer with Schedule C income only",
  "params": {
    "taxYear": 2024,
    "filingStatus": "single",
    "grossRevenue": 140000,
    "businessExpenses": 35000
  }
}
```

```json
{
  "tool": "irs-taxpayer-mcp_estimate_self_employment_tax",
  "intent": "Estimate self-employment tax for a joint filer with business income, W-2 income, and retirement contributions",
  "params": {
    "taxYear": 2025,
    "filingStatus": "married_filing_jointly",
    "grossRevenue": 220000,
    "businessExpenses": 70000,
    "otherW2Income": 45000,
    "retirementContributions": 18000,
    "healthInsurancePremiums": 9000,
    "dependents": 2
  }
}
