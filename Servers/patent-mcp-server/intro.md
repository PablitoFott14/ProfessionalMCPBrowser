## patent-mcp-server

The patent-mcp-server provides access to two distinct patent data sources: the USPTO database via a unified method-routing tool, and Google Patents Public Datasets via a set of targeted search and retrieval tools. Together they cover patent discovery by keyword, inventor, assignee, or classification code; full document retrieval including claims and descriptions; application-level data such as continuity, assignments, and transaction history; and bulk dataset access — all scoped to US or international patents depending on the source.

### How it works

- **USPTO data** is accessed through a single tool, `uspto_patents`, which routes to 23 different endpoints via the `method` parameter. Methods span full-text patent and application search using USPTO Public Search syntax, application lookup by number, PDF download, and administrative data (continuity, assignments, attorney, transactions, documents).
- **Google Patents data** is split across seven tools. The four search tools (`google_search_patents`, `google_search_by_inventor`, `google_search_by_assignee`, `google_search_by_cpc`) return discovery results including publication numbers. The three retrieval tools (`google_get_patent`, `google_get_patent_claims`, `google_get_patent_description`) each take a publication number and return a specific section of the full patent document.
- All Google search tools accept `country`, `limit`, `offset`, `start_date`, and `end_date` for scoping and pagination. Allowed country codes are: US, EP, WO, JP, CN, KR, GB, DE, FR, CA, AU.
- USPTO `ppubs_search_*` methods use USPTO Public Search field-code syntax and boolean operators; Google search tools accept natural language or keyword queries.

### Potential resolution paths

- **Discover patents by topic across multiple countries:** Use `google_search_patents` with a natural language or keyword query scoped to the relevant country and date range.
- **Research a company's full patent portfolio:** Use `google_search_by_assignee` to retrieve all patents assigned to a company, optionally filtered by country and date range.
- **Track an inventor's filing history:** Use `google_search_by_inventor` to find all patents listing a specific inventor across one or more countries.
- **Explore a technology area by classification:** Use `google_search_by_cpc` with the relevant CPC code to find patents in a defined technology domain without relying on keyword matching.
- **Read a full patent document once the publication number is known:** Call `google_get_patent` for the complete record, `google_get_patent_claims` for the legal claims, and `google_get_patent_description` for the detailed description — each returns a distinct section.
- **Search and retrieve US patents using USPTO syntax:** Use `uspto_patents` with `ppubs_search_patents` or `ppubs_search_applications` for field-level queries, then `ppubs_get_patent_by_number` or `ppubs_get_full_document` to retrieve the full text.
- **Look up application-level administrative data:** Use `uspto_patents` with `get_app_continuity`, `get_app_assignment`, `get_app_transactions`, or related `get_app_*` methods when the application number is known.
- **Download a patent as PDF:** Use `uspto_patents` with `ppubs_download_patent_pdf` and the patent number.

### Best practices

- **Use Google search tools to get publication numbers before calling the retrieval tools:** `google_get_patent`, `google_get_patent_claims`, and `google_get_patent_description` all require a publication number. If the user doesn't already have one, run a search first to obtain it.
- **Choose the right search tool based on query type:** USPTO `ppubs_search_*` methods require structured field-code syntax (e.g., `TTL/battery AND ISD/20220101->20251231`); Google search tools accept plain keywords or natural language. Using Google syntax against USPTO or vice versa will produce poor results.
- **Retrieve claims and description as separate calls when both are needed:** `google_get_patent_claims` and `google_get_patent_description` are distinct endpoints — neither is a subset of `google_get_patent`. If the full document content is required, all three tools may need to be called.
