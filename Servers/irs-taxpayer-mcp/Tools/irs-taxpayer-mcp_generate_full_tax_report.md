## irs-taxpayer-mcp_generate_full_tax_report

### What this tool is for
Generates a full tax estimate report that combines federal tax, state tax, FICA, credits, deductions, withholding, and payment information into one summary. Use this when the user wants a broad end-to-end estimate rather than a focused calculation on a single tax area.

---

### Used parameters

**(1) taxYear - Required**  
Default: No default  
Tax year used for the report.

**(2) filingStatus - Required**  
Default: No default  
Filing status used for the report.

**(4) w2Income - Optional**  
Default: No default  
W-2 wages.

**(5) selfEmploymentIncome - Optional**  
Default: No default  
Self-employment net profit.

**(98) interestIncome - Optional**  
Default: No default  
Interest income.

**(99) dividendIncome - Optional**  
Default: No default  
Ordinary dividend income.

**(100) qualifiedDividends - Optional**  
Default: No default  
Qualified dividends.

**(101) longTermCapitalGains - Optional**  
Default: No default  
Long-term capital gains or losses.

**(8) shortTermCapitalGains - Optional**  
Default: No default  
Short-term capital gains or losses.

**(23) otherIncome - Optional**  
Default: No default  
Other income.

**(10) aboveTheLineDeductions - Optional**  
Default: No default  
Above-the-line deductions.

**(30) mortgageInterest - Optional**  
Default: No default  
Mortgage interest.

**(102) stateLocalTaxesPaid - Optional**  
Default: No default  
State, local, or property taxes paid.

**(31) charitableDonations - Optional**  
Default: No default  
Charitable contributions.

**(28) medicalExpenses - Optional**  
Default: No default  
Unreimbursed medical expenses.

**(32) otherItemized - Optional**  
Default: No default  
Other itemized deductions.

**(12) dependents - Optional**  
Default: No default  
Qualifying children under 17.

**(9) qualifiedBusinessIncome - Optional**  
Default: No default  
Qualified Business Income used for the Section 199A deduction.

**(20) stateCode - Optional**  
Default: No default  
State code used for the state tax estimate.

**(103) federalWithheld - Optional**  
Default: No default  
Federal tax already withheld year to date.

**(104) stateWithheld - Optional**  
Default: No default  
State tax already withheld year to date.

**(105) estimatedPaymentsMade - Optional**  
Default: No default  
Estimated tax payments already made.

---

### JSON input alternatives

```json
{
  "tool": "irs-taxpayer-mcp_generate_full_tax_report",
  "intent": "Generate a full tax estimate report for a single wage earner with investment income",
  "params": {
    "taxYear": 2024,
    "filingStatus": "single",
    "w2Income": 125000,
    "interestIncome": 1200,
    "dividendIncome": 1800,
    "qualifiedDividends": 1200,
    "stateCode": "CA",
    "federalWithheld": 22000,
    "stateWithheld": 6500
  }
}
```

```json
{
  "tool": "irs-taxpayer-mcp_generate_full_tax_report",
  "intent": "Generate a full tax estimate report for a joint filer with business income, deductions, and estimated payments",
  "params": {
    "taxYear": 2025,
    "filingStatus": "married_filing_jointly",
    "w2Income": 90000,
    "selfEmploymentIncome": 70000,
    "longTermCapitalGains": 15000,
    "aboveTheLineDeductions": 7000,
    "mortgageInterest": 16000,
    "stateLocalTaxesPaid": 12000,
    "charitableDonations": 3000,
    "dependents": 2,
    "qualifiedBusinessIncome": 70000,
    "stateCode": "NY",
    "federalWithheld": 18000,
    "stateWithheld": 5000,
    "estimatedPaymentsMade": 6000
  }
}
