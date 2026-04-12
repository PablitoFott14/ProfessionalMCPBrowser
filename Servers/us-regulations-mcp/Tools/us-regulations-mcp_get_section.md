## us-regulations-mcp_get_section

### What this tool is for
Retrieves the full text of a specific regulation section when the regulation and section are already known. Use this after discovery, when the user needs the actual section text rather than search results.

---

### Used parameters

**(5) regulation - Required**  
Default: No default  
Regulation identifier used to select the regulation.

**(6) section - Required**  
Default: No default  
Section identifier used to retrieve the specific provision.

---

### JSON input alternatives

```json
{
  "tool": "us-regulations-mcp_get_section",
  "intent": "Retrieve the HIPAA section for uses and disclosures of protected health information",
  "params": {
    "regulation": "HIPAA",
    "section": "164.502"
  }
}
```

```json
{
  "tool": "us-regulations-mcp_get_section",
  "intent": "Retrieve the CCPA section covering consumer rights requests",
  "params": {
    "regulation": "CCPA",
    "section": "1798.100"
  }
}
```
