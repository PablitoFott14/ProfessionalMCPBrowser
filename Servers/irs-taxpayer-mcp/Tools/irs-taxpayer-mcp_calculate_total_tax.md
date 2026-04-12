## irs-taxpayer-mcp_calculate_total_tax

### What this tool is for
Calculates combined federal and state tax liability in one call. Use this when the user needs a more complete tax picture that includes both the federal breakdown and the tax impact of a specific state.

---

### Used parameters

**(1) taxYear - Required**  
Default: No default  
Tax year used for the calculation.

**(2) filingStatus - Required**  
Default: No default  
Allowed: single, married_filing_jointly, married_filing_separately, head_of_household, qualifying_surviving_spouse  
Filing status used for the calculation.

**(3) grossIncome - Required**  
Default: No default  
Total gross income in USD.

**(20) stateCode - Required**  
Default: No default  
Two-letter state code used for the state tax calculation.

**(4) w2Income - Optional**  
Default: No default  
W-2 wage income.

**(5) selfEmploymentIncome - Optional**  
Default: No default  
Self-employment income.

**(6) capitalGains - Optional**  
Default: No default  
Long-term capital gains.

**(7) capitalGainsLongTerm - Optional**  
Default: true  
Flag indicating whether capital gains should be treated as long-term.

**(9) qualifiedBusinessIncome - Optional**  
Default: No default  
Qualified Business Income used for the Section 199A deduction.

**(10) aboveTheLineDeductions - Optional**  
Default: No default  
Above-the-line deductions.

**(11) itemizedDeductions - Optional**  
Default: No default  
Total itemized deductions.

**(12) dependents - Optional**  
Default: No default  
Number of qualifying child dependents.

---

### JSON input alternatives

```json
{
  "tool": "irs-taxpayer-mcp_calculate_total_tax",
  "intent": "Calculate combined federal and California tax for a single wage earner",
  "params": {
    "taxYear": 2024,
    "filingStatus": "single",
    "grossIncome": 110000,
    "stateCode": "CA",
    "w2Income": 110000
  }
}
```

```json
{
  "tool": "irs-taxpayer-mcp_calculate_total_tax",
  "intent": "Calculate combined federal and New York tax for a joint filer with business income and dependents",
  "params": {
    "taxYear": 2025,
    "filingStatus": "married_filing_jointly",
    "grossIncome": 240000,
    "stateCode": "NY",
    "selfEmploymentIncome": 150000,
    "qualifiedBusinessIncome": 150000,
    "aboveTheLineDeductions": 5000,
    "dependents": 2
  }
}
```
