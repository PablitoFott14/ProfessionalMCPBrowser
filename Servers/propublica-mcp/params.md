(1) query
Search term (organization name, keywords, etc.).
Required. No default value.

(2) state
Two-letter state code filter (e.g., "CA", "NY").
Optional. Default: null.

(3) ntee_code
NTEE category code filter (e.g., "A01", "B20").
Optional. Default: null.

(4) subsection_code
501(c) subsection code filter (e.g., "3", "4", "6").
Optional. Default: null.

(5) page
Page number for pagination.
Optional. Default: 0.

(6) per_page
Number of results per page. Maximum: 25.
Optional. Default: 25.

(7) ein
Employer Identification Number of the nonprofit (9 digits, with or without hyphen).
Required. No default value.

(8) years
Number of recent years to analyze. Maximum: 10.
Optional. Default: 3.

(9) limit
Maximum number of results to retrieve.
Optional. Default and maximum vary by tool.

(10) radius_miles
Geographic radius in miles for location-based filtering.
Optional. Default: null.

(11) same_ntee
Whether to restrict results to the same NTEE category as the reference organization.
Optional. Default: true.

(12) min_revenue
Minimum annual revenue filter.
Optional. Default: null.

(13) max_revenue
Maximum annual revenue filter.
Optional. Default: null.

(14) eins
List of EINs to export. Maximum: 10 organizations.
Required. No default value.

(15) format
Export format.
Optional. Default: json.
Allowed: json, csv.

(16) include_financials
Whether to include financial analysis in the export.
Optional. Default: true.

(17) include_filings
Whether to include recent filings in the export.
Optional. Default: false.

(18) max_filings_per_org
Maximum number of filings to include per organization when include_filings is true.
Optional. Default: 3.
