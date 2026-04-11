## alpaca

The alpaca server provides full brokerage access through the Alpaca API, covering account management, market data, order execution, and portfolio operations across equities, cryptocurrencies, and options.

### How it works
- Parameters are passed as flat key-value pairs — no nested wrapper object is required.
- Most tools return formatted strings ready for direct display or further processing.
- Tools that affect account state (orders, positions) operate on the live account by default.

### Tool categories

**Account & portfolio**
- Account info, open positions, and full portfolio history with configurable resolution and time window.

**Market data — Stocks**
- Historical bars, quotes, and trades with flexible lookback (days/hours/minutes or ISO date ranges).
- Latest bar, quote, trade, and full snapshot for one or multiple symbols.

**Market data — Crypto**
- Historical and latest bars, quotes, trades, orderbook, and snapshots for crypto pairs (e.g., BTC/USD).

**Market data — Options**
- Latest quotes, snapshots (with Greeks and IV), and full option chains with filtering by strike, expiration, and type.

**Order execution**
- Stock orders: market, limit, stop, stop_limit, trailing_stop — with bracket, OCO, and OTO support.
- Crypto orders: market, limit, and stop_limit with GTC/IOC time in force.
- Options orders: single-leg and multi-leg market orders (up to 4 legs, atomic execution).
- Cancel individual orders or all open orders at once.

**Position management**
- Close individual positions fully or partially (by quantity or percentage).
- Close all positions at once, with optional pre-cancellation of open orders.
- Exercise held option contracts.

**Watchlists**
- Create, update, retrieve, and delete watchlists. Add or remove individual symbols.

**Corporate actions & calendar**
- Corporate action announcements filtered by type, symbol, or date.
- Market calendar and real-time market clock.

**Assets**
- Browse all available assets with filtering by status, class, and exchange.
- Retrieve detailed trading properties for a specific asset.

### Best practices
- Use `get_clock` to verify market status before placing orders.
- Use `get_option_contracts` or `get_option_chain` to discover contract symbols before querying option quotes or snapshots.
- For crypto orders, only `gtc` and `ioc` are valid time_in_force values.
- For options orders, only `day` is a valid time_in_force value.
- Prefer `get_stock_snapshot` or `get_crypto_snapshot` over multiple individual calls when a full market picture is needed.
