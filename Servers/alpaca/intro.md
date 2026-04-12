## alpaca

The alpaca server is the operational side of the stack: it combines live brokerage actions with market data, account visibility, portfolio monitoring, watchlist management, and multi-asset trading across equities, crypto, and options. It is the server you use when the goal is not only to inspect the market, but to act on it and manage the resulting positions.

### How it works
- The server spans the full trade lifecycle: check market status, inspect assets and quotes, place orders, review positions, and manage portfolio state afterward.
- It also supports broader account workflows such as watchlists, portfolio history, and corporate actions, so monitoring and execution stay in the same environment.
- Requests use flat key-value inputs, and tools that change account state should be treated as live operational actions rather than passive lookups.

### Potential resolution paths
- **Go from market check to execution:** Use `get_clock` and the relevant quote, trade, bar, or snapshot tools to understand current conditions, validate the asset with `get_asset`, then place the order through the appropriate stock, crypto, or options endpoint.
- **Manage existing exposure with context:** Pull `get_all_positions`, `get_open_position`, and `get_portfolio_history` to understand what is already on the book, then close, reduce, or exercise positions with the relevant account-action tools.
- **Create a monitoring workflow before trading:** Build or update watchlists, review snapshots for tracked assets, and use the same server later to transition from observation into order placement when conditions are met.

### Best practices
- **Separate read actions from account actions mentally.**
  Many tools are safe informational lookups, while others directly affect capital, positions, or watchlists.
- **Use the broader market picture before sending orders.**
  Snapshots, latest quotes, option chain data, and account state checks reduce avoidable execution mistakes.
