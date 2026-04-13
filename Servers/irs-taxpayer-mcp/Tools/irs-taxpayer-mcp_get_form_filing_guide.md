## irs-taxpayer-mcp_get_form_filing_guide

### What this tool is for
A step-by-step guide for completing a specific IRS form or schedule. Use this when the user needs form-by-form filing guidance rather than a short form summary.

---

### Used parameters

**(35) formNumber - Required**  
Default: No default  
IRS form or schedule to explain.

---

### JSON input alternatives

```json
{
  "tool": "irs-taxpayer-mcp_get_form_filing_guide",
  "intent": "Get a filing guide for Form 1040",
  "params": {
    "formNumber": "1040"
  }
}
```

```json
{
  "tool": "irs-taxpayer-mcp_get_form_filing_guide",
  "intent": "Get a filing guide for Schedule C",
  "params": {
    "formNumber": "Schedule C"
  }
}
