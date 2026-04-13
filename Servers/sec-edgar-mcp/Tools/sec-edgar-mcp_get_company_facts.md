## sec-edgar-mcp_get_company_facts

### What this tool is used for
Gets company facts and key financial metrics.

---

### Used parameters

**(2) identifier: Required**
Default: No default
Company ticker symbol or CIK number to use for retrieving company facts.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve company facts and financial metrics for NVIDIA",
  "params": {
    "identifier": "NVDA"
  }
}
```

```json
{
  "intent": "Retrieve company facts and financial metrics using a CIK number",
  "params": {
    "identifier": "0001045810"
  }
}
```
