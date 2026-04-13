## uspto-patent-mcp_search_office_actions

### What this tool is used for
Searches office actions across applications. The schema notes that this tool is temporarily unavailable because legacy endpoints were decommissioned and ODP migration is pending, and it points users to `odp_get_documents` or `odp_get_transactions` instead.

---

### Used parameters

**(3) query - Optional**
Default: null
Full-text search query for office actions.

**(11) application_number - Optional**
Default: null
Filters results by application number.

**(35) examiner_name - Optional**
Default: null
Filters results by examiner name.

**(36) art_unit - Optional**
Default: null
Filters results by art unit number.

**(37) mail_date_from - Optional**
Default: null
Sets the mail date range start for this office action search.

**(38) mail_date_to - Optional**
Default: null
Sets the mail date range end for this office action search.

**(4) offset - Optional**
Default: 0
Starting position for pagination in this office action search.

**(5) limit - Optional**
Default: 25
Maximum number of office action results to return in this tool.

---

### JSON input alternatives

```json
{
  "intent": "Attempt to search office actions for a specific application",
  "params": {
    "application_number": "16123456",
    "limit": 10
  }
}
```

```json
{
  "intent": "Attempt to search office actions by examiner and mail date range",
  "params": {
    "examiner_name": "Smith",
    "mail_date_from": "2024-01-01",
    "mail_date_to": "2024-12-31",
    "limit": 25
  }
}
```
