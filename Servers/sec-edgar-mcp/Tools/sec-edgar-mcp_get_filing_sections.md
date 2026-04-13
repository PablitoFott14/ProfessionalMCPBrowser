## sec-edgar-mcp_get_filing_sections

### What this tool is used for
Gets specific sections from a filing, such as the business description, risk factors, or MD&A.

---

### Used parameters

**(2) identifier: Required**
Default: No default
Company ticker symbol or CIK number used to identify the company.

**(5) accession_number: Required**
Default: No default
Accession number of the filing to retrieve sections from.

**(6) form_type: Required**
Default: No default
Type of SEC form for the filing.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve sections from a specific NVIDIA 10-K filing",
  "params": {
    "identifier": "NVDA",
    "accession_number": "0001045810-24-000123",
    "form_type": "10-K"
  }
}
```

```json
{
  "intent": "Retrieve sections from a specific filing using a company CIK and form type",
  "params": {
    "identifier": "0001045810",
    "accession_number": "0001045810-24-000123",
    "form_type": "10-Q"
  }
}
```
