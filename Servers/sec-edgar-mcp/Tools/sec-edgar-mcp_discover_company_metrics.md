## sec-edgar-mcp_discover_company_metrics

### What this tool is used for
Discovers available financial metrics for a company.

---

### Used parameters

**(2) identifier: Required**
Default: No default
Company ticker symbol or CIK number used to identify the company.

**(14) search_term: Optional**
Default: null
Search term used to filter the available metrics.

---

### JSON input alternatives

```json
{
  "intent": "Discover available financial metrics for NVIDIA",
  "params": {
    "identifier": "NVDA"
  }
}
```

```json
{
  "intent": "Discover available company metrics related to revenue",
  "params": {
    "identifier": "AAPL",
    "search_term": "revenue"
  }
}
```
