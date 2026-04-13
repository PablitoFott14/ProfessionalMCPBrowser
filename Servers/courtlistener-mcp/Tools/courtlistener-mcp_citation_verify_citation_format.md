## courtlistener-mcp_citation_verify_citation_format

### What this tool is used for
Verifies whether a citation string is in a recognized legal citation format using citeurl's citation templates. Use it to validate a citation before passing it to lookup or parsing tools, or to surface any formatting issues in a citation string.

---

### Used parameters

**(10) citation: Required**
Default: No default
Legal citation string to verify.

---

### JSON input alternatives

```json
{
  "intent": "Verify that a citation string is in a valid recognized format",
  "params": {
    "citation": "410 U.S. 113"
  }
}
```

```json
{
  "intent": "Check whether a citation string has formatting issues before lookup",
  "params": {
    "citation": "42 USC 1983"
  }
}
```
