(1) ticker
Ticker symbol of the company (e.g., "NVDA", "AAPL").
Required. No default value.

(2) identifier
Company ticker symbol or CIK number.
Required or optional depending on the tool. Default value only when stated in the tool schema.

(3) query
Search query for company name.
Required. No default value.

(4) limit
Maximum number of results to return.
Optional. Default varies by tool.

(5) accession_number
Accession number of the filing.
Required or optional depending on the tool. Default value only when stated in the tool schema.

(6) form_type
Specific SEC form type to filter by (e.g., "10-K", "10-Q", "8-K").
Required or optional depending on the tool. Default value only when stated in the tool schema.

(7) days
Number of days to look back.
Optional. Default varies by tool.

(8) statement_type
Type of financial statement to retrieve. Accepted values: income, balance, cash, all.
Optional. Default: all.

(9) segment_type
Type of segment analysis.
Optional. Default: geographic.

(10) metrics
List of specific metrics to retrieve.
Optional. Default: null.

(11) metric
Financial metric to compare (e.g., "Revenues", "NetIncomeLoss").
Required. No default value.

(12) start_year
Starting year for comparison.
Required. No default value.

(13) end_year
Ending year for comparison.
Required. No default value.

(14) search_term
Search term to filter metrics.
Optional. Default: null.

(15) namespace_filter
Filter to show only concepts from a specific namespace.
Optional. Default: null.

(16) form_types
List of form types to include.
Optional. Default: null.

(17) months
Number of months to analyze.
Optional. Default: 6.
