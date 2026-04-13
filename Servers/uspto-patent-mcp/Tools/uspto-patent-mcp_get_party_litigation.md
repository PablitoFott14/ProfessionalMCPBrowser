## uspto-patent-mcp_get_party_litigation

### What this tool is used for
Gets litigation history for a company or individual. Use it when you need to understand a party's patent litigation profile as a plaintiff, defendant, or both.

---

### Used parameters

**(18) party_name - Required**
Default: No default
Company or individual name to look up.

**(46) role - Optional**
Default: null
Filters results by litigation role.

**(5) limit - Optional**
Default: 25
Maximum number of litigation results to return in this tool.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve patent litigation history for a company in any role",
  "params": {
    "party_name": "IBM",
    "limit": 10
  }
}
```

```json
{
  "intent": "Retrieve patent litigation history where a company appears as a defendant",
  "params": {
    "party_name": "Apple",
    "role": "defendant",
    "limit": 25
  }
}
```
