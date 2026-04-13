## goldrush-mcp_multichain_address_activity

### What this tool is used for
Identifies which chains a given address has been active on, using a single API call. It is used when the starting point is an address and the goal is to discover which networks to query further, before pulling balances or transactions.

---

### Used parameters

**(9) walletAddress — Required**
Default: No default
The wallet address to check for activity. ENS, RNS, Lens Handle, and Unstoppable Domain names resolve automatically.

**(11) testnets — Optional**
Default: false
Set to true to include testnet chains with activity in the response. By default only mainnet activity is returned.

---

### JSON input alternatives

```json
{
  "intent": "Find which mainnet chains a wallet has been active on",
  "params": {
    "walletAddress": "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"
  }
}

{
  "intent": "Check active chains for an ENS name including testnets",
  "params": {
    "walletAddress": "vitalik.eth",
    "testnets": true
  }
}
```
