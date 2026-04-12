## irs-taxpayer-mcp_compare_mfj_vs_mfs

### What this tool is for
Compares Married Filing Jointly against Married Filing Separately and highlights the tax difference along with MFS restrictions that may matter. Use this when the user needs a filing-status decision specifically for married taxpayers.

---

### Used parameters

**(1) taxYear - Required**  
Default: No default  
Tax year (2024 or 2025).

**(84) spouse1Income - Required**  
Default: No default  
Spouse 1 gross income.

**(85) spouse2Income - Required**  
Default: No default  
Spouse 2 gross income.

**(12) dependents - Optional**  
Default: No default  
Number of qualifying children.

**(11) itemizedDeductions - Optional**  
Default: No default  
Total itemized deductions (combined for MFJ, split for MFS).

**(86) studentLoanInterest - Optional**  
Default: No default  
Either spouse paying student loan interest.

**(87) hasEducationCredits - Optional**  
Default: No default  
Either spouse claiming AOTC or LLC.

**(88) hasEITC - Optional**  
Default: No default  
Either spouse would qualify for the EITC.

**(89) hasIRAContributions - Optional**  
Default: No default  
Either spouse contributing to an IRA.

---

### JSON input alternatives

```json
{
  "tool": "irs-taxpayer-mcp_compare_mfj_vs_mfs",
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
  "tool": "irs-taxpayer-mcp_compare_mfj_vs_mfs",
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
