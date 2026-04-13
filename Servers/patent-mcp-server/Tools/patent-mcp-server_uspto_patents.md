## patent-mcp-server_uspto_patents

### What this tool is used for
Is a unified tool for all USPTO patent operations. It routes to different underlying endpoints through the `method` parameter, covering full-text patent search, application lookup, document retrieval, PDF download, assignment and continuity data, transaction history, and bulk dataset access. It is used whenever the goal involves finding, reading, or downloading US patent or application data from USPTO databases.

Available methods:
- `ppubs_search_patents` — Search granted patents in USPTO Public Search
- `ppubs_search_applications` — Search published patent applications
- `ppubs_get_full_document` — Get full patent document by GUID
- `ppubs_get_patent_by_number` — Get granted patent full text by number
- `ppubs_download_patent_pdf` — Download granted patent as PDF
- `get_app` — Get patent application data by number
- `search_applications` — Search patent applications with query parameters
- `search_applications_post` — Search patent applications with JSON payload
- `download_applications` — Download patent applications with query parameters
- `download_applications_post` — Download patent applications with JSON payload
- `get_app_metadata` — Get application metadata
- `get_app_adjustment` — Get patent term adjustment data
- `get_app_assignment` — Get assignment data
- `get_app_attorney` — Get attorney/agent information
- `get_app_continuity` — Get continuity data
- `get_app_foreign_priority` — Get foreign priority claims
- `get_app_transactions` — Get transaction history
- `get_app_documents` — Get document details
- `get_app_associated_documents` — Get associated documents
- `get_status_codes` — Search for status codes
- `get_status_codes_post` — Search status codes with JSON payload
- `search_datasets` — Search bulk dataset products
- `get_dataset_product` — Get specific dataset product

---

### Used parameters

**(1) method — Required**
Default: No default
The operation to perform. See available methods above.

**(2) query — Optional**
Default: null
Search query string using USPTO Public Search syntax. Used by `ppubs_search_*` methods.

**(3) start — Optional**
Default: 0
Starting position for results. Used by `ppubs_search_*` methods.

**(4) limit — Optional**
Default: 100
Maximum number of results to return. Used by `ppubs_search_*` and `search_*` methods.

**(5) sort — Optional**
Default: date_publ desc
Sort order for results.

**(6) default_operator — Optional**
Default: OR
Default boolean operator between search terms. Used by `ppubs_search_*` methods.

**(7) expand_plurals — Optional**
Default: true
If true, includes plural forms of search terms. Used by `ppubs_search_*` methods.

**(8) british_equivalents — Optional**
Default: true
If true, includes British spelling equivalents. Used by `ppubs_search_*` methods.

**(9) guid — Optional**
Default: null
Document unique identifier. Used by `ppubs_get_full_document`.

**(10) source_type — Optional**
Default: null
Document type to retrieve. Used by `ppubs_get_full_document`. Accepts USPAT or US-PGPUB.

**(11) patent_number — Optional**
Default: null
Patent number to retrieve or download. Used by `ppubs_get_patent_by_number` and `ppubs_download_patent_pdf`.

**(12) app_num — Optional**
Default: null
U.S. Patent Application Number (e.g., 14412875). Used by `get_app_*` methods.

**(13) q — Optional**
Default: null
Search query string. Used by `search_*` and `download_*` methods.

**(14) offset — Optional**
Default: 0
Starting position for results. Used by `search_*` and `download_*` methods.

**(15) facets — Optional**
Default: null
Comma-separated fields to facet upon. Used by `search_*` and `download_*` methods.

**(16) fields — Optional**
Default: null
Comma-separated fields to include in the response. Used by `search_*` and `download_*` methods.

**(17) filters — Optional**
Default: null
Filter conditions to apply. Used by `search_*` and `download_*` methods.

**(18) range_filters — Optional**
Default: null
Range filter conditions to apply. Used by `search_*` and `download_*` methods.

**(19) format — Optional**
Default: json
Download format. Used by `download_*` methods. Accepts json or csv.

**(20) filters_list — Optional**
Default: null
List of filter objects. Used by `*_post` methods.

**(21) range_filters_list — Optional**
Default: null
List of range filter objects. Used by `*_post` methods.

**(22) sort_list — Optional**
Default: null
List of sort objects. Used by `*_post` methods.

**(23) fields_list — Optional**
Default: null
List of field names to include in the response. Used by `*_post` methods.

**(24) facets_list — Optional**
Default: null
List of facet field names. Used by `*_post` methods.

**(25) product_title — Optional**
Default: null
Specific product title to filter by. Used by `search_datasets`.

**(26) product_description — Optional**
Default: null
Specific product description to filter by. Used by `search_datasets`.

**(27) product_short_name — Optional**
Default: null
Product identifier short name. Used by `search_datasets`.

**(28) include_files — Optional**
Default: true
If true, includes file listings in the dataset response. Used by `search_datasets` and `get_dataset_product`.

**(29) latest — Optional**
Default: false
If true, returns only the latest dataset product. Used by `search_datasets` and `get_dataset_product`.

**(30) labels — Optional**
Default: null
Filter datasets by labels. Used by `search_datasets`.

**(31) categories — Optional**
Default: null
Filter datasets by categories. Used by `search_datasets`.

**(32) datasets — Optional**
Default: null
Filter by dataset names. Used by `search_datasets`.

**(33) file_types — Optional**
Default: null
Filter datasets by file types. Used by `search_datasets`.

**(34) product_id — Optional**
Default: null
Product identifier. Used by `get_dataset_product`.

**(35) file_data_from_date — Optional**
Default: null
Filter dataset files from this date (YYYY-MM-DD). Used by `get_dataset_product`.

**(36) file_data_to_date — Optional**
Default: null
Filter dataset files to this date (YYYY-MM-DD). Used by `get_dataset_product`.

---

### JSON input alternatives

```json
{
  "intent": "Search granted patents related to transformer neural network architectures",
  "params": {
    "method": "ppubs_search_patents",
    "query": "transformer neural network attention mechanism",
    "limit": 25,
    "sort": "date_publ desc",
    "default_operator": "AND"
  }
}

{
  "intent": "Retrieve full application data including continuity and assignment for a known application number",
  "params": {
    "method": "get_app",
    "app_num": "14412875"
  }
}

{
  "intent": "Search published patent applications for CRISPR gene editing filed after 2020",
  "params": {
    "method": "search_applications",
    "q": "CRISPR gene editing",
    "filters": "applicationFilingDate:[2020-01-01 TO *]",
    "limit": 50,
    "offset": 0
  }
}
```
