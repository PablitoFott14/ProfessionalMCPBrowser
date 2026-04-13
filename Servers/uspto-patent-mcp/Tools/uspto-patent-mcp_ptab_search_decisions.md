## uspto-patent-mcp_ptab_search_decisions

### What this tool is used for
Searches PTAB trial decisions. Use it when you need to find institution decisions, final written decisions, or termination orders.

---

### Used parameters

**(3) query - Optional**
Default: null
Full-text search query for PTAB decision text.

**(22) decision_type - Optional**
Default: null
Filters results by decision type.
Allowed: institution, final, termination

**(20) proceeding_number - Optional**
Default: null
Filters results by proceeding number.

**(9) patent_number - Optional**
Default: null
Filters results by patent number.

**(23) decision_date_from - Optional**
Default: null
Sets the decision date range start for this PTAB decision search.

**(24) decision_date_to - Optional**
Default: null
Sets the decision date range end for this PTAB decision search.

**(4) offset - Optional**
Default: 0
Starting position for pagination in this PTAB decision search.

**(5) limit - Optional**
Default: 25
Maximum number of PTAB decision results to return in this tool.

---

### JSON input alternatives

```json
{
  "intent": "Search final PTAB decisions for a specific patent",
  "params": {
    "decision_type": "final",
    "patent_number": "7123456",
    "limit": 10
  }
}
```

```json
{
  "intent": "Search PTAB decisions within a date range for a known proceeding",
  "params": {
    "proceeding_number": "IPR2023-00001",
    "decision_date_from": "2024-01-01",
    "decision_date_to": "2024-12-31",
    "limit": 25
  }
}
```
