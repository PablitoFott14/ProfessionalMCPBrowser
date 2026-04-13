## irs-taxpayer-mcp_get_tax_planning_tips

### What this tool is for
Year-end tax optimization strategies based on the taxpayer's income, withholding, deductions, and overall situation. Use this when the user wants planning ideas to reduce tax liability before year-end rather than a static calculation alone.

---

### Used parameters

**(1) taxYear - Required**  
Default: No default  
Tax year used for the planning recommendations.

**(2) filingStatus - Required**  
Default: No default  
Allowed: single, married_filing_jointly, married_filing_separately, head_of_household, qualifying_surviving_spouse  
Filing status used for the planning recommendations.

**(56) estimatedIncome - Required**  
Default: No default  
Expected total income for the year.

**(57) currentWithholding - Optional**  
Default: No default  
Total tax already withheld or paid year to date.

**(58) hasRetirementPlan - Optional**  
Default: No default  
Flag indicating whether the taxpayer has access to a workplace retirement plan.

**(59) currentRetirementContributions - Optional**  
Default: No default  
Year-to-date retirement contributions.

**(60) hasHSA - Optional**  
Default: No default  
Flag indicating whether the taxpayer has an HSA-eligible plan.

**(61) currentHSAContributions - Optional**  
Default: No default  
Year-to-date HSA contributions.

**(62) hasMortgage - Optional**  
Default: No default  
Flag indicating whether the taxpayer has a mortgage.

**(63) estimatedItemizedDeductions - Optional**  
Default: No default  
Estimated total itemized deductions.

**(64) hasCapitalGains - Optional**  
Default: No default  
Flag indicating whether the taxpayer expects capital gains.

**(65) estimatedCapitalGains - Optional**  
Default: No default  
Estimated capital gains.

**(66) hasCapitalLosses - Optional**  
Default: No default  
Flag indicating whether the taxpayer expects capital losses.

**(67) isSelfEmployed - Optional**  
Default: No default  
Flag indicating whether the taxpayer is self-employed.

**(68) charitableGiving - Optional**  
Default: No default  
Year-to-date charitable donations.

---

### JSON input alternatives

```json
{
  "tool": "irs-taxpayer-mcp_get_tax_planning_tips",
  "intent": "Get year-end tax planning ideas for a salaried single filer",
  "params": {
    "taxYear": 2024,
    "filingStatus": "single",
    "estimatedIncome": 125000,
    "currentWithholding": 18000,
    "hasRetirementPlan": true,
    "currentRetirementContributions": 12000,
    "hasHSA": true,
    "currentHSAContributions": 2500
  }
}
```

```json
{
  "tool": "irs-taxpayer-mcp_get_tax_planning_tips",
  "intent": "Get year-end tax planning ideas for a self-employed joint filer with gains and charitable giving",
  "params": {
    "taxYear": 2025,
    "filingStatus": "married_filing_jointly",
    "estimatedIncome": 260000,
    "isSelfEmployed": true,
    "hasCapitalGains": true,
    "estimatedCapitalGains": 18000,
    "charitableGiving": 6000,
    "estimatedItemizedDeductions": 24000
  }
}
```
