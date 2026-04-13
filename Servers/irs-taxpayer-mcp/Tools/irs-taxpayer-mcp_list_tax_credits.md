## irs-taxpayer-mcp_list_tax_credits

### What this tool is for
Available federal tax credits along with eligibility, amounts, and phase-out rules. Use this when the user needs to review credit options rather than calculate a specific tax result.

---

### Used parameters

**(27) category - Optional**  
Default: all  
Category used to filter the listed tax credits.

**(36) refundableOnly - Optional**  
Default: No default  
Flag indicating whether only refundable credits should be shown.

---

### JSON input alternatives

```json
{
  "intent": "List all available federal tax credits",
  "params": {}
}
```

```json
{
  "intent": "List refundable family-related tax credits",
  "params": {
    "category": "family",
    "refundableOnly": true
  }
}
```
