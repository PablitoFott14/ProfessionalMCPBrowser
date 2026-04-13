## irs-taxpayer-mcp_simulate_tax_scenario

### What this tool is for
A what-if tax scenario by comparing a current baseline against a hypothetical change. Use this when the user wants to see the tax impact of changes such as income shifts, relocation, Roth conversions, filing-status changes, or deduction changes.

---

### Used parameters

**(1) taxYear - Required**  
Default: No default  
Tax year used for the scenario comparison.

**(2) filingStatus - Required**  
Default: No default  
Allowed: single, married_filing_jointly, married_filing_separately, head_of_household, qualifying_surviving_spouse  
Current filing status used as the baseline.

**(120) currentIncome - Required**  
Default: No default  
Current gross income used as the baseline.

**(121) currentState - Optional**  
Default: No default  
Current state code used as the baseline location.

**(122) currentSelfEmployment - Optional**  
Default: No default  
Current self-employment income used as the baseline.

**(123) currentCapitalGains - Optional**  
Default: No default  
Current capital gains used as the baseline.

**(124) currentItemizedDeductions - Optional**  
Default: No default  
Current itemized deductions used as the baseline.

**(125) currentDependents - Optional**  
Default: No default  
Current number of dependents used as the baseline.

**(126) whatIfIncomeChange - Optional**  
Default: No default  
Hypothetical change in income.

**(127) whatIfNewState - Optional**  
Default: No default  
Hypothetical new state code.

**(128) whatIfFilingStatus - Optional**  
Default: No default  
Allowed: single, married_filing_jointly, married_filing_separately, head_of_household, qualifying_surviving_spouse  
Hypothetical new filing status.

**(129) whatIfRothConversion - Optional**  
Default: No default  
Hypothetical Roth conversion amount.

**(130) whatIfAdditional401k - Optional**  
Default: No default  
Hypothetical additional 401(k) contribution.

**(131) whatIfNewDependents - Optional**  
Default: No default  
Hypothetical new number of dependents.

**(132) whatIfItemizedChange - Optional**  
Default: No default  
Hypothetical change in itemized deductions.

---

### JSON input alternatives

```json
{
  "tool": "irs-taxpayer-mcp_simulate_tax_scenario",
  "intent": "Estimate the tax impact of relocating from California to Texas",
  "params": {
    "taxYear": 2025,
    "filingStatus": "single",
    "currentIncome": 140000,
    "currentState": "CA",
    "whatIfNewState": "TX"
  }
}
```

```json
{
  "tool": "irs-taxpayer-mcp_simulate_tax_scenario",
  "intent": "Estimate the tax impact of a raise, Roth conversion, and extra 401k contributions",
  "params": {
    "taxYear": 2025,
    "filingStatus": "married_filing_jointly",
    "currentIncome": 220000,
    "currentState": "NY",
    "currentDependents": 2,
    "whatIfIncomeChange": 25000,
    "whatIfRothConversion": 30000,
    "whatIfAdditional401k": 6000
  }
}
