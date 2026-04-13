## massive-mcp

The `massive-mcp` server is a financial market data access server for discovering API endpoints, reviewing endpoint documentation, calling those endpoints, and analyzing stored results with SQL. It is useful when the user needs to move from a natural-language market data request into an executable data workflow without leaving the server.

### How it works
- The server is organized as a stepwise workflow: `search_endpoints` is used to discover relevant endpoints or local functions, `get_endpoint_docs` is used to inspect endpoint parameters, `call_api` is used to fetch market data, and `query_data` is used to analyze stored results.
- Common inputs include `query` and `scope` for discovery, `url` for documentation lookup, `method`, `path`, `params`, `store_as`, and `api_key` for API calls, and `sql` for querying stored tables.
- The server also supports optional post-processing through `apply`, both when data is fetched and when query results are analyzed.

### Potential resolution paths
- **Discover an endpoint, then execute it:** Start with `search_endpoints` to find the right market data endpoint, use `get_endpoint_docs` to inspect the endpoint pattern and query parameters, then call `call_api` with the selected path and needed request parameters.
- **Turn raw API results into queryable tables:** Use `call_api` with `store_as` when the user wants to keep the returned data available for later analysis, then use `query_data` to inspect, filter, aggregate, or compare the stored results with SQL.
- **Move from data retrieval into post-processing:** Use `search_endpoints` with function scope when the user needs available local functions, then apply those functions either during `call_api` or after a SQL result with `query_data`.

### Best practices
- **Follow the workflow in order when the endpoint is not already known:** `search_endpoints` and `get_endpoint_docs` are the right starting points before building a `call_api` request.
- **Store results when the user will need follow-up analysis:** `store_as` makes later SQL analysis through `query_data` much more efficient than repeatedly calling the same endpoint.
