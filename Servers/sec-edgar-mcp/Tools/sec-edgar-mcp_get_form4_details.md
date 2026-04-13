## sec-edgar-mcp_get_form4_details

### What this tool is used for
Gets detailed information from a specific Form 4 filing.

---

### Used parameters

**(2) identifier: Required**
Default: No default
Company ticker symbol or CIK number used to identify the company.

**(5) accession_number: Required**
Default: No default
Accession number of the Form 4 filing to retrieve.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve details from a specific Form 4 filing for NVIDIA",
  "params": {
    "identifier": "NVDA",
    "accession_number": "0001045810-24-000123"
  }
}
```

```json
{
  "intent": "Retrieve details from a specific Form 4 filing using a company CIK",
  "params": {
    "identifier": "0001045810",
    "accession_number": "0001045810-24-000123"
  }
}
```
