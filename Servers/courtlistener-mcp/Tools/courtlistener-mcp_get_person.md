## courtlistener-mcp_get_person

### What this tool is used for
Retrieves judge or legal professional information by ID from CourtListener. Use it when biographical or appointment details about a specific judge or person are needed.

---

### Used parameters

**(16) person_id: Required**
Default: No default
CourtListener person ID for the judge or legal professional to retrieve.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve biographical information for a judge by their CourtListener ID",
  "params": {
    "person_id": "1234"
  }
}
```

```json
{
  "intent": "Look up appointment and career details for a federal judge",
  "params": {
    "person_id": "5678"
  }
}
```
