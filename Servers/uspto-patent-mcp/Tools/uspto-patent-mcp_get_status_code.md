## uspto-patent-mcp_get_status_code

### What this tool is used for
Looks up the meaning of a USPTO application status code. Use it when a status code appears in application data and needs to be interpreted.

---

### Used parameters

**(2) code: Required**
Default: No default
Status code number to look up.

---

### JSON input alternatives

```json
{
  "intent": "Find out what USPTO status code 30 means",
  "params": {
    "code": "30"
  }
}
```

```json
{
  "intent": "Look up another USPTO application status code",
  "params": {
    "code": "161"
  }
}
```
