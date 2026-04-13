## irs-taxpayer-mcp_analyze_relocation_taxes

### What this tool is for
The tax impact of relocating from one state to another. Use this when the user wants a deeper state-to-state comparison that includes projected savings rather than a single-state estimate.

---

### Used parameters

**(1) taxYear - Required**  
Default: No default  
Tax year used for the relocation analysis.

**(2) filingStatus - Required**  
Default: No default  
Allowed: single, married_filing_jointly, married_filing_separately, head_of_household, qualifying_surviving_spouse  
Filing status used for the relocation analysis.

**(3) grossIncome - Required**  
Default: No default  
Annual gross income.

**(177) fromState - Required**  
Default: No default  
Current state code.

**(178) toState - Required**  
Default: No default  
Target state code.

**(5) selfEmploymentIncome - Optional**  
Default: No default  
Self-employment income included in the comparison.

**(6) capitalGains - Optional**  
Default: No default  
Capital gains included in the comparison.

**(12) dependents - Optional**  
Default: No default  
Number of dependents included in the comparison.

**(179) yearsToProject - Optional**  
Default: No default  
Number of years used to project savings.

**(180) incomeGrowthRate - Optional**  
Default: No default  
Annual income growth rate used in the projection.

---

### JSON input alternatives

```json
{
  "tool": "irs-taxpayer-mcp_analyze_relocation_taxes",
  "intent": "Compare relocating from California to Texas for a wage earner",
  "params": {
    "taxYear": 2025,
    "filingStatus": "single",
    "grossIncome": 180000,
    "fromState": "CA",
    "toState": "TX",
    "yearsToProject": 5,
    "incomeGrowthRate": 0.03
  }
}
```

```json
{
  "tool": "irs-taxpayer-mcp_analyze_relocation_taxes",
  "intent": "Compare relocating from New York to Florida for a joint filer with business income and dependents",
  "params": {
    "taxYear": 2025,
    "filingStatus": "married_filing_jointly",
    "grossIncome": 260000,
    "fromState": "NY",
    "toState": "FL",
    "selfEmploymentIncome": 90000,
    "capitalGains": 20000,
    "dependents": 2,
    "yearsToProject": 7,
    "incomeGrowthRate": 0.04
  }
}
