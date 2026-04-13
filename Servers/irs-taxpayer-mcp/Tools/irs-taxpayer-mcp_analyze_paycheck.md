## irs-taxpayer-mcp_analyze_paycheck

### What this tool is for
A paycheck to assess withholding accuracy using pay stub figures. Use this when the user wants to check whether current federal and state withholding looks aligned with the pay period details.

---

### Used parameters

**(1) taxYear: Required**  
Default: No default  
Tax year used for the analysis.

**(2) filingStatus: Required**  
Default: No default  
Allowed: single, married_filing_jointly, married_filing_separately, head_of_household, qualifying_surviving_spouse  
Filing status used for the analysis.

**(22) payFrequency: Required**  
Default: No default  
Allowed: weekly, biweekly, semimonthly, monthly  
Pay frequency for the paycheck being analyzed.

**(115) grossPay: Required**  
Default: No default  
Gross pay for the current pay period.

**(103) federalWithheld: Required**  
Default: No default  
Federal tax withheld for the current pay period.

**(104) stateWithheld: Optional**  
Default: No default  
State tax withheld for the current pay period.

**(116) socialSecurityWithheld: Optional**  
Default: No default  
Social Security tax withheld for the current pay period.

**(117) medicareWithheld: Optional**  
Default: No default  
Medicare tax withheld for the current pay period.

**(118) retirement401k: Optional**  
Default: No default  
401(k) or 403(b) pre-tax contribution for the current pay period.

**(119) hsaContribution: Optional**  
Default: No default  
HSA contribution for the current pay period.

**(20) stateCode: Optional**  
Default: No default  
Two-letter state code for state withholding context.

---

### JSON input alternatives

```json
{
  "intent": "Analyze withholding for a biweekly paycheck",
  "params": {
    "taxYear": 2025,
    "filingStatus": "single",
    "payFrequency": "biweekly",
    "grossPay": 4200,
    "federalWithheld": 540,
    "socialSecurityWithheld": 260.4,
    "medicareWithheld": 60.9
  }
}
```

```json
{
  "intent": "Analyze a paycheck including state withholding and pre-tax contributions",
  "params": {
    "taxYear": 2025,
    "filingStatus": "married_filing_jointly",
    "payFrequency": "semimonthly",
    "grossPay": 6800,
    "federalWithheld": 710,
    "stateWithheld": 260,
    "socialSecurityWithheld": 421.6,
    "medicareWithheld": 98.6,
    "retirement401k": 400,
    "hsaContribution": 150,
    "stateCode": "CA"
  }
}
