## propublica-mcp_search_nonprofits

### What this tool is used for
Searches for nonprofit organizations in the ProPublica Nonprofit Explorer database by name or keyword, with optional filters for state, NTEE category, and 501(c) subsection. Use it when researching nonprofits or locating an organization's EIN for further lookup.

---

### Used parameters

**(1) query: Required**
Default: No default
Search term such as an organization name or keyword.

**(2) state: Optional**
Default: null
Filters results to a specific state by two-letter code (e.g., "CA", "NY").

**(3) ntee_code: Optional**
Default: null
Filters results by NTEE category code (e.g., "A01", "B20").

**(4) subsection_code: Optional**
Default: null
Filters results by 501(c) subsection code (e.g., "3", "4", "6").

**(5) page: Optional**
Default: 0
Page number for paginating through results.

**(6) per_page: Optional**
Default: 25
Number of results to return per page. Maximum: 25.

---

### JSON input alternatives

```json
{
  "intent": "Search for nonprofits by name or keyword",
  "params": {
    "query": "environmental conservation"
  }
}
```

```json
{
  "intent": "Search for 501(c)(3) nonprofits in California with a specific NTEE code",
  "params": {
    "query": "education foundation",
    "state": "CA",
    "subsection_code": "3",
    "ntee_code": "B20"
  }
}
```
