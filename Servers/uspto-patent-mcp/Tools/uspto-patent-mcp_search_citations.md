## uspto-patent-mcp_search_citations

### What this tool is used for
Searches citation records. The schema notes that this tool is temporarily unavailable because legacy endpoints were decommissioned and ODP migration is pending, and it points users to `patentsview_search_patents` instead.

---

### Used parameters

**(41) citing_patent: Optional**
Default: null
Filters results by the patent that is citing another patent.

**(42) cited_patent: Optional**
Default: null
Filters results by the patent being cited.

**(43) assignee: Optional**
Default: null
Filters results by assignee name.

**(44) date_from: Optional**
Default: null
Sets the date range start for this citation search.

**(45) date_to: Optional**
Default: null
Sets the date range end for this citation search.

**(4) offset: Optional**
Default: 0
Starting position for pagination in this citation search.

**(5) limit: Optional**
Default: 25
Maximum number of citation records to return in this tool.

---

### JSON input alternatives

```json
{
  "intent": "Attempt to search for records citing a specific patent",
  "params": {
    "cited_patent": "7861317",
    "limit": 10
  }
}
```

```json
{
  "intent": "Attempt to search citation records for an assignee within a date range",
  "params": {
    "assignee": "IBM",
    "date_from": "2023-01-01",
    "date_to": "2023-12-31",
    "limit": 25
  }
}
```
