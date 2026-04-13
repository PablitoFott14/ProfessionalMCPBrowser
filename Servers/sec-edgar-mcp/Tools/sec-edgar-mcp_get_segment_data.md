## sec-edgar-mcp_get_segment_data

### What this tool is used for
Gets revenue breakdown by segments, such as geographic or product segments.

---

### Used parameters

**(2) identifier: Required**
Default: No default
Company ticker symbol or CIK number used to identify the company.

**(9) segment_type: Optional**
Default: geographic
Type of segment analysis to retrieve.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve geographic segment revenue data for NVIDIA",
  "params": {
    "identifier": "NVDA"
  }
}
```

```json
{
  "intent": "Retrieve product segment revenue data for a company",
  "params": {
    "identifier": "AAPL",
    "segment_type": "product"
  }
}
```
