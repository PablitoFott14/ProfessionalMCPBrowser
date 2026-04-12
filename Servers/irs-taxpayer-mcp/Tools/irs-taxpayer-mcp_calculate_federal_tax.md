## irs-taxpayer-mcp_calculate_federal_tax

### What this tool is for
Calculates federal income tax for an individual taxpayer for TY2024 or TY2025. Use this when the user needs a local tax calculation that can incorporate filing status, income mix, deductions, credits, self-employment tax, capital gains, and related tax components.

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

**(4) w2Income - Optional**  
Default: No default  
W-2 wage income.

**(5) selfEmploymentIncome - Optional**  
Default: No default  
Self-employment income.

**(6) capitalGains - Optional**  
Default: No default  
Long-term capital gains or losses.

**(7) capitalGainsLongTerm - Optional**  
Default: true  
Flag indicating whether capital gains should be treated as long-term.

**(8) shortTermCapitalGains - Optional**  
Default: No default  
Short-term capital gains taxed as ordinary income.

**(9) qualifiedBusinessIncome - Optional**  
Default: No default  
Qualified Business Income used for the Section 199A deduction.

**(10) aboveTheLineDeductions - Optional**  
Default: No default  
Above-the-line deductions.

**(11) itemizedDeductions - Optional**  
Default: No default  
Itemized deductions used if greater than the standard deduction.

**(12) dependents - Optional**  
Default: No default  
Number of qualifying child dependents.

**(13) age65OrOlder - Optional**  
Default: No default  
Flag indicating whether the taxpayer is age 65 or older.

**(14) blind - Optional**  
Default: No default  
Flag indicating whether the taxpayer is blind.

**(15) isoExerciseSpread - Optional**  
Default: No default  
ISO exercise spread used for AMT calculation.

**(16) stateTaxDeducted - Optional**  
Default: No default  
State or local taxes included in itemized deductions for AMT-related calculation.

---

### JSON input alternatives

```json
{
  "tool": "irs-taxpayer-mcp_calculate_federal_tax",
  "intent": "Calculate federal tax for a single W-2 taxpayer in 2024",
  "params": {
    "taxYear": 2024,
    "filingStatus": "single",
    "grossIncome": 95000,
    "w2Income": 95000
  }
}
```

```json
{
  "tool": "irs-taxpayer-mcp_calculate_federal_tax",
  "intent": "Calculate federal tax for a married joint filer with self-employment income, qualified business income, and capital gains in 2025",
  "params": {
    "taxYear": 2025,
    "filingStatus": "married_filing_jointly",
    "grossIncome": 260000,
    "selfEmploymentIncome": 180000,
    "capitalGains": 20000,
    "qualifiedBusinessIncome": 180000,
    "aboveTheLineDeductions": 6000,
    "dependents": 2
  }
}
```
