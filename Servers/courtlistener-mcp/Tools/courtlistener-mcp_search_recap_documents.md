## courtlistener-mcp_search_recap_documents

### What this tool is used for
Searches federal filing documents from the PACER system via the RECAP archive. Use it when researching filed documents in federal litigation, filtering by court, docket number, party, or date range.

---

### Used parameters

**(1) q: Required**
Default: No default
Full-text search query for RECAP filing documents.

**(2) court: Optional**
Default: ""
Filters results to a specific court by court ID (e.g., "scotus", "ca9").

**(3) case_name: Optional**
Default: ""
Filters results by case name.

**(29) docket_number: Optional**
Default: ""
Filters results to a specific docket number.

**(30) document_number: Optional**
Default: ""
Filters results to a specific document number within a docket.

**(31) attachment_number: Optional**
Default: ""
Filters results to a specific attachment number.

**(5) filed_after: Optional**
Default: ""
Restricts results to documents filed after this date (YYYY-MM-DD).

**(6) filed_before: Optional**
Default: ""
Restricts results to documents filed before this date (YYYY-MM-DD).

**(32) party_name: Optional**
Default: ""
Filters results by party name.

**(9) order_by: Optional**
Default: score desc
Sort order for results. Accepted values: score desc, dateFiled desc, dateFiled asc.

---

### JSON input alternatives

```json
{
  "intent": "Search RECAP documents for a case by party name and court",
  "params": {
    "q": "motion to dismiss",
    "court": "dcd",
    "party_name": "United States",
    "order_by": "dateFiled desc"
  }
}
```

```json
{
  "intent": "Find documents filed in a specific docket within a date range",
  "params": {
    "q": "summary judgment",
    "docket_number": "1:23-cv-01234",
    "filed_after": "2023-01-01",
    "filed_before": "2023-12-31"
  }
}
```
