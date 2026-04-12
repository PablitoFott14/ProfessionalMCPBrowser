## irs-taxpayer-mcp_compare_mfj_vs_mfs

### What this tool is for
Compares Married Filing Jointly against Married Filing Separately and highlights the tax difference along with MFS restrictions that may matter. Use this when the user needs a filing-status decision specifically for married taxpayers.

---

### Used parameters

**(1) taxYear - Required**  
Default: No default  
Tax year used for the comparison.

**(84) spouse1Income - Required**  
Default: No default  
Gross income for spouse 1.

**(85) spouse2Income - Required**  
Default: No default  
Gross income for spouse 2.

**(12) dependents - Optional**  
Default: No default  
Number of qualifying children used in the comparison.

**(11) itemizedDeductions - Optional**  
Default: No default  
Total itemized deductions used in the comparison.

**(86) studentLoanInterestFlag - Optional**  
Default: No default  
Flag indicating whether either spouse is paying student loan interest.

**(87) hasEducationCredits - Optional**  
Default: No default  
Flag indicating whether either spouse is claiming education credits.

**(88) hasEITC - Optional**  
Default: No default  
Flag indicating whether either spouse would qualify for the EITC.

**(89) hasIRAContributions - Optional**  
Default: No default  
Flag indicating whether either spouse is contributing to an IRA.

---

### JSON input alternatives

```json
{
  "intent": "Compare MFJ and MFS for a married couple with straightforward income",
  "params": {
    "taxYear": 2024,
    "spouse1Income": 90000,
    "spouse2Income": 55000
  }
}
```

```json
{
  "intent": "Compare MFJ and MFS for a married couple with children, itemized deductions, and education-related restrictions",
  "params": {
    "taxYear": 2025,
    "spouse1Income": 140000,
    "spouse2Income": 60000,
    "dependents": 2,
    "itemizedDeductions": 22000,
    "studentLoanInterest": true,
    "hasEducationCredits": true,
    "hasIRAContributions": true
  }
}
