## uspto-patent-mcp_ppubs_get_patent_by_number

### What this tool is used for
Retrieves a granted patent from USPTO Patent Public Search by patent number. Use it when the patent number is already known and you want the full document without searching first.

---

### Used parameters

**(9) patent_number — Required**
Default: No default
Granted patent number to retrieve.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve a granted patent by patent number",
  "params": {
    "patent_number": "7123456"
  }
}
```

```json
{
  "intent": "Retrieve another granted patent by patent number",
  "params": {
    "patent_number": "10000000"
  }
}
```
