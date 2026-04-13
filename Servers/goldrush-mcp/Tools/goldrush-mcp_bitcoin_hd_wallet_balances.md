## goldrush-mcp_bitcoin_hd_wallet_balances

### What this tool is used for
Fetches balances for each active child address derived from a Bitcoin HD wallet. It is used when the user has an extended public key and needs a consolidated view of balances across all derived addresses without querying each one individually.

---

### Used parameters

**(9) walletAddress — Required**
Default: No default
The extended public key of the Bitcoin HD wallet. Accepts xPub, yPub, or zPub formats.

**(8) quoteCurrency — Optional**
Default: null
Allowed: USD, CAD, EUR, SGD, INR, JPY, VND, CNY, KRW, RUB, TRY, NGN, ARS, AUD, CHF, GBP
Currency used for balance value conversions in the response.

---

### JSON input alternatives

```json
{
  "intent": "Get BTC balances for all active addresses derived from an HD wallet in USD",
  "params": {
    "walletAddress": "xpub6CUGRUonZSQ4TWtTMmzXdrXDtypWKiKrhko4egpiMZbpiaQL2jkwSB1icqYh2cfDfVxdx4df189oLKnC5fSwqPfgyP3hooxujYzAu3fDVmz",
    "quoteCurrency": "USD"
  }
}
```
