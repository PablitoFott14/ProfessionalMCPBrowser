## irs-taxpayer-mcp_get_tax_document_checklist

### What this tool is for
Generates a personalized checklist of tax documents to gather before filing. Use this when the user wants a filing-prep checklist based on income sources, deductions, credits, and major life events.

---

### Used parameters

**(144) hasW2 - Optional**  
Default: No default  
Flag indicating whether the taxpayer has W-2 employment.

**(145) hasSelfEmployment - Optional**  
Default: No default  
Flag indicating whether the taxpayer has self-employment or freelance income.

**(113) hasInvestments - Optional**  
Default: No default  
Flag indicating whether the taxpayer has investment accounts.

**(146) hasRentalProperty - Optional**  
Default: No default  
Flag indicating whether the taxpayer owns rental property.

**(62) hasMortgage - Optional**  
Default: No default  
Flag indicating whether the taxpayer has a mortgage.

**(41) hasStudentLoans - Optional**  
Default: No default  
Flag indicating whether the taxpayer pays student loan interest.

**(37) hasChildren - Optional**  
Default: No default  
Flag indicating whether the taxpayer has dependent children.

**(39) hasChildcare - Optional**  
Default: No default  
Flag indicating whether the taxpayer pays for childcare.

**(147) hasEducationExpenses - Optional**  
Default: No default  
Flag indicating whether the taxpayer has tuition or other education expenses.

**(148) hasHealthInsurance - Optional**  
Default: No default  
Flag indicating whether the taxpayer has health insurance relevant to tax filing.

**(60) hasHSA - Optional**  
Default: No default  
Flag indicating whether the taxpayer has an HSA-eligible account or plan context.

**(45) hasRetirementContributions - Optional**  
Default: No default  
Flag indicating whether the taxpayer made retirement contributions.

**(149) hasCharitableDonations - Optional**  
Default: No default  
Flag indicating whether the taxpayer made charitable donations.

**(150) hasForeignAccounts - Optional**  
Default: No default  
Flag indicating whether the taxpayer has foreign bank accounts or foreign income.

**(151) soldHome - Optional**  
Default: No default  
Flag indicating whether the taxpayer sold a home during the year.

**(152) gotMarried - Optional**  
Default: No default  
Flag indicating whether the taxpayer got married during the year.

**(153) gotDivorced - Optional**  
Default: No default  
Flag indicating whether the taxpayer got divorced during the year.

**(154) hadBaby - Optional**  
Default: No default  
Flag indicating whether the taxpayer had a baby during the year.

**(42) boughtEV - Optional**  
Default: No default  
Flag indicating whether the taxpayer bought an electric vehicle.

**(44) installedSolar - Optional**  
Default: No default  
Flag indicating whether the taxpayer installed solar or renewable energy.

---

### JSON input alternatives

```json
{
  "intent": "Generate a checklist for a salaried filer with investments, mortgage, and children",
  "params": {
    "hasW2": true,
    "hasInvestments": true,
    "hasMortgage": true,
    "hasChildren": true,
    "hasChildcare": true,
    "hasHealthInsurance": true,
    "hasRetirementContributions": true
  }
}
```

```json
{
  "intent": "Generate a checklist for a freelancer with rental property, student loans, and recent life events",
  "params": {
    "hasSelfEmployment": true,
    "hasRentalProperty": true,
    "hasStudentLoans": true,
    "hasEducationExpenses": true,
    "hasCharitableDonations": true,
    "gotMarried": true,
    "boughtEV": true,
    "installedSolar": true
  }
}
```
