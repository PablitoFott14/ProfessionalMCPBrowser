## uspto-patent-mcp_get_office_action_citations

### What this tool is used for
Gets prior art citations from office actions. The schema notes that this tool is temporarily unavailable because legacy endpoints were decommissioned and ODP migration is pending, and it points users to `get_enriched_citations` as an alternative.

---

### Used parameters

**(11) application_number: Required**
Default: No default
Application number to retrieve office action citations for.

**(34) mail_date: Optional**
Default: null
Filters office action citations by mail date.

---

### JSON input alternatives

```json
{
  "intent": "Attempt to retrieve prior art citations for a known application",
  "params": {
    "application_number": "16123456"
  }
}
```

```json
{
  "intent": "Attempt to retrieve prior art citations for a specific mailed office action",
  "params": {
    "application_number": "16123456",
    "mail_date": "2024-06-15"
  }
}
```
