## irs-taxpayer-mcp_list_deductions

### What this tool is for
Available tax deductions along with eligibility rules and limits. Use this when the user needs to review deduction options rather than calculate a specific tax result.

---

### Used parameters

**(27) category - Optional**  
Default: all  
Deduction category used to filter the listed deductions.

---

### JSON input alternatives

```json
{
  "tool": "irs-taxpayer-mcp_list_deductions",
  "intent": "List all available tax deductions",
  "params": {}
}
```

```json
{
  "tool": "irs-taxpayer-mcp_list_deductions",
  "intent": "List charitable deductions",
  "params": {
    "category": "charity"
  }
}
```
