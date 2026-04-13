## courtlistener-mcp_citation_batch_lookup_citations

### What this tool is used for
Looks up multiple legal citations in a single request against the CourtListener API. Use it when a list of citations needs to be resolved at once rather than making individual calls per citation. Accepts up to 100 citations per request.

---

### Used parameters

**(14) citations: Required**
Default: No default
List of legal citation strings to look up. Minimum 1, maximum 100.

---

### JSON input alternatives

```json
{
  "intent": "Look up multiple case citations in a single batch request",
  "params": {
    "citations": ["410 U.S. 113", "347 U.S. 483", "384 U.S. 436"]
  }
}
```

```json
{
  "intent": "Resolve a set of citations extracted from a document",
  "params": {
    "citations": ["530 U.S. 428", "542 U.S. 507", "556 U.S. 662"]
  }
}
```
