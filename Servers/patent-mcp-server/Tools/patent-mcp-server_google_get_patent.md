## patent-mcp-server_google_get_patent

### What this tool is used for
Google_get_patent retrieves complete patent details from Google Patents by publication number. It returns the full record including title, abstract, publication and filing dates, inventors, assignees, and classification codes. It is used when the user already has a specific patent publication number and needs the full structured data for that patent from Google's dataset.

---

### Used parameters

**(40) publication_number — Required**
Default: No default
Patent publication number (e.g., US-9876543-B2).

---

### JSON input alternatives

```json
{
  "intent": "Get full details for a specific US patent by publication number",
  "params": {
    "publication_number": "US-9876543-B2"
  }
}

{
  "intent": "Retrieve complete patent record for an EP patent",
  "params": {
    "publication_number": "EP-3456789-A1"
  }
}
```
