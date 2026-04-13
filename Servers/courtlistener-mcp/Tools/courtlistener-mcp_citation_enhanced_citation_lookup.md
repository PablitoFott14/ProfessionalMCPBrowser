## courtlistener-mcp_citation_enhanced_citation_lookup

### What this tool is used for
Performs an enhanced citation lookup by combining citeurl parsing with CourtListener API data. Use it when a citation string needs to be validated and enriched with case information from both local parsing and CourtListener records.

---

### Used parameters

**(10) citation: Required**
Default: No default
Legal citation string to look up and analyze (e.g., "410 U.S. 113").

**(11) include_courtlistener: Optional**
Default: true
Controls whether a CourtListener API lookup is performed in addition to local citeurl parsing.

---

### JSON input alternatives

```json
{
  "intent": "Look up and enrich a citation using both citeurl and CourtListener",
  "params": {
    "citation": "410 U.S. 113"
  }
}
```

```json
{
  "intent": "Parse and validate a citation locally without a CourtListener API call",
  "params": {
    "citation": "347 U.S. 483",
    "include_courtlistener": false
  }
}
```
