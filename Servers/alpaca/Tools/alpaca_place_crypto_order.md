## alpaca_place_crypto_order

### What this tool is for
Places a cryptocurrency order on Alpaca supporting market, limit, and stop_limit order types. Use this when the user wants to buy or sell a crypto pair with control over execution type and sizing.

Key constraints:
- Market orders require either `qty` or `notional` (not both).
- Limit and stop_limit orders require `qty` and do not support `notional`.
- Only `gtc` and `ioc` are valid time_in_force values for crypto orders.

---

### Used parameters

**(1) symbol — Required**
Default: No default
Crypto symbol to trade (e.g., BTC/USD, ETH/USD).

**(44) side — Required**
Default: No default
Allowed: buy, sell
Order side.

**(58) order_type — Optional**
Default: market
Allowed: market, limit, stop_limit
Order type.

**(47) time_in_force — Optional**
Default: gtc
Allowed: gtc, ioc
How long the order remains active.

**(59) qty — Optional**
Default: null
Quantity of the asset to trade. Required for limit and stop_limit orders.

**(60) notional — Optional**
Default: null
Notional value in USD. Supported for market orders only.

**(49) limit_price — Optional**
Default: null
Limit price. Required for limit and stop_limit order types.

**(50) stop_price — Optional**
Default: null
Stop price. Required for stop_limit orders.

**(53) client_order_id — Optional**
Default: null
Custom identifier for the order.

---

### JSON input alternatives

```json
{
  "tool": "alpaca_place_crypto_order",
  "intent": "Buy $500 worth of Bitcoin at market price",
  "params": {
    "symbol": "BTC/USD",
    "side": "buy",
    "notional": 500
  }
}
```

```json
{
  "tool": "alpaca_place_crypto_order",
  "intent": "Place a limit buy order for 0.5 ETH at a specific price",
  "params": {
    "symbol": "ETH/USD",
    "side": "buy",
    "order_type": "limit",
    "qty": 0.5,
    "limit_price": 3200,
    "time_in_force": "gtc"
  }
}
```
