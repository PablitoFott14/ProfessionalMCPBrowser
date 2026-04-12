## irs-taxpayer-mcp_compare_tax_years

### What this tool is for
Compares tax liability across tax years for the same income profile. Use this when the user wants to see how bracket changes and inflation adjustments affect tax outcomes over time.

---

### Used parameters

**(2) filingStatus - Required**  
Default: No default  
Filing status used across the year comparison.

**(3) grossIncome - Required**  
Default: No default  
Gross income used across the compared tax years.

**(5) selfEmploymentIncome - Optional**  
Default: No default  
Self-employment income included in the comparison.

**(12) dependents - Optional**  
Default: No default  
Number of qualifying dependents used in the comparison.

---

### JSON input alternatives

```json
{
  "intent": "Compare tax years for a single filer with wage income only",
  "params": {
    "filingStatus": "single",
    "grossIncome": 95000
  }
}
```

```json
{
  "intent": "Compare tax years for a head of household filer with self-employment income and dependents",
  "params": {
    "filingStatus": "head_of_household",
    "grossIncome": 130000,
    "selfEmploymentIncome": 40000,
    "dependents": 2
  }
}
```
