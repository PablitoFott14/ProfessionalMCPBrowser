## goldrush-mcp_bitcoin_non_hd_wallet_balances

### What this tool is used for
Fetches the Bitcoin balance for a single non-HD address, including spot prices and token metadata. It is used when the user needs a lightweight balance check for a standard Bitcoin address rather than an HD wallet derived from an extended public key.

---

### Used parameters

**(9) walletAddress — Required**
Default: No default
The Bitcoin non-HD address to retrieve the balance for.

**(8) quoteCurrency — Optional**
Default: null
Allowed: USD, CAD, EUR, SGD, INR, JPY, VND, CNY, KRW, RUB, TRY, NGN, ARS, AUD, CHF, GBP
Currency used for spot price conversions in the response.

---

### JSON input alternatives

```json
{
  "intent": "Get the current Bitcoin balance for a non-HD address in USD",
  "params": {
    "walletAddress": "bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh",
    "quoteCurrency": "USD"
  }
}
```
