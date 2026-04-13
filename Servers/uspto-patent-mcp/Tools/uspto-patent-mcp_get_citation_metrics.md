## uspto-patent-mcp_get_citation_metrics

### What this tool is used for
Gets citation metrics for a patent. The schema notes that this tool is temporarily unavailable because legacy endpoints were decommissioned and ODP migration is pending.

---

### Used parameters

**(9) patent_number: Required**
Default: No default
Patent number to retrieve citation metrics for.

---

### JSON input alternatives

```json
{
  "intent": "Attempt to retrieve citation metrics for a known patent",
  "params": {
    "patent_number": "7861317"
  }
}
```

```json
{
  "intent": "Attempt to retrieve citation metrics for another patent",
  "params": {
    "patent_number": "10000000"
  }
}
```
