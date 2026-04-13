## sec-edgar-mcp_get_cik_by_ticker

### What this tool is used for
Gets the CIK (Central Index Key) for a company based on its ticker symbol.

---

### Used parameters

**(1) ticker: Required**
Default: No default
Ticker symbol of the company to look up.

---

### JSON input alternatives

```json
{
  "intent": "Find the SEC CIK for NVIDIA",
  "params": {
    "ticker": "NVDA"
  }
}
```

```json
{
  "intent": "Look up the SEC CIK for Apple",
  "params": {
    "ticker": "AAPL"
  }
}
```
