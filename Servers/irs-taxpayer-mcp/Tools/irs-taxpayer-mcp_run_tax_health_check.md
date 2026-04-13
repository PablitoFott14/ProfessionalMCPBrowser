## irs-taxpayer-mcp_run_tax_health_check

### What this tool is for
A broad tax health check across income, withholding, deductions, credits, retirement savings, and common risk areas. Use this when the user wants a single high-level diagnostic rather than running several separate tax tools.

---

### Used parameters

**(1) taxYear: Required**  
Default: No default  
Tax year used for the health check.

**(2) filingStatus: Required**  
Default: No default  
Allowed: single, married_filing_jointly, married_filing_separately, head_of_household, qualifying_surviving_spouse  
Filing status used for the health check.

**(90) age: Optional**  
Default: No default  
Age used in the health check.

**(3) grossIncome: Required**  
Default: No default  
Gross income used in the health check.

**(4) w2Income: Optional**  
Default: No default  
W-2 income.

**(5) selfEmploymentIncome: Optional**  
Default: No default  
Self-employment income.

**(6) capitalGains: Optional**  
Default: No default  
Capital gains.

**(20) stateCode: Optional**  
Default: No default  
State code used for the health check.

**(12) dependents: Optional**  
Default: No default  
Number of dependents.

**(30) mortgageInterest: Optional**  
Default: No default  
Mortgage interest.

**(29) stateLocalTaxes: Optional**  
Default: No default  
State and local taxes.

**(31) charitableDonations: Optional**  
Default: No default  
Charitable donations.

**(118) retirement401k: Optional**  
Default: No default  
401(k) or 403(b) contribution amount.

**(181) retirementIRA: Optional**  
Default: No default  
IRA contribution amount.

**(182) hsaContributions: Optional**  
Default: No default  
HSA contribution amount.

**(103) federalWithheld: Optional**  
Default: No default  
Federal tax withheld.

**(148) hasHealthInsurance: Optional**  
Default: No default  
Flag indicating whether the taxpayer has health insurance relevant to filing.

**(40) isStudent: Optional**  
Default: No default  
Flag indicating whether the taxpayer is currently enrolled in post-secondary education.

**(42) boughtEV: Optional**  
Default: No default  
Flag indicating whether the taxpayer bought an electric vehicle.

**(44) installedSolar: Optional**  
Default: No default  
Flag indicating whether the taxpayer installed solar or renewable energy.

---

### JSON input alternatives

```json
{
  "intent": "Run a health check for a salaried filer with a mortgage, retirement savings, and withholding",
  "params": {
    "taxYear": 2025,
    "filingStatus": "single",
    "age": 36,
    "grossIncome": 132000,
    "w2Income": 132000,
    "stateCode": "CA",
    "mortgageInterest": 14000,
    "stateLocalTaxes": 9000,
    "charitableDonations": 1800,
    "retirement401k": 18500,
    "federalWithheld": 21000,
    "hasHealthInsurance": true
  }
}
```

```json
{
  "intent": "Run a health check for a joint filer with business income, dependents, and tax-saving opportunities",
  "params": {
    "taxYear": 2025,
    "filingStatus": "married_filing_jointly",
    "grossIncome": 245000,
    "w2Income": 110000,
    "selfEmploymentIncome": 90000,
    "capitalGains": 12000,
    "stateCode": "NY",
    "dependents": 2,
    "retirement401k": 23000,
    "retirementIRA": 14000,
    "hsaContributions": 6000,
    "federalWithheld": 26000,
    "boughtEV": true,
    "installedSolar": true
  }
}
