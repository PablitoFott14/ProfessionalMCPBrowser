## sec-edgar-mcp_get_company_info

### What this tool is used for
Gets detailed company information from SEC records using a ticker symbol or CIK number.

---

### Used parameters

**(2) identifier: Required**
Default: No default
Company ticker symbol or CIK number to look up in SEC records.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve SEC company information for NVIDIA using its ticker",
  "params": {
    "identifier": "NVDA"
  }
}
```

```json
{
  "intent": "Retrieve SEC company information for a company using its CIK",
  "params": {
    "identifier": "0001045810"
  }
}
```
