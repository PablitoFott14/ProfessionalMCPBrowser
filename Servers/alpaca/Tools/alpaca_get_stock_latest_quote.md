## alpaca_get_stock_latest_quote

### What this tool is for
Retrieves the latest level 1 bid/ask quote for one or more stocks, including bid price, ask price, sizes, and timestamp. Use this when the user needs the current spread or most recent quote snapshot without historical context.

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
  "tool": "alpaca_get_stock_latest_quote",
  "intent": "Get the latest bid/ask quote for Tesla",
  "params": {
    "symbol_or_symbols": "TSLA"
  }
}
```

```json
{
  "tool": "alpaca_get_stock_latest_quote",
  "intent": "Get the latest quotes for multiple stocks using the SIP feed",
  "params": {
    "symbol_or_symbols": ["AAPL", "NVDA", "META"],
    "feed": "sip"
  }
}
```
