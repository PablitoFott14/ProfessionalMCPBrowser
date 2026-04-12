## us-regulations-mcp_compare_requirements

### What this tool is for
Compares how multiple regulations address the same topic across their relevant sections. Use this when the user needs a cross-regulation view of the same requirement area rather than a search within a single regulation.

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
  "intent": "Compare how regulations address breach notification",
  "params": {
    "topic": "breach notification",
    "regulations": ["HIPAA", "CCPA", "GLBA"]
  }
}
```

```json
{
  "intent": "Compare access control requirements across multiple regulations",
  "params": {
    "topic": "access controls",
    "regulations": ["HIPAA", "SOX", "GLBA"]
  }
}
```
