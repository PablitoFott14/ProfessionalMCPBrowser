## sec-edgar-mcp

The `sec-edgar-mcp` server provides structured access to SEC EDGAR data, covering company identification, filing discovery and retrieval, financial statement extraction, XBRL concept and metric discovery, segment analysis, insider trading records, and form-type guidance. It is useful when the user needs to move from a company name or ticker through to specific filing content, financial data, or insider activity in a single server.

### How it works
- Company lookups start with `get_cik_by_ticker`, `get_company_info`, or `search_companies` to resolve the entity, then filing tools like `get_recent_filings` and `get_filing_content` retrieve the actual documents.
- Financial data tools (`get_financials`, `get_key_metrics`, `get_company_facts`, `get_segment_data`, `compare_periods`) operate against XBRL-structured data from SEC filings and accept a ticker or CIK as the primary identifier.
- XBRL discovery tools (`discover_company_metrics`, `discover_xbrl_concepts`) enumerate what data is available before extraction, which is useful when the metric name is not known in advance.
- Insider trading tools (`get_insider_transactions`, `get_insider_summary`, `get_form4_details`, `analyze_form4_transactions`, `analyze_insider_sentiment`) are all Form 4 focused and share the same company identifier pattern.
- `get_recommended_tools` provides guidance on which tools to use for a given SEC form type, useful when starting research on an unfamiliar form.

### Potential resolution paths
- **Research a company's financial position:** Use `get_company_info` to confirm the entity, then `get_financials` for income, balance sheet, or cash flow data, and `get_key_metrics` or `compare_periods` for specific metric trends.
- **Drill into a specific filing:** Use `get_recent_filings` to find the accession number, then `get_filing_content` for the full document or `get_filing_sections` to extract a specific section such as risk factors or MD&A.
- **Analyze an 8-K event:** Use `get_recent_filings` filtered to 8-K, then `analyze_8k` to extract the event type and items from the filing.
- **Research insider trading activity:** Use `get_insider_transactions` or `get_insider_summary` for a company-level view, then `get_form4_details` or `analyze_form4_transactions` for a specific filing, and `analyze_insider_sentiment` for trend analysis.
- **Discover available metrics before extraction:** Use `discover_company_metrics` or `discover_xbrl_concepts` to enumerate what is reported in EDGAR before calling `get_key_metrics` or `compare_periods`.
- **Get oriented on an unfamiliar form type:** Use `get_recommended_tools` with the form type to receive tool selection guidance before starting.

### Best practices
- **Resolve the company identifier first:** Most tools accept either a ticker or CIK. When starting from a name, use `search_companies` or `get_cik_by_ticker` to confirm the identifier before calling financial or filing tools.
- **Use discovery tools before metric extraction:** `discover_company_metrics` and `discover_xbrl_concepts` reveal what XBRL data a company actually reports, which prevents failed calls to `get_key_metrics` or `compare_periods` when a metric is not available for that company.
- **Use accession number for targeted filing access:** Once `get_recent_filings` returns an accession number, pass it directly to `get_filing_content`, `get_filing_sections`, or `get_form4_details` rather than searching again.
