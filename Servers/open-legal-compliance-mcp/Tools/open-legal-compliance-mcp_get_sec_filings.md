## open-legal-compliance-mcp_get_sec_filings

### What this tool is used for
Retrieves SEC filings for a company by its Central Index Key (CIK). Use it when accessing a company's full filing history from EDGAR using a known CIK number.

---

### Used parameters

**(8) cik: Required**
Default: No default
SEC Central Index Key for the company to retrieve filings for (10 digits).

---

### JSON input alternatives

```json
{
  "intent": "Retrieve SEC filings for a company by CIK",
  "params": {
    "cik": "0000320193"
  }
}
```

```json
{
  "intent": "Fetch the filing history for a known company from EDGAR",
  "params": {
    "cik": "0001018724"
  }
}
```
