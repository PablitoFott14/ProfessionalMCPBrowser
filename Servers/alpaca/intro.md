## alpaca

The `alpaca` server is the operational side of the stack: it combines live brokerage actions with market data, account visibility, portfolio monitoring, watchlist management, and multi-asset trading across equities, crypto, and options. It is the server you use when the goal is not only to inspect the market, but to act on it and manage the resulting positions.

### How it works
- The server spans the full trade lifecycle: check market status, inspect assets and quotes, place orders, review positions, and manage portfolio state afterward.
- It also supports broader account workflows such as watchlists, portfolio history, and corporate actions, so monitoring and execution stay in the same environment.
- Requests use flat key-value inputs, and tools that change account state should be treated as live operational actions rather than passive lookups.

### Potential resolution paths
- **Go from market check to execution:** Use `get_clock` plus market-data tools such as `get_stock_latest_quote`, `get_crypto_latest_quote`, `get_stock_snapshot`, `get_crypto_snapshot`, or `get_option_snapshot` to understand current conditions, validate the asset with `get_asset`, then place the order through `place_stock_order`, `place_crypto_order`, or `place_option_market_order`.
- **Manage existing exposure with context:** Pull `get_all_positions`, `get_open_position`, and `get_portfolio_history` to understand what is already on the book, then use `close_position`, `close_all_positions`, `cancel_order_by_id`, `cancel_all_orders`, or `exercise_options_position` for the follow-up account action.
- **Create a monitoring workflow before trading:** Use `create_watchlist`, `update_watchlist_by_id`, `add_asset_to_watchlist_by_id`, `remove_asset_from_watchlist_by_id`, `get_watchlists`, or `get_watchlist_by_id`, then review tracked names with `get_stock_snapshot`, `get_crypto_snapshot`, or `get_option_snapshot` before transitioning into order placement.

### Best practices
- **Separate read actions from account actions mentally:** Tools such as `get_account_info`, `get_asset`, `get_clock`, `get_stock_snapshot`, `get_crypto_snapshot`, and `get_option_snapshot` are informational, while `place_stock_order`, `place_crypto_order`, `place_option_market_order`, `close_position`, `close_all_positions`, and watchlist mutation tools directly affect account state.
- **Use the broader market picture before sending orders:** `get_stock_snapshot`, `get_crypto_snapshot`, `get_option_snapshot`, `get_stock_latest_quote`, `get_crypto_latest_quote`, `get_option_chain`, `get_account_info`, and `get_all_positions` reduce avoidable execution mistakes.
