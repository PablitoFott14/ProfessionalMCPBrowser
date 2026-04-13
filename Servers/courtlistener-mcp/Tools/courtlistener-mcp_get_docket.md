## courtlistener-mcp_get_docket

### What this tool is used for
Retrieves a specific court docket by ID from CourtListener. Use it when a docket ID is already known and the full docket record is needed.

---

### Used parameters

**(19) docket_id: Required**
Default: No default
CourtListener docket ID to retrieve.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve a court docket by its CourtListener ID",
  "params": {
    "docket_id": "4214664"
  }
}
```

```json
{
  "intent": "Fetch a known docket record to review its entries and filings",
  "params": {
    "docket_id": "9876543"
  }
}
```
