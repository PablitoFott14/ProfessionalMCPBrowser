## uspto-patent-mcp_get_office_action_text

### What this tool is used for
Gets full text of office actions for an application. The schema notes that the legacy Office Action text APIs were decommissioned in early 2026, have not yet been migrated to the ODP, and that this tool is temporarily unavailable. It points users to `odp_get_documents` to list file wrapper documents, including office actions, and download them instead.

---

### Used parameters

**(11) application_number - Required**
Default: No default
Application number to retrieve office action text for.

**(34) mail_date - Optional**
Default: null
Filters office action text by mail date.

---

### JSON input alternatives

```json
{
  "intent": "Attempt to retrieve office action text for a known application",
  "params": {
    "application_number": "16123456"
  }
}
```

```json
{
  "intent": "Attempt to retrieve office action text for a specific mailed office action",
  "params": {
    "application_number": "16123456",
    "mail_date": "2024-06-15"
  }
}
```
