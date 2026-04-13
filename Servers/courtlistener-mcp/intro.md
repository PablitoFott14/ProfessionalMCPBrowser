## courtlistener-mcp

The `courtlistener-mcp` server provides access to the CourtListener legal research database, covering opinion and case law search, citation parsing and validation, PACER docket and document access via the RECAP archive, oral argument audio, judge and court records, and server status. It is useful when the user needs to research precedent, resolve citations, investigate federal litigation, or look up court and judge information from a single server.

### How it works
- The server is split across several functional groups: opinion search and retrieval (`search_opinions`, `get_opinion`, `get_cluster`), citation tools (`citation_lookup_citation`, `citation_batch_lookup_citations`, `citation_enhanced_citation_lookup`, `citation_parse_citation_with_citeurl`, `citation_verify_citation_format`, `citation_extract_citations_from_text`), RECAP archive tools (`search_dockets`, `get_docket`, `search_recap_documents`), audio tools (`search_audio`, `get_audio`), and entity lookup tools (`get_court`, `get_person`, `search_people`).
- Citation tools combine two sources: the citeurl library for local parsing, validation, and URL generation, and the CourtListener API for case record lookup. The enhanced lookup tool uses both together.
- Search tools across opinions, dockets, documents, audio, and people all share a common query-plus-filter pattern, accepting a full-text query alongside optional field-level filters and sort order.
- Get-by-ID tools (`get_opinion`, `get_cluster`, `get_docket`, `get_audio`, `get_person`) require IDs that are typically returned by the corresponding search tools first. `get_court` accepts well-known court identifiers directly (e.g., "scotus", "ca9") without a prior search step.

### Potential resolution paths
- **Research case law on a topic:** Use `search_opinions` with a full-text query and optional court, judge, or date filters, then follow with `get_cluster` or `get_opinion` once a relevant result is identified.
- **Resolve a citation to a case record:** Use `citation_lookup_citation` for a single citation or `citation_batch_lookup_citations` for multiple citations. Use `citation_enhanced_citation_lookup` when both parsed structure and CourtListener record data are needed together.
- **Validate or parse a citation string:** Use `citation_verify_citation_format` to check whether a citation is well-formed, or `citation_parse_citation_with_citeurl` to decompose it into tokens and generate a URL.
- **Extract citations from a document:** Use `citation_extract_citations_from_text` to identify all citations within a block of text before looking them up individually or in batch.
- **Investigate federal litigation:** Use `search_dockets` to find cases by party, court, or docket number, then `get_docket` for the full record and `search_recap_documents` to retrieve specific filed documents.
- **Research a judge:** Use `search_people` to find a judge by name, appointment, or school, then `get_person` for the full biographical and appointment record.
- **Find oral argument recordings:** Use `search_audio` with topic and court filters, then `get_audio` for the specific recording record.

### Best practices
- **Use search tools to obtain IDs before calling get-by-ID tools:** `get_opinion`, `get_cluster`, `get_docket`, `get_audio`, and `get_person` all require a known ID returned by the corresponding search tool. `get_court` is the exception — court IDs such as "scotus" or "ca9" are well-known and can be passed directly.
- **Use `citation_verify_citation_format` before lookup when citation quality is uncertain:** Validating the format locally with citeurl before calling the CourtListener API avoids failed lookups from malformed citation strings.
- **Prefer `citation_batch_lookup_citations` when resolving multiple citations:** It handles up to 100 citations in a single request, which is more efficient than calling `citation_lookup_citation` repeatedly.
