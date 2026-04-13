## courtlistener-mcp_get_opinion

### What this tool is used for
Retrieves a specific court opinion by ID from CourtListener. Use it when an opinion ID is already known and the full opinion text or metadata is needed.

---

### Used parameters

**(20) opinion_id: Required**
Default: No default
CourtListener opinion ID to retrieve.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve the full text of a court opinion by its CourtListener ID",
  "params": {
    "opinion_id": "108713"
  }
}
```

```json
{
  "intent": "Fetch a specific opinion document from a known cluster",
  "params": {
    "opinion_id": "2345678"
  }
}
```
