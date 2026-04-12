## irs-taxpayer-mcp_get_personalized_tax_calendar

### What this tool is for
Generates a personalized tax calendar based on the taxpayer's situation. Use this when the user needs a tailored schedule of deadlines, estimated payments, extensions, and other tax-related actions.

---

### Used parameters

**(1) taxYear - Required**  
Default: No default  
Tax year used for the calendar.

**(67) isSelfEmployed - Optional**  
Default: No default  
Flag indicating whether the taxpayer has self-employment income.

**(111) filedExtension - Optional**  
Default: No default  
Flag indicating whether the taxpayer filed an extension.

**(112) hasEmployer - Optional**  
Default: No default  
Flag indicating whether the taxpayer has W-2 employment.

**(113) hasInvestments - Optional**  
Default: No default  
Flag indicating whether the taxpayer has investment accounts.

**(114) hasRentalIncome - Optional**  
Default: No default  
Flag indicating whether the taxpayer has rental property income.

---

### JSON input alternatives

```json
{
  "intent": "Generate a basic personalized tax calendar for a wage earner",
  "params": {
    "taxYear": 2025,
    "hasEmployer": true
  }
}
```

```json
{
  "intent": "Generate a personalized tax calendar for a self-employed taxpayer with investments and a filed extension",
  "params": {
    "taxYear": 2025,
    "isSelfEmployed": true,
    "filedExtension": true,
    "hasInvestments": true,
    "hasRentalIncome": true
  }
}
