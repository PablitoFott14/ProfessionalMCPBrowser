## sec-edgar-mcp_discover_xbrl_concepts

### What this tool is used for
Discovers all available XBRL concepts in a filing, including company-specific concepts.

---

### Used parameters

**(2) identifier: Required**
Default: No default
Company ticker symbol or CIK number used to identify the company.

**(5) accession_number: Optional**
Default: null
Specific filing accession number to inspect for XBRL concepts.

**(6) form_type: Optional**
Default: 10-K
Form type to use when no accession number is provided.

**(15) namespace_filter: Optional**
Default: null
Filter to show only concepts from a specific namespace.

---

### JSON input alternatives

```json
{
  "intent": "Discover all XBRL concepts in a specific filing for NVIDIA",
  "params": {
    "identifier": "NVDA",
    "accession_number": "0001045810-24-000123"
  }
}
```

```json
{
  "intent": "Discover XBRL concepts from a recent 10-Q filing and filter by namespace",
  "params": {
    "identifier": "AAPL",
    "form_type": "10-Q",
    "namespace_filter": "us-gaap"
  }
}
```
