## us-regulations-mcp_get_breach_notification_timeline

### What this tool is for
Retrieves breach notification timelines across supported federal and state jurisdictions. Use this when the user needs to review notification deadlines, recipients, penalties, or thresholds by jurisdiction or regulation.

---

### Used parameters

**(13) state - Optional**  
Default: null  
State or jurisdiction name used to narrow the results.

**(5) regulation - Optional**  
Default: null  
Regulation identifier used to filter the returned breach notification rules.

---

### JSON input alternatives

```json
{
  "tool": "us-regulations-mcp_get_breach_notification_timeline",
  "intent": "Get breach notification timelines across all supported jurisdictions",
  "params": {}
}
```

```json
{
  "tool": "us-regulations-mcp_get_breach_notification_timeline",
  "intent": "Get California breach notification timelines for HIPAA-related rules",
  "params": {
    "state": "California",
    "regulation": "HIPAA"
  }
}
```
