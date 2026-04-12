## massive-mcp_get_endpoint_docs

### What this tool is for
Retrieves parameter documentation for a financial data API endpoint from its documentation URL. Use this after endpoint discovery, when the user needs the endpoint pattern and available query parameters before making a request.

---

### Used parameters

**(3) url - Required**  
Default: No default  
Documentation URL used to retrieve endpoint details.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve documentation for a discovered aggregates endpoint",
  "params": {
    "url": "https://example.com/docs/aggs"
  }
}
```

```json
{
  "intent": "Retrieve documentation for a discovered options endpoint",
  "params": {
    "url": "https://example.com/docs/options"
  }
}
```
