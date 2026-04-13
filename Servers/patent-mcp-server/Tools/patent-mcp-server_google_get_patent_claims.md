## patent-mcp-server_google_get_patent_claims

### What this tool is used for
Retrieves all claims for a specific patent from Google Patents by publication number. It returns each claim with its claim number and full claim text. It is used when the user needs to read, analyze, or compare the legal claim language of a known patent.

---

### Used parameters

**(40) publication_number — Required**
Default: No default
Patent publication number (e.g., US-9876543-B2).

---

### JSON input alternatives

```json
{
  "intent": "Retrieve all claims for a specific US patent",
  "params": {
    "publication_number": "US-9876543-B2"
  }
}

{
  "intent": "Get the full claim text for an EP patent",
  "params": {
    "publication_number": "EP-3456789-A1"
  }
}
```
