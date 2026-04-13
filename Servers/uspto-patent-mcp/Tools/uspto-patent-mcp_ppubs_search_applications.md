## uspto-patent-mcp_ppubs_search_applications

### What this tool is used for
Searches published US patent applications in USPTO Patent Public Search using USPTO query syntax. Use it when research needs to include published applications rather than only granted patents.

---

### Used parameters

**(3) query: Required**
Default: No default
Search query using USPTO syntax. Supports field codes (e.g., TTL/ for title, IN/ for inventor, AN/ for assignee, CPC/ for classification), phrase search with quotes, and boolean operators (AND, OR).

**(4) offset: Optional**
Default: 0
Starting position for pagination through published-application results.

**(5) limit: Optional**
Default: 100
Maximum number of published-application results to return. Maximum allowed value is 500.

**(6) sort: Optional**
Default: date_publ desc
Sort order for published-application results.

---

### JSON input alternatives

```json
{
  "intent": "Search published applications mentioning transformer architecture in the title",
  "params": {
    "query": "TTL/\"transformer architecture\"",
    "limit": 50
  }
}
```

```json
{
  "intent": "Find published applications assigned to Google in the G06N CPC class",
  "params": {
    "query": "AN/\"Google LLC\" AND CPC/G06N",
    "offset": 50,
    "limit": 25
  }
}
```
