(1) query
 Natural language search query used to find relevant API endpoints or local functions.
 Required. No default value.

(2) scope
 Search scope used to limit results to API endpoints, local functions, or both.
 Optional. Default: null.

(3) url
 Documentation URL used to retrieve endpoint parameter details.
 Required. No default value.

(4) method
 HTTP method used for the API call. This tool only supports GET.
 Required. No default value.

(5) path
 API endpoint path used to request financial data.
 Required. No default value.

(6) params
 Query parameters passed as key-value pairs with the API request.
 Optional. Default: null.

(7) store_as
 Table name used to store the returned results for later SQL querying.
 Optional. Default: null.

(8) apply
 List of post-processing function steps to apply to the returned results.
 Optional. Default: null.

(9) api_key
 API key used to override the server's default key for the request.
 Optional. Default: null.

(10) sql
 SQL query or special command used to analyze stored data tables.
 Required. No default value.
