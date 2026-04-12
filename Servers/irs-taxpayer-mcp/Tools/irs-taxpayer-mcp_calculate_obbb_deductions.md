## irs-taxpayer-mcp_calculate_obbb_deductions

### What this tool is for
Calculates OBBB deductions for TY2025 and later, including tips income, overtime pay, senior bonus, and auto loan interest deductions. Use this when the user needs to see which of the new OBBB deductions may apply and how much tax savings they may generate.

---

### Used parameters

**(1) taxYear - Required**  
Default: No default  
Tax year used for the calculation.

**(2) filingStatus - Required**  
Default: No default  
Filing status used for the calculation.

**(33) agi - Required**  
Default: No default  
Adjusted Gross Income used to evaluate OBBB deduction eligibility.

**(90) age - Optional**  
Default: No default  
Taxpayer age used for senior bonus analysis.

**(91) spouseAge - Optional**  
Default: No default  
Spouse age used for senior bonus analysis when filing jointly.

**(92) tipIncome - Optional**  
Default: No default  
Annual tip income from a qualifying occupation.

**(93) overtimePay - Optional**  
Default: No default  
Annual overtime premium pay.

**(94) autoLoanInterest - Optional**  
Default: No default  
Interest paid on a qualifying auto loan.

**(95) marginalRate - Optional**  
Default: No default  
Marginal tax rate used for tax savings estimates.

---

### JSON input alternatives

```json
{
  "tool": "irs-taxpayer-mcp_calculate_obbb_deductions",
  "intent": "Check which OBBB deductions may apply for a single taxpayer with tip income",
  "params": {
    "taxYear": 2025,
    "filingStatus": "single",
    "agi": 72000,
    "age": 34,
    "tipIncome": 18000,
    "marginalRate": 0.22
  }
}
```

```json
{
  "tool": "irs-taxpayer-mcp_calculate_obbb_deductions",
  "intent": "Estimate OBBB deductions for a joint filer with senior bonus, overtime pay, and auto loan interest",
  "params": {
    "taxYear": 2025,
    "filingStatus": "married_filing_jointly",
    "agi": 145000,
    "age": 67,
    "spouseAge": 65,
    "overtimePay": 9000,
    "autoLoanInterest": 2400,
    "marginalRate": 0.24
  }
}
```
