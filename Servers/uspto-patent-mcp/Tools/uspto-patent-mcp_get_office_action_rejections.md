## uspto-patent-mcp_get_office_action_rejections

### What this tool is used for
Gets rejection data from office actions. The schema notes that this tool is temporarily unavailable because legacy endpoints were decommissioned and ODP migration is pending, and it points users to `odp_get_documents` to find office actions.

---

### Used parameters

**(11) application_number: Required**
Default: No default
Application number to retrieve office action rejection data for.

**(34) mail_date: Optional**
Default: null
Filters office action rejection data by mail date.

---

### JSON input alternatives

```json
{
  "intent": "Attempt to retrieve rejection data for a known application",
  "params": {
    "application_number": "16123456"
  }
}
```

```json
{
  "intent": "Attempt to retrieve rejection data for a specific mailed office action",
  "params": {
    "application_number": "16123456",
    "mail_date": "2024-06-15"
  }
}
```
