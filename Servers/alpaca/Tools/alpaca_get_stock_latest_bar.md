## alpaca_get_stock_latest_bar

### What this tool is for
Retrieves the latest minute bar for one or more stocks, returning the most recent OHLCV data point available. Use this when the user needs a real-time or near-real-time snapshot of price activity without pulling a full history.

---

### Used parameters

**(32) symbol_or_symbols — Required**
Default: No default
Single ticker symbol or list of symbols (e.g., AAPL or ["AAPL", "MSFT"]).

**(28) feed — Optional**
Default: null
Market data feed to retrieve from (iex, sip, delayed_sip, otc).

**(29) currency — Optional**
Default: null (USD)
Currency for price values (e.g., USD, EUR, GBP).

---

### JSON input alternatives

```json
{
  "intent": "Get the latest price bar for Apple",
  "params": {
    "symbol_or_symbols": "AAPL"
  }
}
```

```json
{
  "intent": "Get the latest bars for a set of stocks using the SIP feed",
  "params": {
    "symbol_or_symbols": ["MSFT", "GOOGL", "AMZN"],
    "feed": "sip"
  }
}
```
