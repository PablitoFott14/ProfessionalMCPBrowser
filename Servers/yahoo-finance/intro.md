## yahoo-finance

The yahoo-finance server is a market research server centered on ticker discovery, company snapshots, recent news, historical price data, option chains, earnings data, and sector-level entity lists. It is useful when the user needs to move between symbol discovery, ticker-specific context, and broader market browsing within the same server.

### How it works
- The server supports both discovery workflows and ticker-specific retrieval, depending on whether the user starts from a free-text search, a sector view, or a known symbol.
- Most tools center on a `symbol`, while broader discovery tools use inputs such as `query`, `entity_type`, `sector`, `period`, `interval`, `option_type`, or `date` when applicable.
- The server combines current company context, recent news, historical pricing, options data, and earnings data, so different views of the same ticker can be retrieved without switching servers.

### Potential resolution paths
- **Find a symbol, then inspect it:** Start with `search` when the user has a company name or broad query, then move into `get-ticker-info` or `get-ticker-news` once the correct symbol is identified.
- **Move from a company snapshot into market history:** Use `get-ticker-info` for a broad ticker overview, then follow with `get-price-history` when the user needs to review how that company has traded over time.
- **Expand from a stock into derivatives or event context:** Pull `ticker-option-chain` when the user needs option chain data for the same symbol, or `ticker-earning` when the focus shifts to annual or quarterly earnings context.
- **Explore a sector before narrowing to a ticker:** Use `get-top-entities` to review leading entities within a sector, then choose a symbol from those results for ticker-level data such as `get-ticker-info`, `get-price-history`, or `get-ticker-news`.

### Best practices
- **Use discovery tools before ticker tools when the symbol is uncertain:** `search` and `get-top-entities` are better starting points than guessing a ticker and calling a symbol-specific endpoint directly.
- **Match the tool to the type of context needed:** Use `get-ticker-info` for a broad company view, `get-ticker-news` for recent developments, `get-price-history` for past market behavior, `ticker-option-chain` for options data, and `ticker-earning` for earnings context.
