## irs-taxpayer-mcp_get_tax_deadlines

### What this tool is for
Returns important IRS tax deadlines and due dates for a given tax year. Use this when the user needs a deadline reference rather than a tax calculation or deduction analysis.

---

### Used parameters

**(1) taxYear - Optional**  
Default: 2025  
Tax year used to retrieve the relevant IRS deadlines.

---

### JSON input alternatives

```json
{
  "intent": "Get IRS tax deadlines for the default tax year",
  "params": {}
}
```

```json
{
  "intent": "Get IRS tax deadlines for 2024",
  "params": {
    "taxYear": 2024
  }
}
```
