## goldrush-mcp_bitcoin_transactions

### What this tool is used for
Bitcoin_transactions fetches the full paginated transaction history for a single Bitcoin non-HD wallet address. It is used when the user needs to review or analyze the on-chain activity of a specific Bitcoin address.

---

### Used parameters

**(37) address — Required**
Default: No default
The Bitcoin address to retrieve transactions for.

**(17) pageSize — Optional**
Default: 10
Number of transactions to return per page. Defaults to 100 if omitted without an explicit value.

**(18) pageNumber — Optional**
Default: 0
0-indexed page number to begin pagination.

---

### JSON input alternatives

```json
{
  "intent": "Fetch the first page of transactions for a Bitcoin address",
  "params": {
    "address": "bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh"
  }
}

{
  "intent": "Paginate through Bitcoin transaction history with a larger page size",
  "params": {
    "address": "bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh",
    "pageSize": 50,
    "pageNumber": 2
  }
}
```
