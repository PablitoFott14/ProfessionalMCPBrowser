## open-legal-compliance-mcp

The `open-legal-compliance-mcp` server is a broad legal and regulatory research server spanning US federal and state law, EU and UK legislation, Canadian case law, congressional activity, FDA enforcement, SEC filings, and open government data. It is useful when the user needs to research legal or compliance requirements across multiple jurisdictions or source types from a single server.

### How it works
- The server aggregates multiple legal and regulatory data sources under a unified search interface. Each tool targets a distinct source: US Code, CFR, case law via CourtListener, Federal Register, EU regulations via EUR-Lex, UK legislation, state law for CA/NY/IL, state legislation across all 50 states via OpenStates, Canadian case law via CanLII, FDA adverse event and enforcement data, SEC filings via EDGAR, and the Data.gov catalog.
- Most tools follow a simple query-plus-optional-filter pattern. The main filters vary by source: title for US Code and CFR, court for case law, language for EU regulations, state or jurisdiction for state-level searches, congress number for bills, database for CanLII, and type for FDA searches.
- `get_sec_filings` is the only tool that does not accept a query string — it retrieves filings directly by CIK number.
- `search_state_law` covers only CA, NY, and IL, while `search_open_states` covers all 50 states via OpenStates. Both serve state-level research but with different scope and source.

### Potential resolution paths
- **Research a US federal compliance requirement:** Use `search_us_code` for statutory text, `search_cfr` for regulatory requirements, and `search_federal_register` for proposed or final rules and agency notices.
- **Research a legal topic across case law:** Use `search_case_law` for US federal and circuit court opinions, `search_canlii_cases` for Canadian precedent, or combine both for cross-jurisdictional research.
- **Research EU or UK regulatory requirements:** Use `search_eu_regulations` with a query or CELEX number for EU law, and `search_uk_legislation` for British statutory instruments and Acts of Parliament.
- **Research state-level requirements:** Use `search_state_law` for deep statutory research in CA, NY, or IL, and `search_open_states` when coverage beyond those three states is needed or when tracking active legislative activity.
- **Track pending legislation:** Use `search_congress_bills` for federal bills, optionally filtered by Congress number, and `search_open_states` for state-level bills across all jurisdictions.
- **Research FDA compliance or enforcement history:** Use `search_fda_events` with the appropriate type (drug, device, or food) to find adverse event reports or enforcement actions.
- **Access SEC filings for a company:** Use `get_sec_filings` with the company's CIK number to retrieve its full EDGAR filing history.
- **Find government datasets for a topic:** Use `search_data_gov` to locate relevant public datasets from the Data.gov catalog.

### Best practices
- **Use `search_open_states` instead of `search_state_law` when the target state is outside CA, NY, or IL:** `search_state_law` is limited to those three states by its enum constraint, while `search_open_states` covers all 50 states.
- **Use a CELEX number in `search_eu_regulations` when the specific regulation is known:** Passing a CELEX number directly retrieves the exact regulation rather than running a broad query.
- **Resolve a company CIK before calling `get_sec_filings`:** The tool requires a 10-digit CIK. If the CIK is not already known, use `sec-edgar-mcp`'s `get_cik_by_ticker` or `search_companies` tools to look it up first.
