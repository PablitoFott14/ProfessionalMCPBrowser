## propublica-mcp_get_most_recent_pdf

### What this tool is used for
Retrieves the most recent Form 990 PDF filing available for a specific nonprofit by searching backwards through its filing history. Use it when the latest available PDF of a nonprofit's tax return is needed directly.

---

### Used parameters

**(7) ein: Required**
Default: No default
Employer Identification Number of the nonprofit (9 digits, with or without hyphen).

---

### JSON input alternatives

```json
{
  "intent": "Get the most recent Form 990 PDF for a nonprofit by EIN",
  "params": {
    "ein": "131655952"
  }
}
```

```json
{
  "intent": "Retrieve the latest available PDF filing for a known nonprofit",
  "params": {
    "ein": "13-1655952"
  }
}
```
