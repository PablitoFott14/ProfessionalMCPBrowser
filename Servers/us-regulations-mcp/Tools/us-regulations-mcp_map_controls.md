## us-regulations-mcp_map_controls

### What this tool is for
Maps control framework objectives to relevant regulation sections for compliance mapping and gap analysis. Use this when the user needs to connect a control framework to specific regulatory requirements.

---

### Used parameters

**(10) framework - Required**  
Default: No default  
Control framework used as the source for the mapping request.

**(11) control - Optional**  
Default: null  
Specific control identifier used to narrow the mapping results.

**(5) regulation - Optional**  
Default: null  
Regulation identifier used to limit mappings to a specific regulation.

---

### JSON input alternatives

```json
{
  "tool": "us-regulations-mcp_map_controls",
  "intent": "Map NIST CSF controls to relevant regulations",
  "params": {
    "framework": "NIST_CSF"
  }
}
```

```json
{
  "tool": "us-regulations-mcp_map_controls",
  "intent": "Map a specific NIST 800-53 control to HIPAA sections",
  "params": {
    "framework": "NIST_800_53_R5",
    "control": "AC-1",
    "regulation": "HIPAA"
  }
}
```
