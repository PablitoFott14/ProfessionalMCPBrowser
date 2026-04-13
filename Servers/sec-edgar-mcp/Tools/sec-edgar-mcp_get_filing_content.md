## sec-edgar-mcp_get_filing_content

### What this tool is used for
Gets the content of a specific SEC filing.

---

### Used parameters

**(2) identifier: Required**
Default: No default
Company ticker symbol or CIK number used to identify the company.

**(5) accession_number: Required**
Default: No default
Accession number of the SEC filing to retrieve.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve the content of a specific SEC filing for NVIDIA",
  "params": {
    "identifier": "NVDA",
    "accession_number": "0001045810-24-000123"
  }
}
```

```json
{
  "intent": "Retrieve a specific SEC filing using a company CIK and accession number",
  "params": {
    "identifier": "0001045810",
    "accession_number": "0001045810-24-000123"
  }
}
```
