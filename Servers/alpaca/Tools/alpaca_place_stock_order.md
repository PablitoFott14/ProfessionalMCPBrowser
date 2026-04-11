## alpaca_place_stock_order

### What this tool is for
Places a stock order on Alpaca with full control over order type, timing, and advanced order classes such as bracket and OCO. Use this when the user wants to buy or sell a stock with a specific execution strategy.

---

### Used parameters

**(1) symbol — Required**
Default: No default
Stock ticker symbol to trade (e.g., AAPL, MSFT).

**(44) side — Required**
Default: No default
Order side (buy or sell).

**(45) quantity — Required**
Default: No default
Number of shares to trade.

**(46) type — Optional**
Default: market
Order type: market, limit, stop, stop_limit, or trailing_stop.

**(47) time_in_force — Optional**
Default: day
How long the order remains active: day, gtc, opg, cls, ioc, or fok.

**(48) order_class — Optional**
Default: null
Order class for advanced strategies: simple, bracket, oco, or oto.

**(49) limit_price — Optional**
Default: null
Limit price. Required for limit and stop_limit order types.

**(50) stop_price — Optional**
Default: null
Stop price. Required for stop and stop_limit order types.

**(51) trail_price — Optional**
Default: null
Trail amount in dollars. Used with trailing_stop order type.

**(52) trail_percent — Optional**
Default: null
Trail amount as a percentage. Used with trailing_stop order type.

**(19) extended_hours — Optional**
Default: false
Whether to allow execution during extended trading hours.

**(53) client_order_id — Optional**
Default: null
Custom identifier for the order, useful for tracking on the client side.

---

### JSON input alternatives

```json
{
  "intent": "Place a market buy order for 10 shares of Apple",
  "params": {
    "symbol": "AAPL",
    "side": "buy",
    "quantity": 10
  }
}
```

```json
{
  "intent": "Place a limit sell order for Nvidia with a bracket to protect profits",
  "params": {
    "symbol": "NVDA",
    "side": "sell",
    "quantity": 5,
    "type": "limit",
    "limit_price": 950,
    "order_class": "bracket",
    "stop_price": 880,
    "time_in_force": "gtc"
  }
}
```
