## us-regulations-mcp_compare_requirements

### What this tool is for
How multiple regulations address the same topic across their relevant sections. Use this when the user needs a cross-regulation view of the same requirement area rather than a search within a single regulation.

---

### Used parameters

**(7) topic - Required**  
Default: No default  
Topic used to compare regulatory treatment across multiple regulations.

**(2) regulations - Required**  
Default: No default  
List of regulation identifiers to include in the comparison.

---

### JSON input alternatives

```json
{
  "tool": "us-regulations-mcp_compare_requirements",
  "intent": "Compare how regulations address breach notification",
  "params": {
    "topic": "breach notification",
    "regulations": ["HIPAA", "CCPA", "GLBA"]
  }
}
```

```json
{
  "tool": "us-regulations-mcp_compare_requirements",
  "intent": "Compare access control requirements across multiple regulations",
  "params": {
    "topic": "access controls",
    "regulations": ["HIPAA", "SOX", "GLBA"]
  }
}
```
