## octagon-mcp

The octagon-mcp server is a market intelligence and research server designed for broader, synthesis-heavy analysis across multiple financial and market information sources. It is useful when the user needs an aggregated research view, a multi-source market intelligence answer, or focused analysis on prediction market events.

### How it works
- The server centers on agent-style tools driven by a natural language `prompt`, with different tools oriented toward broader market intelligence, deep research, or prediction-market-specific analysis.
- It also includes a historical prediction market data tool keyed by `event_ticker`, with optional pagination, time-window filtering, and analysis-column controls.
- The server is oriented more toward synthesis and interpreted research workflows than toward direct low-level dataset retrieval.

### Potential resolution paths
- **Run broad market intelligence research:** Use `octagon-agent` when the user needs a wide market intelligence view that combines multiple research domains into one answer.
- **Go deeper on a focused investment research question:** Use `octagon-deep-research-agent` when the request is narrower but still requires aggregated, up-to-date research from multiple sources.
- **Analyze a prediction market with both data and research context:** Pull historical event data with `prediction_markets_history`, then use `octagon-prediction-markets-agent` when the user wants a more interpretive report on drivers, model versus market probabilities, or potential mispricings.

### Best practices
- **Choose the agent by research depth and scope:** Use the broader agent for holistic market intelligence, the deep research agent for focused investment research, and the prediction-markets agent when the question is specifically about Kalshi-style event markets.
- **Use historical event data before interpretive prediction-market analysis when specific event context matters:** `prediction_markets_history` helps ground the later research step in a concrete event and time window.
