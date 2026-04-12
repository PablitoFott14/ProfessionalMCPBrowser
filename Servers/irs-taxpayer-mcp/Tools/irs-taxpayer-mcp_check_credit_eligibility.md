## irs-taxpayer-mcp_check_credit_eligibility

### What this tool is for
Checks which federal tax credits a taxpayer may be eligible for based on their situation. Use this when the user needs an eligibility screen across possible credits before looking at a specific credit in detail.

---

### Used parameters

**(33) agi - Required**  
Default: No default  
Adjusted Gross Income used in the eligibility screening.

**(2) filingStatus - Required**  
Default: No default  
Allowed: single, married_filing_jointly, married_filing_separately, head_of_household, qualifying_surviving_spouse  
Filing status used in the eligibility screening.

**(37) hasChildren - Optional**  
Default: No default  
Flag indicating whether the taxpayer has qualifying children under 17.

**(38) numChildren - Optional**  
Default: No default  
Number of qualifying children used in the screening.

**(39) hasChildcare - Optional**  
Default: No default  
Flag indicating whether the taxpayer pays for childcare to work.

**(40) isStudent - Optional**  
Default: No default  
Flag indicating whether the taxpayer is enrolled in post-secondary education.

**(41) hasStudentLoans - Optional**  
Default: No default  
Flag indicating whether the taxpayer pays student loan interest.

**(42) boughtEV - Optional**  
Default: No default  
Flag indicating whether the taxpayer bought an electric vehicle this year.

**(43) madeHomeImprovements - Optional**  
Default: No default  
Flag indicating whether the taxpayer made energy-efficient home improvements.

**(44) installedSolar - Optional**  
Default: No default  
Flag indicating whether the taxpayer installed solar or renewable energy.

**(45) hasRetirementContributions - Optional**  
Default: No default  
Flag indicating whether the taxpayer made retirement contributions.

**(46) hasMarketplaceInsurance - Optional**  
Default: No default  
Flag indicating whether the taxpayer bought insurance through the ACA marketplace.

**(47) hasEarnedIncome - Optional**  
Default: No default  
Flag indicating whether the taxpayer has earned income from work.

**(48) paidForeignTax - Optional**  
Default: No default  
Flag indicating whether the taxpayer paid income tax to a foreign country.

---

### JSON input alternatives

```json
{
  "tool": "irs-taxpayer-mcp_check_credit_eligibility",
  "intent": "Check likely credit eligibility for a single parent with children and childcare costs",
  "params": {
    "agi": 52000,
    "filingStatus": "head_of_household",
    "hasChildren": true,
    "numChildren": 2,
    "hasChildcare": true,
    "hasEarnedIncome": true
  }
}
```

```json
{
  "tool": "irs-taxpayer-mcp_check_credit_eligibility",
  "intent": "Check likely credit eligibility for a taxpayer with education, EV, and retirement-related factors",
  "params": {
    "agi": 78000,
    "filingStatus": "single",
    "isStudent": true,
    "hasStudentLoans": true,
    "boughtEV": true,
    "hasRetirementContributions": true
  }
}
```
