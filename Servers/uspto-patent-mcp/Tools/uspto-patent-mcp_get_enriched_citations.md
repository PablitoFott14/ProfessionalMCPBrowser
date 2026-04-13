## uspto-patent-mcp_get_enriched_citations

### What this tool is used for
Gets enriched citation data for a patent. The schema notes that the legacy Enriched Citation API was decommissioned in early 2026, has not yet been migrated to the ODP, and that this tool is temporarily unavailable. It points users to `patentsview_get_patent` for basic citation data instead.

---

### Used parameters

**(9) patent_number: Required**
Default: No default
Patent number to retrieve enriched citation data for.

**(39) include_forward: Optional**
Default: true
Controls whether forward citations are included in this request.

**(40) include_backward: Optional**
Default: true
Controls whether backward citations are included in this request.

---

### JSON input alternatives

```json
{
  "intent": "Attempt to retrieve both forward and backward enriched citations for a patent",
  "params": {
    "patent_number": "7861317"
  }
}
```

```json
{
  "intent": "Attempt to retrieve only backward enriched citations for a patent",
  "params": {
    "patent_number": "7861317",
    "include_forward": false
  }
}
```
