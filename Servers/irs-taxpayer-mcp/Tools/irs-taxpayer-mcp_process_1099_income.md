## irs-taxpayer-mcp_process_1099_income

### What this tool is for
Processes multiple 1099 forms and estimates the tax impact of each income type. Use this when the user needs a consolidated view of mixed 1099 income rather than handling each form type separately.

---

### Used parameters

**(1) taxYear - Required**  
Default: No default  
Tax year used for the analysis.

**(2) filingStatus - Required**  
Default: No default  
Filing status used for the analysis.

**(4) w2Income - Optional**  
Default: No default  
W-2 income included for context.

**(106) forms - Required**  
Default: No default  
Array of 1099 form entries used in the analysis.

**(107) payer - Optional**  
Default: No default  
Payer name within a form entry.

**(108) amount - Required**  
Default: No default  
Total amount within a form entry.

**(109) qualifiedDividendsForm - Optional**  
Default: No default  
Qualified dividends amount within a 1099-DIV entry.

**(110) longTerm - Optional**  
Default: No default  
Flag indicating whether a 1099-B gain is long-term.

---

### JSON input alternatives

```json
{
  "intent": "Process freelance and interest income reported on 1099 forms",
  "params": {
    "taxYear": 2024,
    "filingStatus": "single",
    "forms": [
      {
        "type": "1099-NEC",
        "payer": "Acme Consulting",
        "amount": 28000
      },
      {
        "type": "1099-INT",
        "payer": "First Bank",
        "amount": 650
      }
    ]
  }
}
```

```json
{
  "intent": "Process mixed 1099 income with W-2 context and investment income details",
  "params": {
    "taxYear": 2025,
    "filingStatus": "married_filing_jointly",
    "w2Income": 90000,
    "forms": [
      {
        "type": "1099-DIV",
        "payer": "Brokerage A",
        "amount": 3200,
        "qualifiedDividends": 2400
      },
      {
        "type": "1099-B",
        "payer": "Brokerage B",
        "amount": 7500,
        "longTerm": true
      },
      {
        "type": "1099-MISC",
        "payer": "Marketplace Platform",
        "amount": 1800
      }
    ]
  }
}
