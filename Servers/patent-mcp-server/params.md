(1) method
The operation to perform. Determines which parameters are relevant for the call.
Required. No default value.

(2) query
Search query string. Usage and syntax vary by tool and method.
Optional. Default: null.

(3) start
Starting position for results. Used by ppubs_search_* methods.
Optional. Default: 0.

(4) limit
Maximum number of results to return. Used by ppubs_search_* and search_* methods.
Optional. Default: 100.

(5) sort
Sort order for results.
Optional. Default: date_publ desc.

(6) default_operator
Default boolean operator to apply between search terms. Used by ppubs_search_* methods.
Optional. Default: OR.

(7) expand_plurals
If true, includes plural forms of search terms. Used by ppubs_search_* methods.
Optional. Default: true.

(8) british_equivalents
If true, includes British spelling equivalents of search terms. Used by ppubs_search_* methods.
Optional. Default: true.

(9) guid
Document unique identifier. Used by ppubs_get_full_document.
Optional. Default: null.

(10) source_type
Document type to retrieve. Used by ppubs_get_full_document.
Optional. Default: null.

(11) patent_number
Patent number to retrieve or download. Used by ppubs_get_patent_by_number and ppubs_download_patent_pdf.
Optional. Default: null.

(12) app_num
U.S. Patent Application Number (e.g., 14412875). Used by get_app_* methods.
Optional. Default: null.

(13) q
Search query string. Used by search_* and download_* methods.
Optional. Default: null.

(14) offset
Starting position for results. Used by search_* and download_* methods.
Optional. Default: 0.

(15) facets
Comma-separated fields to facet upon. Used by search_* and download_* methods.
Optional. Default: null.

(16) fields
Comma-separated fields to include in the response. Used by search_* and download_* methods.
Optional. Default: null.

(17) filters
Filter conditions to apply to the query. Used by search_* and download_* methods.
Optional. Default: null.

(18) range_filters
Range filter conditions to apply to the query. Used by search_* and download_* methods.
Optional. Default: null.

(19) format
Download format. Used by download_* methods.
Optional. Default: json.

(20) filters_list
List of filter objects. Used by *_post methods.
Optional. Default: null.

(21) range_filters_list
List of range filter objects. Used by *_post methods.
Optional. Default: null.

(22) sort_list
List of sort objects. Used by *_post methods.
Optional. Default: null.

(23) fields_list
List of field names to include in the response. Used by *_post methods.
Optional. Default: null.

(24) facets_list
List of facet field names. Used by *_post methods.
Optional. Default: null.

(25) product_title
Specific product title to filter by. Used by search_datasets.
Optional. Default: null.

(26) product_description
Specific product description to filter by. Used by search_datasets.
Optional. Default: null.

(27) product_short_name
Product identifier short name. Used by search_datasets.
Optional. Default: null.

(28) include_files
If true, includes file listings in the dataset response. Used by search_datasets and get_dataset_product.
Optional. Default: true.

(29) latest
If true, returns only the latest dataset product. Used by search_datasets and get_dataset_product.
Optional. Default: false.

(30) labels
Filter datasets by labels. Used by search_datasets.
Optional. Default: null.

(31) categories
Filter datasets by categories. Used by search_datasets.
Optional. Default: null.

(32) datasets
Filter by dataset names. Used by search_datasets.
Optional. Default: null.

(33) file_types
Filter datasets by file types. Used by search_datasets.
Optional. Default: null.

(34) product_id
Product identifier. Used by get_dataset_product.
Optional. Default: null.

(35) file_data_from_date
Filter dataset files from this date (YYYY-MM-DD). Used by get_dataset_product.
Optional. Default: null.

(36) file_data_to_date
Filter dataset files to this date (YYYY-MM-DD). Used by get_dataset_product.
Optional. Default: null.

(37) country
Country code to scope the search.
Optional. Default: US.

(38) start_date
Start date for filtering results by publication date (YYYYMMDD integer format, e.g., 20220101).
Optional. Default: null.

(39) end_date
End date for filtering results by publication date (YYYYMMDD integer format, e.g., 20251231).
Optional. Default: null.

(40) publication_number
Patent publication number (e.g., US-9876543-B2).
Required. No default value.

(41) inventor_name
Inventor name to search for.
Required. No default value.

(42) assignee_name
Assignee or company name to search for.
Required. No default value.

(43) cpc_code
Cooperative Patent Classification (CPC) code to search for (e.g., G06N3/08 for neural networks).
Required. No default value.
