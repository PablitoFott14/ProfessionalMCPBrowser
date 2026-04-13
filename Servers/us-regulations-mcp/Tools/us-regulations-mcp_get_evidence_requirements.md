## us-regulations-mcp_get_evidence_requirements

### What this tool is for
Audit evidence requirements from a specific regulation section. Use this after identifying the relevant section, when the user needs to understand what artifacts or records may be required for compliance or audit support.

---

### Used parameters

**(5) regulation - Required**  
Default: No default  
Regulation identifier used to select the regulation.

**(6) section - Required**  
Default: No default  
Section identifier used to retrieve and analyze the specific provision.

---

### JSON input alternatives

```json
{
  "tool": "us-regulations-mcp_get_evidence_requirements",
  "intent": "Extract audit evidence requirements from a HIPAA section",
  "params": {
    "regulation": "HIPAA",
    "section": "164.312(b)"
  }
}
```

```json
{
  "tool": "us-regulations-mcp_get_evidence_requirements",
  "intent": "Extract evidence requirements from the SOX section on internal controls",
  "params": {
    "regulation": "SOX",
    "section": "SOX-404"
  }
}
```
