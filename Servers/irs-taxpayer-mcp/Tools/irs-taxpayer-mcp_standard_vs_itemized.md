## irs-taxpayer-mcp_standard_vs_itemized

### What this tool is for
The standard deduction against itemized deductions to determine which is more beneficial. Use this when the user needs to evaluate whether itemizing deductions is likely to produce a better tax outcome.

---

### Used parameters

**(1) taxYear: Required**  
Default: No default  
Tax year used for the comparison.

**(2) filingStatus: Required**  
Default: No default  
Allowed: single, married_filing_jointly, married_filing_separately, head_of_household, qualifying_surviving_spouse  
Filing status used for the comparison.

**(28) medicalExpenses: Optional**  
Default: No default  
Unreimbursed medical expenses included in the itemized total.

**(29) stateLocalTaxes: Optional**  
Default: No default  
State and local taxes included in the itemized total.

**(30) mortgageInterest: Optional**  
Default: No default  
Mortgage interest included in the itemized total.

**(31) charitableDonations: Optional**  
Default: No default  
Charitable contributions included in the itemized total.

**(32) otherItemized: Optional**  
Default: No default  
Other itemized deductions included in the comparison.

**(33) agi: Required**  
Default: No default  
Adjusted Gross Income used for the medical expense threshold.

**(13) age65OrOlder: Optional**  
Default: No default  
Flag indicating whether the taxpayer is age 65 or older.

**(14) blind: Optional**  
Default: No default  
Flag indicating whether the taxpayer is blind.

---

### JSON input alternatives

```json
{
  "intent": "Compare standard and itemized deductions for a single filer with mortgage interest and charitable giving",
  "params": {
    "taxYear": 2024,
    "filingStatus": "single",
    "agi": 95000,
    "mortgageInterest": 11000,
    "charitableDonations": 2500
  }
}
```

```json
{
  "intent": "Compare standard and itemized deductions for a head of household filer with medical expenses and state taxes",
  "params": {
    "taxYear": 2025,
    "filingStatus": "head_of_household",
    "agi": 120000,
    "medicalExpenses": 14000,
    "stateLocalTaxes": 9000,
    "otherItemized": 1200,
    "age65OrOlder": true
  }
}
```
