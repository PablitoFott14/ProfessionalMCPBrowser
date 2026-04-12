## massive-mcp_query_data

### What this tool is for
Queries stored financial data tables using SQL and can optionally post-process the query results. Use this after data has been stored through `call_api`, when the user needs analysis, filtering, aggregation, or table inspection.

---

### Used parameters

**(10) sql - Required**  
Default: No default  
SQL query or special command used to analyze stored tables.

**(8) apply - Optional**  
Default: null  
List of post-processing function steps to apply to the query results.

---

### JSON input alternatives

```json
{
  "tool": "massive-mcp_query_data",
  "intent": "List all stored data tables",
  "params": {
    "sql": "SHOW TABLES"
  }
}
```

```json
{
  "tool": "massive-mcp_query_data",
  "intent": "Calculate the average close price from a stored prices table and post-process the result",
  "params": {
    "sql": "SELECT AVG(close) AS avg_close FROM prices",
    "apply": [
      {
        "function": "returns",
        "inputs": {
          "price": "avg_close"
        },
        "output": "avg_return"
      }
    ]
  }
}
```
