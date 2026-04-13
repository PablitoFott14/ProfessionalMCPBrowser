## propublica-mcp

The `propublica-mcp` server provides access to ProPublica's Nonprofit Explorer database, covering nonprofit search and discovery, detailed organization records, Form 990 filing retrieval, financial trend analysis, peer comparison, and bulk data export. It is useful when researching nonprofit organizations, evaluating their financial health, accessing their tax filings, or comparing them against similar entities.

### How it works
- The server is organized around two entry points: search tools (`search_nonprofits`, `search_nonprofits_with_pdfs`, `search_similar_nonprofits`) for discovery, and EIN-based tools (`get_organization`, `get_organization_filings`, `get_most_recent_pdf`, `analyze_nonprofit_financials`) for deep lookup once an organization is identified.
- All EIN-based tools require a 9-digit EIN, which can be provided with or without a hyphen. EINs are typically returned by search tools.
- `search_nonprofits` supports filters for state, NTEE category code, and 501(c) subsection, making it the primary discovery tool when the organization name is not known.
- `search_similar_nonprofits` uses a reference EIN to find peer organizations, with optional filters for geographic radius, revenue range, and NTEE category matching.
- `export_nonprofit_data` accepts a list of up to 10 EINs and produces a consolidated JSON or CSV output, optionally enriched with financial analysis and filing history.

### Potential resolution paths
- **Find and profile a nonprofit:** Use `search_nonprofits` to locate the organization and retrieve its EIN, then `get_organization` for the full record and `analyze_nonprofit_financials` for a trend summary.
- **Access Form 990 filings:** Use `get_organization_filings` for structured filing data, or `get_most_recent_pdf` when the latest PDF version is specifically needed. Use `search_nonprofits_with_pdfs` when PDF availability is a requirement before selecting an organization.
- **Benchmark against peers:** Use `search_similar_nonprofits` with the reference EIN to find comparable organizations, then call `get_organization` or `analyze_nonprofit_financials` on individual results for comparison.
- **Export data for multiple organizations:** Collect EINs through search tools, then pass them to `export_nonprofit_data` to produce a consolidated output suitable for analysis or CRM import.

### Best practices
- **Retrieve the EIN from search before calling lookup tools:** `get_organization`, `get_organization_filings`, `get_most_recent_pdf`, `analyze_nonprofit_financials`, and `search_similar_nonprofits` all require a known EIN. Use `search_nonprofits` first if the EIN is not already available.
- **Use `search_nonprofits_with_pdfs` when PDF access is required:** Not all organizations have PDF filings available. This tool filters the search to only return organizations with PDFs, avoiding a failed `get_most_recent_pdf` call on an organization without them.
- **Keep export batches to 10 or fewer EINs:** `export_nonprofit_data` accepts a maximum of 10 EINs per call. For larger sets, split into multiple export calls.
