## irs-taxpayer-mcp_plan_retirement_withdrawals

### What this tool is for
Tax-efficient retirement withdrawals across traditional, Roth, and taxable accounts. Use this when the user wants to compare withdrawal order, spending coverage, and whether Roth conversions may fit the plan.

---

### Used parameters

**(1) taxYear - Required**  
Default: No default  
Tax year used for the withdrawal plan.

**(2) filingStatus - Required**  
Default: No default  
Allowed: single, married_filing_jointly, married_filing_separately, head_of_household, qualifying_surviving_spouse  
Filing status used for the withdrawal plan.

**(90) age - Required**  
Default: No default  
Current age used in the withdrawal plan.

**(163) traditionalBalance - Required**  
Default: No default  
Traditional IRA or 401(k) balance.

**(164) rothBalance - Required**  
Default: No default  
Roth IRA or Roth 401(k) balance.

**(165) taxableBalance - Required**  
Default: No default  
Taxable brokerage account balance.

**(166) socialSecurityIncome - Optional**  
Default: No default  
Annual Social Security income.

**(167) pensionIncome - Optional**  
Default: No default  
Annual pension income.

**(168) annualSpending - Required**  
Default: No default  
Annual pre-tax spending need.

**(169) rothConversionInterest - Optional**  
Default: No default  
Flag indicating whether Roth conversion strategy should be considered.

---

### JSON input alternatives

```json
{
  "intent": "Plan withdrawals for a retiree balancing taxable and traditional accounts",
  "params": {
    "taxYear": 2025,
    "filingStatus": "single",
    "age": 68,
    "traditionalBalance": 620000,
    "rothBalance": 140000,
    "taxableBalance": 210000,
    "socialSecurityIncome": 28000,
    "annualSpending": 72000
  }
}
```

```json
{
  "intent": "Plan joint retirement withdrawals and evaluate whether Roth conversions may help",
  "params": {
    "taxYear": 2025,
    "filingStatus": "married_filing_jointly",
    "age": 63,
    "traditionalBalance": 980000,
    "rothBalance": 260000,
    "taxableBalance": 180000,
    "pensionIncome": 22000,
    "annualSpending": 95000,
    "rothConversionInterest": true
  }
}
