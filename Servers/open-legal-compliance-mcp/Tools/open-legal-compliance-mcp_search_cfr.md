## open-legal-compliance-mcp_search_cfr

### What this tool is used for
Searches the Code of Federal Regulations (CFR) by query string with an optional title filter. Use it when researching federal regulatory requirements or locating provisions within a specific CFR title.

---

### Used parameters

**(1) query: Required**
Default: No default
Search query for CFR content.

**(2) title: Optional**
Default: No default
Restricts the search to a specific CFR title.

---

### JSON input alternatives

```json
{
  "intent": "Search federal regulations for provisions related to a topic",
  "params": {
    "query": "environmental impact assessment"
  }
}
```

```json
{
  "intent": "Search within a specific CFR title for relevant regulatory provisions",
  "params": {
    "query": "hazardous waste disposal",
    "title": "Title 40"
  }
}
```
