(1) symbol
 Ticker symbol of the asset (e.g., AAPL, TSLA).
 Required. No default value.

(2) status
 Filters assets by status (e.g., active, inactive).
 Default: null

(3) asset_class
 Filters assets by class (e.g., us_equity, crypto).
 Default: null

(4) exchange
 Filters assets by exchange (e.g., NYSE, NASDAQ).
 Default: null

(5) attributes
 Comma-separated list of asset attributes to filter by.
 Default: null

(6) ca_types
 List of corporate action types to filter by (e.g., reverse_split, cash_dividend, spin_off). Accepts multiple values.
 Default: null (all types)

(7) start
 Start date for the data range (e.g., 2024-01-01).
 Default: null (current day)

(8) end
 End date for the data range (e.g., 2024-12-31).
 Default: null (current day)

(9) symbols
 List of ticker symbols to filter results by.
 Default: null

(10) cusips
 List of CUSIP identifiers to filter results by.
 Default: null

(11) ids
 List of corporate action IDs to retrieve. Mutually exclusive with other filters.
 Default: null

(12) limit
 Maximum number of results to return.
 Default: 1000

(13) sort
 Sort order of the results (asc or desc).
 Default: asc

(14) timeframe
 Resolution of each data point (e.g., 1Min, 5Min, 15Min, 1H, 1D).
 Default: null

(15) period
 Length of the time window to retrieve (e.g., 1W, 1M, 3M, 6M, 1Y, all).
 Default: null

(16) date_end
 Alternative end date for the range, as ISO date or datetime.
 Default: null

(17) intraday_reporting
 Controls which hours are included in intraday data (market_hours, extended_hours, continuous).
 Default: null

(18) pnl_reset
 Defines when P/L resets within the period (e.g., daily, weekly, no_reset).
 Default: null

(19) extended_hours
 Whether to include extended trading hours data where applicable.
 Default: null

(20) cashflow_types
 List of cashflow categories to include in portfolio history.
 Default: null

(21) name
 Name of the watchlist.
 Required. No default value.

(22) watchlist_id
 UUID of the watchlist to reference or update.
 Required. No default value.

(23) start_date
 Start date of the range in YYYY-MM-DD format.
 Required. No default value.

(24) end_date
 End date of the range in YYYY-MM-DD format.
 Required. No default value.

(25) days
 Number of days to look back from now (ignored if start is provided).
 Default: 5

(26) hours
 Number of hours to look back from now (ignored if start is provided).
 Default: 0

(27) minutes
 Number of minutes to look back from now (ignored if start is provided).
 Default: 30

(28) feed
 Market data feed to retrieve from (e.g., iex, sip, delayed_sip, otc).
 Default: null

(29) currency
 Currency for price values (e.g., USD, EUR, GBP).
 Default: null (USD)

(30) asof
 As-of date for symbol resolution in YYYY-MM-DD format.
 Default: null

(31) tz
 Timezone for interpreting naive datetime strings (e.g., America/New_York, UTC).
 Default: America/New_York

(32) symbol_or_symbols
 Single ticker symbol or list of ticker symbols (e.g., AAPL or ["AAPL", "MSFT"]).
 Required. No default value.

(33) underlying_symbols
 Underlying asset symbol or list of symbols for options lookup (e.g., SPY, AAPL).
 Required. No default value.

(34) expiration_date
 Specific expiration date to filter option contracts (YYYY-MM-DD).
 Default: null

(35) expiration_date_gte
 Minimum expiration date filter for option contracts (YYYY-MM-DD).
 Default: null

(36) expiration_date_lte
 Maximum expiration date filter for option contracts (YYYY-MM-DD).
 Default: null

(37) expiration_expression
 Natural language expression for expiration date (e.g., "week of September 2, 2025").
 Default: null

(38) strike_price_gte
 Minimum strike price filter for option contracts.
 Default: null

(39) strike_price_lte
 Maximum strike price filter for option contracts.
 Default: null

(40) contract_type
 Filters option contracts by type (call or put).
 Default: null

(41) root_symbol
 Filters option contracts by root symbol.
 Default: null

(42) feed (options)
 Options data feed source (opra or indicative). OPRA requires a subscription; indicative is used as fallback.
 Default: null (opra if subscribed, indicative otherwise)

(43) underlying_symbol
 Single underlying asset symbol for options chain lookup (e.g., AAPL, SPY).
 Required. No default value.

(44) side
 Order side (buy or sell).
 Required. No default value.

(45) quantity
 Number of shares or units to trade.
 Required. No default value.

(46) type
 Order type (market, limit, stop, stop_limit, trailing_stop).
 Default: market

(47) time_in_force
 Time in force for the order (day, gtc, opg, cls, ioc, fok).
 Default: day

(48) order_class
 Order class (simple, bracket, oco, oto, mleg).
 Default: null

(49) limit_price
 Limit price for limit and stop_limit orders.
 Default: null

(50) stop_price
 Stop price for stop and stop_limit orders.
 Default: null

(51) trail_price
 Trail amount in dollars for trailing stop orders.
 Default: null

(52) trail_percent
 Trail amount as a percentage for trailing stop orders.
 Default: null

(53) client_order_id
 Custom client-defined identifier for the order.
 Default: null

(54) after
 Returns results after this timestamp (ISO format).
 Default: null

(55) until
 Returns results up until this timestamp (ISO format).
 Default: null

(56) direction
 Sort direction of results (asc or desc).
 Default: null

(57) nested
 Whether to roll up multi-leg orders under a legs field.
 Default: null

(58) order_type
 Order type for crypto orders (market, limit, stop_limit).
 Default: market

(59) qty
 Quantity of the asset to trade. For crypto market orders, either qty or notional must be provided.
 Default: null

(60) notional
 Notional value in USD to trade. Supported for crypto market orders only.
 Default: null

(61) legs
 List of option legs for single or multi-leg orders. Each leg contains symbol, side, and ratio_qty.
 Required. No default value.

(62) order_id
 UUID of the order to reference or cancel.
 Required. No default value.

(63) percentage
 Percentage of the position to liquidate (e.g., "50" for 50%). Must result in at least 1 share.
 Default: null

(64) cancel_orders
 If true, cancels all open orders before liquidating positions.
 Default: false

(65) symbol_or_contract_id
 Option contract symbol (OCC format) or contract UUID to exercise.
 Required. No default value.