## sec-edgar-mcp_get_recommended_tools

### What this tool is used for
Gets recommended tools for analyzing specific SEC form types.

---

### Used parameters

**(6) form_type: Required**
Default: No default
SEC form type to get recommended tools for.

---

### JSON input alternatives

```json
{
  "intent": "Get recommended tools for analyzing a 10-K filing",
  "params": {
    "form_type": "10-K"
  }
}
```

```json
{
  "intent": "Get recommended tools for analyzing insider filing forms",
  "params": {
    "form_type": "4"
  }
}
```
