## alpaca_get_stock_latest_trade

### What this tool is for
The latest individual trade execution for one or more stocks, including price, size, and timestamp. Use this when the user needs the most recent transaction price rather than a quote or aggregated bar.

---

### Used parameters

**(32) symbol_or_symbols — Required**
Default: No default
Single ticker symbol or list of symbols (e.g., AAPL or ["AAPL", "MSFT"]).

**(28) feed — Optional**
Default: null
Allowed: iex, sip, delayed_sip, otc
Market data feed to retrieve from.

**(29) currency — Optional**
Default: null (USD)
Currency for price values (e.g., USD, EUR, GBP).

---

### JSON input alternatives

```json
{
  "tool": "alpaca_get_stock_latest_trade",
  "intent": "Get the most recent trade execution for Apple",
  "params": {
    "symbol_or_symbols": "AAPL"
  }
}
```

```json
{
  "tool": "alpaca_get_stock_latest_trade",
  "intent": "Get the latest trade for several stocks simultaneously using the SIP feed",
  "params": {
    "symbol_or_symbols": ["TSLA", "NVDA", "AMD"],
    "feed": "sip"
  }
}
```
