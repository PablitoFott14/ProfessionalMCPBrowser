## propublica-mcp_get_organization

### What this tool is used for
Retrieves detailed information about a specific nonprofit organization by its EIN from the ProPublica Nonprofit Explorer. Use it when the EIN is already known and full organization details are needed.

---

### Used parameters

**(7) ein: Required**
Default: No default
Employer Identification Number of the nonprofit to retrieve (9 digits, with or without hyphen).

---

### JSON input alternatives

```json
{
  "intent": "Retrieve detailed information for a nonprofit by EIN",
  "params": {
    "ein": "131655952"
  }
}
```

```json
{
  "intent": "Look up a nonprofit organization using its hyphenated EIN",
  "params": {
    "ein": "13-1655952"
  }
}
```
