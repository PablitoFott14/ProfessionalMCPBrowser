## irs-taxpayer-mcp_get_tax_brackets

### What this tool is for
Federal income tax brackets and the standard deduction for a given tax year and filing status. Use this when the user needs the baseline tax schedule inputs without running a full tax calculation.

---

### Used parameters

**(1) taxYear - Required**  
Default: No default  
Tax year used to retrieve the bracket schedule.

**(2) filingStatus - Required**  
Default: No default  
Allowed: single, married_filing_jointly, married_filing_separately, head_of_household, qualifying_surviving_spouse  
Filing status used to retrieve the bracket schedule.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve 2024 tax brackets for a single filer",
  "params": {
    "taxYear": 2024,
    "filingStatus": "single"
  }
}
```

```json
{
  "intent": "Retrieve 2025 tax brackets for a head of household filer",
  "params": {
    "taxYear": 2025,
    "filingStatus": "head_of_household"
  }
}
```
