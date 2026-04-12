## us-regulations-mcp

The us-regulations-mcp server is a US regulatory research and compliance analysis server centered on supported federal and state regulations. It is useful for discovering relevant regulation text, inspecting regulation structure, retrieving exact sections, comparing requirements across regulations, checking sector applicability, mapping controls to regulations, and extracting compliance-oriented outputs from identified sections.

### How it works
- The server supports both discovery and follow-up workflows: broad search and listing tools help identify relevant regulations or sections, while retrieval and analysis tools operate on specific regulations, sections, or section sets.
- Common inputs include `query`, `regulation`, `section`, `sections`, `regulations`, `topic`, `sector`, `framework`, and `state`, depending on whether the task is search, lookup, comparison, applicability, control mapping, or compliance extraction.
- The server also includes server metadata through `about`, which can be used to verify coverage, freshness, and provenance before relying on the results.

### Potential resolution paths
- **Discover a rule, then retrieve the exact text:** Start with `search_regulations` to find relevant sections by topic, use `list_regulations` to inspect available regulation IDs or section structure if needed, then move into `get_section` once the exact regulation and section are known.
- **Move from relevant sections into compliance outputs:** After identifying sections with `search_regulations` or `get_section`, use `get_evidence_requirements` to extract audit evidence expectations or `get_compliance_action_items` to turn the same sections into prioritized follow-up actions.
- **Compare or scope obligations before drilling down:** Use `compare_requirements` to see how multiple regulations address the same topic, `check_applicability` to identify which regulations may apply to a sector, or `get_breach_notification_timeline` when the question is specifically about notification deadlines and jurisdictional requirements.
- **Connect control frameworks to regulation text:** Use `map_controls` when the user starts from a NIST framework objective and needs to locate the related regulation sections before reviewing those sections in more detail.

### Best practices
- **Use discovery tools before section-level tools when the exact citation is not known:** `search_regulations` and `list_regulations` are better starting points than guessing a regulation ID or section number.
- **Choose the analysis tool by the type of compliance question:** Use comparison tools for cross-regulation questions, applicability tools for scoping, section retrieval for exact text, and evidence or action tools when the user needs compliance artifacts or next steps.
