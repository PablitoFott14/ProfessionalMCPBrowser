## irs-taxpayer-mcp_analyze_mortgage_tax_benefit

### What this tool is for
The tax benefit of mortgage interest and property taxes by comparing itemizing against the standard deduction. Use this when the user wants to understand whether homeownership-related deductions are providing a tax advantage.

---

### Used parameters

**(1) taxYear - Required**  
Default: No default  
Tax year used for the analysis.

**(2) filingStatus - Required**  
Default: No default  
Allowed: single, married_filing_jointly, married_filing_separately, head_of_household, qualifying_surviving_spouse  
Filing status used for the analysis.

**(3) grossIncome - Required**  
Default: No default  
Gross income used in the analysis.

**(30) mortgageInterest - Required**  
Default: No default  
Annual mortgage interest paid.

**(74) propertyTaxes - Required**  
Default: No default  
Annual property taxes paid.

**(75) stateIncomeTaxes - Optional**  
Default: No default  
State or local income taxes paid.

**(32) otherItemized - Optional**  
Default: No default  
Other itemized deductions included in the analysis.

**(76) mortgageBalance - Optional**  
Default: No default  
Current mortgage balance.

**(77) interestRate - Optional**  
Default: No default  
Mortgage interest rate.

---

### JSON input alternatives

```json
{
  "intent": "Analyze the tax benefit of itemizing for a single homeowner",
  "params": {
    "taxYear": 2024,
    "filingStatus": "single",
    "grossIncome": 135000,
    "mortgageInterest": 14000,
    "propertyTaxes": 7000
  }
}
```

```json
{
  "intent": "Analyze the tax benefit of a larger mortgage for a joint filer with additional itemized deductions",
  "params": {
    "taxYear": 2025,
    "filingStatus": "married_filing_jointly",
    "grossIncome": 260000,
    "mortgageInterest": 22000,
    "propertyTaxes": 11000,
    "stateIncomeTaxes": 9000,
    "otherItemized": 4000,
    "mortgageBalance": 420000,
    "interestRate": 0.065
  }
}
