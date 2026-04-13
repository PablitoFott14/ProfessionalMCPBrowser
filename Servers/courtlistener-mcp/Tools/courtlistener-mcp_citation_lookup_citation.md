## courtlistener-mcp_citation_lookup_citation

### What this tool is used for
Looks up a single legal citation in CourtListener to find the opinion it references. Use it when a citation string needs to be resolved to a case record. Supports U.S. Reporter, Federal Reporter, WestLaw, and state reporter citation formats.

---

### Used parameters

**(10) citation: Required**
Default: No default
Legal citation string to look up (e.g., "410 U.S. 113", "123 F.3d 456", "2023 WL 12345").

---

### JSON input alternatives

```json
{
  "intent": "Resolve a U.S. Reporter citation to its CourtListener opinion record",
  "params": {
    "citation": "410 U.S. 113"
  }
}
```

```json
{
  "intent": "Resolve a Federal Reporter citation to its CourtListener opinion record",
  "params": {
    "citation": "123 F.3d 456"
  }
}
```
