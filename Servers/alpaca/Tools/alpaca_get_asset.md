## alpaca_get_asset

### What this tool is for
Retrieves detailed information about a specific asset on Alpaca, including its name, exchange, asset class, status, and trading properties (e.g., whether it is tradable, marginable, or shortable). Use this when the user needs to verify an asset's characteristics before trading or to understand its market constraints.

---

### Used parameters

**(1) symbol — Required**
Default: No default
Ticker symbol of the asset to look up (e.g., AAPL, TSLA).

---

### JSON input alternatives

```json
{
  "tool": "alpaca_get_asset",
  "intent": "Get detailed trading properties and status for Nvidia",
  "params": {
    "symbol": "NVDA"
  }
}
```
