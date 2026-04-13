## irs-taxpayer-mcp_plan_multi_year_taxes

### What this tool is for
A multi-year tax projection across a three- to five-year planning horizon. Use this when the user wants to compare bracket management, Roth conversions, retirement contributions, and income changes over multiple tax years rather than evaluating a single year in isolation.

---

### Used parameters

**(2) filingStatus - Required**  
Default: No default  
Allowed: single, married_filing_jointly, married_filing_separately, head_of_household, qualifying_surviving_spouse  
Filing status used throughout the projection.

**(170) currentAge - Required**  
Default: No default  
Current age used as the starting point for the projection.

**(171) years - Required**  
Default: No default  
Array of year-by-year projection entries.

**(172) year - Required**  
Default: No default  
Tax year within a projection entry.

**(173) expectedIncome - Required**  
Default: No default  
Expected gross income within a projection entry.

**(5) selfEmploymentIncome - Optional**  
Default: No default  
Self-employment income within a projection entry.

**(174) plannedRothConversion - Optional**  
Default: No default  
Planned Roth conversion amount within a projection entry.

**(175) planned401k - Optional**  
Default: No default  
Planned 401(k) contribution within a projection entry.

**(176) plannedIRA - Optional**  
Default: No default  
Planned IRA contribution within a projection entry.

**(12) dependents - Optional**  
Default: No default  
Number of dependents within a projection entry.

**(20) stateCode - Optional**  
Default: No default  
State code within a projection entry.

---

### JSON input alternatives

```json
{
  "intent": "Project taxes over the next three years with rising income and steady retirement contributions",
  "params": {
    "filingStatus": "single",
    "currentAge": 41,
    "years": [
      {
        "year": 2025,
        "expectedIncome": 135000,
        "planned401k": 23000,
        "plannedIRA": 7000,
        "stateCode": "CA"
      },
      {
        "year": 2026,
        "expectedIncome": 148000,
        "planned401k": 23000,
        "plannedIRA": 7000,
        "stateCode": "CA"
      },
      {
        "year": 2027,
        "expectedIncome": 160000,
        "planned401k": 23000,
        "plannedIRA": 7000,
        "stateCode": "CA"
      }
    ]
  }
}
```

```json
{
  "intent": "Project a joint filer's taxes across several years with Roth conversions and state changes",
  "params": {
    "filingStatus": "married_filing_jointly",
    "currentAge": 59,
    "years": [
      {
        "year": 2025,
        "expectedIncome": 180000,
        "plannedRothConversion": 25000,
        "planned401k": 30000,
        "dependents": 1,
        "stateCode": "NY"
      },
      {
        "year": 2026,
        "expectedIncome": 145000,
        "plannedRothConversion": 40000,
        "plannedIRA": 16000,
        "stateCode": "FL"
      },
      {
        "year": 2027,
        "expectedIncome": 132000,
        "selfEmploymentIncome": 18000,
        "plannedRothConversion": 30000,
        "stateCode": "FL"
      }
    ]
  }
}
