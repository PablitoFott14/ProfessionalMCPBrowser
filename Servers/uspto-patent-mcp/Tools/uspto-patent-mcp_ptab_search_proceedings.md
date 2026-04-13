## uspto-patent-mcp_ptab_search_proceedings

### What this tool is used for
Searches PTAB trial proceedings. Use it when you need to find patent validity challenges at the Patent Trial and Appeal Board.

---

### Used parameters

**(3) query - Optional**
Default: null
Full-text search query for PTAB proceedings.

**(17) trial_type - Optional**
Default: null
Filters results by trial type.
Allowed: IPR, PGR, CBM, DER

**(9) patent_number - Optional**
Default: null
Filters results by patent number being challenged.

**(18) party_name - Optional**
Default: null
Filters results by petitioner or patent owner name.

**(14) filing_date_from - Optional**
Default: null
Sets the filing date range start for this PTAB search.

**(15) filing_date_to - Optional**
Default: null
Sets the filing date range end for this PTAB search.

**(19) status - Optional**
Default: null
Filters results by proceeding status.
Allowed: Pending, Instituted, Terminated, FWD Entered

**(4) offset - Optional**
Default: 0
Starting position for pagination in this PTAB proceeding search.

**(5) limit - Optional**
Default: 25
Maximum number of proceeding results to return in this tool.

---

### JSON input alternatives

```json
{
  "intent": "Search PTAB proceedings involving a specific patent and party",
  "params": {
    "patent_number": "7123456",
    "party_name": "IBM",
    "limit": 10
  }
}
```

```json
{
  "intent": "Find PTAB proceedings filed within a date range and continue to a later page",
  "params": {
    "filing_date_from": "2023-01-01",
    "filing_date_to": "2023-12-31",
    "offset": 25,
    "limit": 25
  }
}
```
