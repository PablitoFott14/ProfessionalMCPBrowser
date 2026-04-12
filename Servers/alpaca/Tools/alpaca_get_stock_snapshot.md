## alpaca_get_stock_snapshot

### What this tool is for
Retrieves a comprehensive market snapshot for one or more stocks in a single call, combining the latest quote, latest trade, current minute bar, current daily bar, and previous daily bar. Use this when the user needs a full picture of a stock's current market state without making multiple separate requests.

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
  "tool": "alpaca_get_stock_snapshot",
  "intent": "Get a full market snapshot for Nvidia including quote, trade, and bars",
  "params": {
    "symbol_or_symbols": "NVDA"
  }
}
```

```json
{
  "tool": "alpaca_get_stock_snapshot",
  "intent": "Retrieve snapshots for a basket of stocks using the SIP feed",
  "params": {
    "symbol_or_symbols": ["AAPL", "MSFT", "GOOGL", "AMZN"],
    "feed": "sip"
  }
}
```
