## us-legal-mcp

The `us-legal-mcp` server is a US legal research server for searching across congressional legislation, Federal Register materials, and court opinions, while also surfacing recent items from each source. It is useful when the user needs either targeted research within one legal source or a broader view across legislation, regulation, and case law.

### How it works
- The server is organized around source-specific search tools for Congress, the Federal Register, and CourtListener, plus recent-item tools for each of those sources.
- Most search workflows start from a `query`, while optional filters such as `congress`, `court`, and `limit` help narrow scope or control result volume.
- The cross-source tool is useful for broader discovery, while the source-specific tools are better when the user already knows whether the question is legislative, regulatory, or judicial.

### Potential resolution paths
- **Start broad, then narrow to the right source:** Use `search_all_legal` when the user only has a topic, then continue with `search_congress_bills`, `search_federal_register`, or `search_court_opinions` once the most relevant legal source is clear.
- **Track a legal topic across different source types:** Use `search_congress_bills` for proposed legislation, `search_federal_register` for regulatory material on the same topic, and `search_court_opinions` when the user also needs judicial treatment of that issue.
- **Monitor what is new without starting from a keyword search:** Use `get_recent_bills`, `get_recent_regulations`, or `get_recent_court_opinions` when the goal is to review the latest published or introduced legal materials first, then follow with a source-specific search if a topic needs deeper research.

### Best practices
- **Choose the source-specific tool when the legal source is already known:** It will usually return more focused results than starting with the cross-source search.
- **Use broad search first when the user is exploring a topic rather than a source:** `search_all_legal` works better as a starting point when the request does not clearly map to legislation, regulation, or case law.
