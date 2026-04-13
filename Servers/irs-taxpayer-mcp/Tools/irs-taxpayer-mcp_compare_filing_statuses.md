## irs-taxpayer-mcp_compare_filing_statuses

### What this tool is for
Federal tax liability across filing statuses for the same income profile. Use this when the user wants to see how tax outcomes differ by filing status without manually recalculating each case.

---

### Used parameters

**(1) taxYear - Required**  
Default: No default  
Tax year used for the comparison.

**(3) grossIncome - Required**  
Default: No default  
Total gross income used across the compared filing statuses.

**(11) itemizedDeductions - Optional**  
Default: No default  
Itemized deductions applied in the comparison if applicable.

**(12) dependents - Optional**  
Default: No default  
Number of qualifying dependents used in the comparison.

---

### JSON input alternatives

```json
{
  "tool": "irs-taxpayer-mcp_compare_filing_statuses",
  "intent": "Compare filing statuses for a taxpayer with moderate income",
  "params": {
    "taxYear": 2024,
    "grossIncome": 85000
  }
}
```

```json
{
  "tool": "irs-taxpayer-mcp_compare_filing_statuses",
  "intent": "Compare filing statuses for a taxpayer with itemized deductions and dependents",
  "params": {
    "taxYear": 2025,
    "grossIncome": 140000,
    "itemizedDeductions": 18000,
    "dependents": 2
  }
}
```
