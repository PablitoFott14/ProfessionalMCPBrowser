## coingecko-mcp_search_docs

### What this tool is used for
Searches the CoinGecko SDK documentation to discover methods, parameters, and usage examples for a given topic. It is used before writing code when the right SDK method or its exact parameter structure is not already known.

---

### Used parameters

**(3) query — Required**
Default: No default
The query to search for in the SDK documentation.

**(4) language — Required**
Default: No default
Allowed: http, python, go, typescript, javascript, terraform, ruby, java, kotlin
The SDK language to search documentation for.

**(5) detail — Optional**
Default: null
Allowed: default, verbose
The amount of detail to return in the documentation results.

---

### JSON input alternatives

```json
{
  "intent": "Find the SDK method for retrieving historical market chart data for a coin",
  "params": {
    "query": "coin market chart history",
    "language": "typescript"
  }
}

{
  "intent": "Explore trending coins endpoint with full parameter detail",
  "params": {
    "query": "trending coins",
    "language": "typescript",
    "detail": "verbose"
  }
}
```
