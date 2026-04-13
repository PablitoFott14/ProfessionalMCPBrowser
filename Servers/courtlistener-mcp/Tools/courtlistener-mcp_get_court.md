## courtlistener-mcp_get_court

### What this tool is used for
Retrieves court information by court ID from CourtListener. Use it when details about a specific court are needed, such as its full name, jurisdiction, or metadata.

---

### Used parameters

**(15) court_id: Required**
Default: No default
CourtListener court identifier to retrieve (e.g., "scotus", "ca9").

---

### JSON input alternatives

```json
{
  "intent": "Retrieve information about the Supreme Court",
  "params": {
    "court_id": "scotus"
  }
}
```

```json
{
  "intent": "Retrieve information about the Ninth Circuit",
  "params": {
    "court_id": "ca9"
  }
}
```
