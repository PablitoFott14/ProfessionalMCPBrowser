## alpaca_get_all_assets

### What this tool is for
The full list of assets available on Alpaca with optional filtering by status, asset class, exchange, or specific attributes. Use this when the user needs to discover tradable instruments or check availability across different markets and asset classes.

---

### Used parameters

**(2) status — Optional**
Default: null
Filters assets by status (e.g., active, inactive).

**(3) asset_class — Optional**
Default: null
Filters assets by class (e.g., us_equity, crypto).

**(4) exchange — Optional**
Default: null
Filters assets by exchange (e.g., NYSE, NASDAQ).

**(5) attributes — Optional**
Default: null
Comma-separated list of asset attributes to filter by.

---

### JSON input alternatives

```json
{
  "tool": "alpaca_get_all_assets",
  "intent": "Get all active US equity assets listed on NASDAQ",
  "params": {
    "status": "active",
    "asset_class": "us_equity",
    "exchange": "NASDAQ"
  }
}
```

```json
{
  "tool": "alpaca_get_all_assets",
  "intent": "List all active crypto assets available on Alpaca",
  "params": {
    "status": "active",
    "asset_class": "crypto"
  }
}
```
