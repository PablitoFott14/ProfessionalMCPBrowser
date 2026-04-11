## alpaca

The alpaca server provides full brokerage access through the Alpaca API, covering account management, market data, order execution, and portfolio operations across equities, cryptocurrencies, and options. Parameters are passed as flat key-value pairs — no nested wrapper object is required.

### How it works
- Most tools return formatted strings ready for direct display or further processing.
- Tools that affect account state — orders, positions, watchlists — operate on the live account by default.
- Asset class constraints apply: crypto orders only accept `gtc` or `ioc` for `time_in_force`; options orders only accept `day`.

### Potential resolution paths
- **Place an order safely:** Call `get_clock` to confirm market status, then `get_asset` to verify the symbol is tradable, before submitting any order.
- **Build an options position:** Use `get_option_contracts` or `get_option_chain` to discover contract symbols and review Greeks, then place the order with `submit_options_order`.
- **Monitor and manage a position:** Fetch `get_open_positions` for current exposure, `get_portfolio_history` for performance context, then close or adjust with `close_position` as needed.
- **Track a new symbol:** Create a watchlist with `create_watchlist`, add symbols via `add_symbol_to_watchlist`, and pull snapshots with `get_stock_snapshot` or `get_crypto_snapshot` for a live market picture.

### Best practices
- Use `get_clock` to verify market status before placing orders.
- Use `get_option_contracts` or `get_option_chain` to discover contract symbols before querying option quotes or snapshots.
- Prefer `get_stock_snapshot` or `get_crypto_snapshot` over multiple individual calls when a full market picture is needed.
