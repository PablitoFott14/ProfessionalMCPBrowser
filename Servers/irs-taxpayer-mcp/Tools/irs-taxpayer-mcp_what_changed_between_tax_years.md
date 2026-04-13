## irs-taxpayer-mcp_what_changed_between_tax_years

### What this tool is for
What changed between two tax years, including bracket shifts, deduction and credit changes, and new provisions. Use this when the user wants a rule-change comparison rather than a taxpayer-specific liability comparison.

---

### Used parameters

**(96) fromYear - Required**  
Default: No default  
Earlier tax year used in the comparison.

**(97) toYear - Required**  
Default: No default  
Later tax year used in the comparison.

**(2) filingStatus - Optional**  
Default: single  
Allowed: single, married_filing_jointly, married_filing_separately, head_of_household, qualifying_surviving_spouse  
Filing status used for filing-status-specific comparisons.

---

### JSON input alternatives

```json
{
  "intent": "Compare what changed between 2024 and 2025 for a single filer",
  "params": {
    "fromYear": 2024,
    "toYear": 2025
  }
}
```

```json
{
  "intent": "Compare tax law changes between 2024 and 2025 for a head of household filer",
  "params": {
    "fromYear": 2024,
    "toYear": 2025,
    "filingStatus": "head_of_household"
  }
}
```
