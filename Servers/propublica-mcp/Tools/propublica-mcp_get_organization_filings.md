## propublica-mcp_get_organization_filings

### What this tool is used for
Retrieves Form 990 filings for a specific nonprofit organization from ProPublica. Use it when accessing a nonprofit's tax filing history and the financial data contained within each filing.

---

### Used parameters

**(7) ein: Required**
Default: No default
Employer Identification Number of the nonprofit (9 digits, with or without hyphen).

**(9) limit: Optional**
Default: 10
Maximum number of filings to retrieve. Maximum: 100 for this tool.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve the most recent Form 990 filings for a nonprofit",
  "params": {
    "ein": "131655952"
  }
}
```

```json
{
  "intent": "Retrieve a larger set of historical Form 990 filings for a nonprofit",
  "params": {
    "ein": "131655952",
    "limit": 50
  }
}
```
