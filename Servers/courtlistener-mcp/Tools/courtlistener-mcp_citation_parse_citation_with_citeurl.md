## courtlistener-mcp_citation_parse_citation_with_citeurl

### What this tool is used for
Parses a legal citation using the citeurl library to extract structured token data, a normalized citation format, and a generated URL. Use it when a citation string needs to be decomposed into its components — volume, reporter, page — or when a canonical URL for the cited source is needed.

---

### Used parameters

**(10) citation: Required**
Default: No default
Legal citation string to parse (e.g., "410 U.S. 113", "42 USC § 1988").

**(13) broad: Optional**
Default: true
Controls whether broad matching is used for more flexible parsing of ambiguous or non-standard citation formats.

---

### JSON input alternatives

```json
{
  "intent": "Parse a case citation to extract its structured components and URL",
  "params": {
    "citation": "410 U.S. 113"
  }
}
```

```json
{
  "intent": "Parse a statutory citation with strict matching only",
  "params": {
    "citation": "42 USC § 1988",
    "broad": false
  }
}
```
