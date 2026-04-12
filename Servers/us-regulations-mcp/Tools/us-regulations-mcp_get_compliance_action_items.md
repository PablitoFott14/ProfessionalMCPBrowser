## us-regulations-mcp_get_compliance_action_items

### What this tool is for
Generates prioritized compliance action items from one or more regulation sections. Use this after relevant sections have been identified, when the user needs concrete compliance follow-up items tied to those sections.

---

### Used parameters

**(5) regulation - Required**  
Default: No default  
Regulation identifier used to select the regulation.

**(12) sections - Required**  
Default: No default  
List of section identifiers used to generate action items.

---

### JSON input alternatives

```json
{
  "intent": "Generate compliance action items from selected HIPAA sections",
  "params": {
    "regulation": "HIPAA",
    "sections": ["164.308(a)(1)(ii)(A)", "164.312(b)"]
  }
}
```

```json
{
  "intent": "Generate action items from selected GLBA sections",
  "params": {
    "regulation": "GLBA",
    "sections": ["314.4", "314.6"]
  }
}
```
