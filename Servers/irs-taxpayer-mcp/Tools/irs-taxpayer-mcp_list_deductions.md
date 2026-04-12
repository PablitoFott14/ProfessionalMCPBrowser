## irs-taxpayer-mcp_list_deductions

### What this tool is for
Lists available tax deductions along with eligibility rules and limits. Use this when the user needs to review deduction options rather than calculate a specific tax result.

---

### Used parameters

**(27) category - Optional**  
Default: all  
Deduction category used to filter the listed deductions.

---

### JSON input alternatives

```json
{
  "intent": "List all available tax deductions",
  "params": {}
}
```

```json
{
  "intent": "List charitable deductions",
  "params": {
    "category": "charity"
  }
}
```
