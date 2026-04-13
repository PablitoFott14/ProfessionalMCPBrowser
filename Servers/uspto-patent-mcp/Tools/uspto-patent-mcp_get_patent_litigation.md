## uspto-patent-mcp_get_patent_litigation

### What this tool is used for
Gets all litigation involving a specific patent. Use it when you need to see the complete litigation history of a patent, including all cases where it was asserted.

---

### Used parameters

**(9) patent_number: Required**
Default: No default
Patent number to look up.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve the litigation history for a known patent",
  "params": {
    "patent_number": "7861317"
  }
}
```

```json
{
  "intent": "Look up litigation history for another patent",
  "params": {
    "patent_number": "10000000"
  }
}
```
