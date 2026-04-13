## courtlistener-mcp_search_people

### What this tool is used for
Searches judges and legal professionals in the CourtListener database. Use it when researching a judge's background, appointment history, political affiliation, or education, or when finding a person ID for use with other tools.

---

### Used parameters

**(1) q: Required**
Default: No default
Full-text search query for judges and legal professionals.

**(21) name: Optional**
Default: ""
Filters results by the person's name.

**(22) position_type: Optional**
Default: ""
Filters results by position type (e.g., "jud" for judge).

**(23) political_affiliation: Optional**
Default: ""
Filters results by political affiliation.

**(24) school: Optional**
Default: ""
Filters results by school attended.

**(25) appointed_by: Optional**
Default: ""
Filters results by appointing authority.

**(26) selection_method: Optional**
Default: ""
Filters results by selection method.

**(9) order_by: Optional**
Default: score desc
Sort order for results. Accepted values: score desc, name asc.

---

### JSON input alternatives

```json
{
  "intent": "Search for federal judges appointed by a specific authority",
  "params": {
    "q": "federal judge",
    "appointed_by": "Obama",
    "position_type": "jud"
  }
}
```

```json
{
  "intent": "Find judges who attended a specific law school, sorted by name",
  "params": {
    "q": "judge",
    "school": "Harvard Law School",
    "order_by": "name asc"
  }
}
```
