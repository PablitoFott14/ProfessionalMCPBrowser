## irs-taxpayer-mcp_analyze_education_tax_benefits

### What this tool is for
Education-related tax benefits such as the AOTC, Lifetime Learning Credit, student loan interest deduction, and 529 plan advantages. Use this when the user needs to evaluate which education tax benefits may be most favorable for their situation.

---

### Used parameters

**(2) filingStatus: Required**  
Default: No default  
Allowed: single, married_filing_jointly, married_filing_separately, head_of_household, qualifying_surviving_spouse  
Filing status used in the analysis.

**(33) agi: Required**  
Default: No default  
Adjusted Gross Income used in the analysis.

**(78) tuitionPaid: Required**  
Default: No default  
Tuition and qualified education expenses paid.

**(79) isUndergrad: Required**  
Default: No default  
Flag indicating whether the student is in the first four years of undergraduate study.

**(80) yearsAOTCClaimed: Optional**  
Default: No default  
Number of years the AOTC has already been claimed.

**(81) studentLoanInterest: Optional**  
Default: No default  
Student loan interest paid during the year.

**(82) has529Plan: Optional**  
Default: No default  
Flag indicating whether the taxpayer is contributing to or using a 529 plan.

**(83) contribution529: Optional**  
Default: No default  
Amount contributed to a 529 plan during the year.

---

### JSON input alternatives

```json
{
  "intent": "Compare education tax benefits for an undergraduate student with tuition expenses",
  "params": {
    "filingStatus": "single",
    "agi": 68000,
    "tuitionPaid": 14000,
    "isUndergrad": true,
    "yearsAOTCClaimed": 1
  }
}
```

```json
{
  "intent": "Compare education tax benefits for a graduate student with student loan interest and a 529 plan",
  "params": {
    "filingStatus": "married_filing_jointly",
    "agi": 125000,
    "tuitionPaid": 18000,
    "isUndergrad": false,
    "studentLoanInterest": 2200,
    "has529Plan": true,
    "contribution529": 5000
  }
}
