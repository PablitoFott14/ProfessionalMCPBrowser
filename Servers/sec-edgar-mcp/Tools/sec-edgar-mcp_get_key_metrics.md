## sec-edgar-mcp_get_key_metrics

### What this tool is used for
Gets key financial metrics for a company.

---

### Used parameters

**(2) identifier: Required**
Default: No default
Company ticker symbol or CIK number used to identify the company.

**(10) metrics: Optional**
Default: null
List of specific metrics to retrieve.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve key financial metrics for NVIDIA",
  "params": {
    "identifier": "NVDA"
  }
}
```

```json
{
  "intent": "Retrieve specific key financial metrics for a company",
  "params": {
    "identifier": "AAPL",
    "metrics": ["revenue", "net_income", "operating_income"]
  }
}
```
