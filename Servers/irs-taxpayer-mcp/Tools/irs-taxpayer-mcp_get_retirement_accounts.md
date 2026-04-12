## irs-taxpayer-mcp_get_retirement_accounts

### What this tool is for
Returns details on retirement account types, including contribution limits, tax treatment, income limits, and related guidance. Use this when the user needs account-type reference information rather than a tax calculation.

---

### Used parameters

**(49) accountType - Optional**  
Default: No default  
Specific retirement account type used to narrow the returned information.

---

### JSON input alternatives

```json
{
  "intent": "List retirement account details across available account types",
  "params": {}
}
```

```json
{
  "intent": "Get details for a Roth IRA",
  "params": {
    "accountType": "roth_ira"
  }
}
```
