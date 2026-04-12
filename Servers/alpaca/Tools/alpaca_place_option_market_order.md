## alpaca_place_option_market_order

### What this tool is for
Places a market order for one or more option legs, supporting both single-leg and multi-leg strategies (spreads, straddles, strangles, etc.) with atomic execution. Use this when the user wants to enter an options position at market price.

Key constraints:
- Only `day` is a valid time_in_force for options orders.
- Single-leg orders default to `simple` order class; multi-leg orders require `mleg`.
- Multi-leg orders support up to 4 legs executed atomically.
- Account option trading level must match the strategy complexity.

---

### Used parameters

**(61) legs — Required**
Default: No default
List of option legs. Each leg is a dictionary with:
- `symbol` (str): OCC option contract symbol (e.g., AAPL230616C00150000)
- `side` (str): buy or sell
- `ratio_qty` (int): Quantity ratio for the leg (1–4)

**(48) order_class — Optional**
Default: null (simple for single-leg, mleg for multi-leg)
Allowed: simple, mleg
Order class.

**(45) quantity — Optional**
Default: 1
Base quantity multiplied by each leg's ratio_qty.

**(47) time_in_force — Optional**
Default: day
Allowed: day
Time in force. Only day is supported for options orders.

**(19) extended_hours — Optional**
Default: false
Whether to allow execution during extended trading hours.

---

### JSON input alternatives

```json
{
  "tool": "alpaca_place_option_market_order",
  "intent": "Buy 1 Apple call option contract at market price",
  "params": {
    "legs": [
      {"symbol": "AAPL230616C00150000", "side": "buy", "ratio_qty": 1}
    ]
  }
}
```

```json
{
  "tool": "alpaca_place_option_market_order",
  "intent": "Place a bull call spread on Apple — buy lower strike, sell higher strike",
  "params": {
    "legs": [
      {"symbol": "AAPL230616C00150000", "side": "buy", "ratio_qty": 1},
      {"symbol": "AAPL230616C00160000", "side": "sell", "ratio_qty": 1}
    ],
    "order_class": "mleg",
    "quantity": 2
  }
}
```
