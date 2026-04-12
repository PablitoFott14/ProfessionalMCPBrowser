## us-regulations-mcp_list_regulations

### What this tool is for
Lists the available regulations or returns the structure of a specific regulation. Use this when the user needs to discover valid regulation IDs or inspect a regulation's chapters and section numbers before retrieving a specific section.

---

### Used parameters

**(5) regulation - Optional**  
Default: null  
Regulation identifier used to return the structure of a specific regulation.

---

### JSON input alternatives

```json
{
  "intent": "List all available regulations",
  "params": {}
}
```

```json
{
  "intent": "Get the structure of the HIPAA regulation",
  "params": {
    "regulation": "HIPAA"
  }
}
```
