## irs-taxpayer-mcp_get_irs_form_info

### What this tool is for
Information about common IRS tax forms, including what they are, who typically needs them, and where to find them. Use this when the user needs form guidance rather than a tax calculation.

---

### Used parameters

**(35) formNumber - Required**  
Default: No default  
IRS form number used to look up the form information.

---

### JSON input alternatives

```json
{
  "intent": "Get information about Form 1040",
  "params": {
    "formNumber": "1040"
  }
}
```

```json
{
  "intent": "Get information about Schedule C",
  "params": {
    "formNumber": "Schedule C"
  }
}
```
