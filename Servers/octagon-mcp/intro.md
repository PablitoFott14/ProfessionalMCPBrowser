## octagon-mcp

The `octagon-mcp` server is a market intelligence and research server designed for broader, synthesis-heavy analysis across multiple financial and market information sources. It is useful when the user needs an aggregated research view, a multi-source market intelligence answer, or focused analysis on prediction market events.

### How it works
- The server centers on agent-style tools driven by a natural language `prompt`, with different tools oriented toward broader market intelligence, deep research, or prediction-market-specific analysis.
- It also includes a historical prediction market data tool keyed by `event_ticker`, with optional pagination, time-window filtering, and analysis-column controls.
- The server is oriented more toward synthesis and interpreted research workflows than toward direct low-level dataset retrieval.

### Potential resolution paths
- **Run broad market intelligence research:** Use `octagon-agent` when the user needs a wide market intelligence view that combines multiple research domains into one answer.
- **Go deeper on a focused investment research question:** Use `octagon-deep-research-agent` when the request is narrower but still requires aggregated, up-to-date research from multiple sources.
- **Analyze a prediction market with both data and research context:** Pull historical event data with `prediction_markets_history`, then use `octagon-prediction-markets-agent` when the user wants a more interpretive report on drivers, model versus market probabilities, or potential mispricings.

### Best practices
- **Choose the agent by research depth and scope:** Use `octagon-agent` for holistic market intelligence, `octagon-deep-research-agent` for focused investment research, and `octagon-prediction-markets-agent` when the question is specifically about Kalshi-style event markets.
- **Retrieve historical market data for a specific event before running prediction-market analysis:** Call `prediction_markets_history` with the `event_ticker` and relevant time window first, then pass that concrete market context into `octagon-prediction-markets-agent` — the analysis is more grounded when actual pricing and event history are part of the prompt.
