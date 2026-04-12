## us-regulations-mcp_check_applicability

### What this tool is for
Determines which regulations may apply to a given industry sector. Use this as a starting point when the user needs a regulation applicability view before moving into specific regulation text or section-level research.

---

### Used parameters

**(8) sector - Required**  
Default: No default  
Industry sector used to check regulatory applicability.

**(9) subsector - Optional**  
Default: null  
More specific industry classification used to refine the applicability result.

---

### JSON input alternatives

```json
{
  "intent": "Check which regulations apply to the healthcare sector",
  "params": {
    "sector": "healthcare"
  }
}
```

```json
{
  "intent": "Check which regulations apply to hospitals within the healthcare sector",
  "params": {
    "sector": "healthcare",
    "subsector": "hospital"
  }
}
```
