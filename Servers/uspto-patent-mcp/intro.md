## uspto-patent-mcp

The `uspto-patent-mcp` server is a USPTO-focused legal and patent research server centered on patent search, application and prosecution data, PTAB proceedings and appeals, litigation history, CPC lookup, and dataset discovery. It is useful when the user needs to move between granted patents, published applications, prosecution records, PTAB matters, litigation records, and bulk data discovery within one server.

### How it works
- The server is split across several data families: PPUBS tools for patent and application search and document retrieval, ODP tools for application and dataset records, PTAB tools for proceedings and decisions, PatentsView compatibility tools, and litigation or citation tools.
- Some tools are live retrieval tools, while others are documented as temporarily unavailable because legacy USPTO endpoints were decommissioned and have not yet been migrated to the Open Data Portal.
- Search-oriented tools generally use shared filters such as `query`, `patent_number`, `application_number`, `cpc_code`, date ranges, pagination fields, or party-name filters depending on the source being queried.
- Several PatentsView tools remain documented for compatibility, but their schemas explicitly note that the PatentsView API was shut down on March 20, 2026, and they point users to PPUBS or ODP alternatives where available.

### Potential resolution paths
- **Find and open a patent or application:** Start with `ppubs_search_patents` or `ppubs_search_applications`, then follow with `ppubs_get_full_document`, `ppubs_get_patent_by_number`, or `ppubs_download_patent_pdf` once the target document is identified.
- **Investigate prosecution history for an application:** Use ODP application tools such as `odp_get_application`, `odp_get_application_metadata`, `odp_get_transactions`, `odp_get_documents`, `odp_get_continuity`, `odp_get_assignment`, `odp_get_adjustment`, `odp_get_attorney`, or `odp_get_foreign_priority` depending on whether the user needs status, metadata, continuity, ownership, term adjustment, representatives, or file-wrapper records.
- **Research PTAB activity:** Use `ptab_search_proceedings`, `ptab_get_proceeding`, `ptab_get_documents`, `ptab_search_decisions`, `ptab_get_decision`, `ptab_search_appeals`, or `ptab_get_appeal` to move from broad PTAB discovery into a specific proceeding, decision, document set, or appeal.
- **Research litigation exposure:** Use `search_litigation`, `get_patent_litigation`, `get_party_litigation`, or `get_litigation_case` depending on whether the user starts from a patent, a party, or a known case identifier.
- **Use fallback paths for retired APIs:** When a PatentsView or legacy USPTO endpoint is marked unavailable, follow the tool-level guidance to pivot to PPUBS or ODP tools instead of continuing down a retired path.

### Best practices
- **Prefer PPUBS for current patent and application retrieval:** The schemas explicitly position `ppubs_search_patents`, `ppubs_search_applications`, and PPUBS document tools as the active alternatives when older PatentsView search and detail endpoints are retired.
- **Use ODP for prosecution and application-level records:** Application metadata, transactions, file-wrapper document lists, continuity, assignments, attorney records, and adjustment data are all grouped under the ODP tool family, so those tools are the best fit when the user is working from an application number rather than a patent number.
- **Treat legacy office action and citation tools as constrained:** Several schemas explicitly say those endpoints are temporarily unavailable because legacy services were decommissioned and ODP migration is still pending, so route users toward the listed alternatives such as `odp_get_documents`, `odp_get_transactions`, or PPUBS and ODP discovery tools.
