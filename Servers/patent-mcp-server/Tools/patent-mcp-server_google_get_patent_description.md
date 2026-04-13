## patent-mcp-server_google_get_patent_description

### What this tool is used for
Retrieves the detailed description section of a patent document from Google Patents by publication number. It is used when the user needs the full technical disclosure narrative of a known patent, separate from its claims or abstract.

---

### Used parameters

**(40) publication_number: Required**
Default: No default
Patent publication number (e.g., US-9876543-B2).

---

### JSON input alternatives

```json
{
  "intent": "Retrieve the detailed description section of a US patent",
  "params": {
    "publication_number": "US-9876543-B2"
  }
}

{
  "intent": "Get the full description text of an EP patent",
  "params": {
    "publication_number": "EP-3456789-A1"
  }
}
```
