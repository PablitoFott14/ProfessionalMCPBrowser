## irs-taxpayer-mcp_assess_audit_risk

### What this tool is for
An IRS audit-risk profile based on a taxpayer's return characteristics. Use this when the user wants to identify potential audit red flags, gauge relative risk, and review factors that may increase scrutiny.

---

### Used parameters

**(2) filingStatus - Required**  
Default: No default  
Allowed: single, married_filing_jointly, married_filing_separately, head_of_household, qualifying_surviving_spouse  
Filing status used in the audit-risk profile.

**(3) grossIncome - Required**  
Default: No default  
Total gross income.

**(5) selfEmploymentIncome - Optional**  
Default: No default  
Self-employment income.

**(133) cashBusiness - Optional**  
Default: No default  
Flag indicating whether the business is cash-intensive.

**(134) homeOfficeDeduction - Optional**  
Default: No default  
Flag indicating whether a home office deduction is being claimed.

**(31) charitableDonations - Optional**  
Default: No default  
Total charitable donations.

**(135) charitableNonCash - Optional**  
Default: No default  
Non-cash charitable donations.

**(136) businessMeals - Optional**  
Default: No default  
Business meal deductions.

**(137) vehicleDeduction - Optional**  
Default: No default  
Vehicle or mileage deduction.

**(138) rentalLosses - Optional**  
Default: No default  
Rental property losses claimed.

**(139) cryptoTransactions - Optional**  
Default: No default  
Flag indicating whether the taxpayer had cryptocurrency transactions.

**(140) foreignAccounts - Optional**  
Default: No default  
Flag indicating whether the taxpayer has foreign bank accounts or assets.

**(141) largeRefund - Optional**  
Default: No default  
Flag indicating whether the taxpayer expects a very large refund.

**(142) eitcClaimed - Optional**  
Default: No default  
Flag indicating whether the taxpayer is claiming EITC.

**(143) roundNumbers - Optional**  
Default: No default  
Flag indicating whether most deductions are reported as round numbers.

---

### JSON input alternatives

```json
{
  "intent": "Assess audit risk for a self-employed taxpayer with several common review triggers",
  "params": {
    "filingStatus": "single",
    "grossIncome": 145000,
    "selfEmploymentIncome": 98000,
    "cashBusiness": true,
    "homeOfficeDeduction": true,
    "businessMeals": 6200,
    "vehicleDeduction": 8400,
    "cryptoTransactions": true
  }
}
```

```json
{
  "intent": "Assess audit risk for a joint filer with charitable deductions, rental losses, and foreign-account exposure",
  "params": {
    "filingStatus": "married_filing_jointly",
    "grossIncome": 260000,
    "charitableDonations": 18000,
    "charitableNonCash": 6500,
    "rentalLosses": 12000,
    "foreignAccounts": true,
    "largeRefund": true,
    "roundNumbers": true
  }
}
```
