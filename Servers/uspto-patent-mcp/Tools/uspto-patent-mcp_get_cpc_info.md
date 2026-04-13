## uspto-patent-mcp_get_cpc_info

### What this tool is used for
Looks up the details of a CPC (Cooperative Patent Classification) code, returning the section, title, and description of the technology area it represents. For top-level section codes (A–H, Y) it also returns a list of subsections. Use when identifying what technology area a CPC code covers or when finding related classification codes to broaden or narrow a patent search.

---

### Used parameters

**(1) cpc_code — Required**
Default: No default
CPC code to look up.

---

### JSON input alternatives

```json
{
  "intent": "Find out what technology area the CPC code G06N covers",
  "params": {
    "cpc_code": "G06N"
  }
}
```

```json
{
  "intent": "Look up a more specific neural network classification",
  "params": {
    "cpc_code": "G06N3/08"
  }
}
```
