## open-legal-compliance-mcp_search_data_gov

### What this tool is used for
Searches the Data.gov catalog by query string. Use it when looking for government datasets relevant to a research or compliance topic.

---

### Used parameters

**(1) query: Required**
Default: No default
Search query for Data.gov catalog content.

---

### JSON input alternatives

```json
{
  "intent": "Search Data.gov for datasets on a regulatory topic",
  "params": {
    "query": "air quality emissions monitoring"
  }
}
```

```json
{
  "intent": "Find government datasets related to a compliance area",
  "params": {
    "query": "financial institution enforcement actions"
  }
}
```
