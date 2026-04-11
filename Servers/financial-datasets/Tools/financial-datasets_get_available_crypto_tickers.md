## financial-datasets_get_available_crypto_tickers

### What this tool is for
Returns the full list of cryptocurrency tickers available in the financial-datasets server. Use this as a discovery tool before querying crypto price data, to confirm a ticker is supported.

---

### Used parameters

This tool takes no parameters.

---

### JSON input alternatives

```json
{
  "intent": "Discover all supported cryptocurrency tickers before querying prices",
  "params": {}
}
```

### Potential resolution paths

**"I want to check price history for a crypto asset but I'm not sure of the ticker format."**
Call `get_available_crypto_tickers` first to confirm the exact symbol, then pass it to `get_crypto_prices` or `get_historical_crypto_prices` with the desired date range.

**"Show me what crypto assets are available and then pull price data for a few of them."**
Use `get_available_crypto_tickers` to present the full list, then call `get_historical_crypto_prices` once per selected ticker to retrieve OHLC data for comparison.
