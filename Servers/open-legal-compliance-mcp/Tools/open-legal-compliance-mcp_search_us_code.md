## open-legal-compliance-mcp_search_us_code

### What this tool is used for
Searches the US Code (Federal Law) by query string with an optional title filter. Use it when researching federal statutory law or locating provisions within a specific US Code title.

---

### Used parameters

**(1) query: Required**
Default: No default
Search query for US Code content.

**(2) title: Optional**
Default: No default
Restricts the search to a specific US Code title (e.g., "Title 15").

---

### JSON input alternatives

```json
{
  "intent": "Search federal law for provisions related to a topic",
  "params": {
    "query": "data privacy consumer protection"
  }
}
```

```json
{
  "intent": "Search within a specific US Code title for relevant provisions",
  "params": {
    "query": "antitrust monopoly",
    "title": "Title 15"
  }
}
```
