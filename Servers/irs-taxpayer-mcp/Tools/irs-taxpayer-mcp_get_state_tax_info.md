## irs-taxpayer-mcp_get_state_tax_info

### What this tool is for
State income tax information, including rates, brackets, and key details for a given US state. Use this when the user needs state tax reference information rather than a combined tax calculation.

---

### Used parameters

**(20) stateCode - Required**  
Default: No default  
Two-letter state code used to retrieve the state tax information.

---

### JSON input alternatives

```json
{
  "intent": "Get state income tax information for California",
  "params": {
    "stateCode": "CA"
  }
}
```

```json
{
  "intent": "Get state income tax information for Texas",
  "params": {
    "stateCode": "TX"
  }
}
```
