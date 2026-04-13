## propublica-mcp_search_nonprofits_with_pdfs

### What this tool is used for
Searches for nonprofit organizations that have PDF Form 990 filings available in ProPublica. Use it when PDF access to tax filings is specifically required, rather than structured data alone.

---

### Used parameters

**(1) query: Required**
Default: No default
Search term such as an organization name or keyword.

**(9) limit: Optional**
Default: 10
Maximum number of organizations to return.

---

### JSON input alternatives

```json
{
  "intent": "Search for nonprofits with PDF Form 990 filings available by keyword",
  "params": {
    "query": "community health foundation"
  }
}
```

```json
{
  "intent": "Search for a specific nonprofit and retrieve more results with PDF filings",
  "params": {
    "query": "arts education",
    "limit": 25
  }
}
```
