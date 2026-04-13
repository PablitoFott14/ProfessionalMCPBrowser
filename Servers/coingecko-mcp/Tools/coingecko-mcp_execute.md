## coingecko-mcp_execute

### What this tool is used for
Runs TypeScript code against an initialized CoinGecko SDK client. It is used when the user needs to query any part of the CoinGecko API — prices, market data, coin metadata, exchanges, trending assets, or historical data — by writing a short async function that calls the relevant SDK method and returns or logs the result.

---

### Used parameters

**(1) code: Required**
Default: No default
TypeScript async function named `run` that accepts the initialized SDK client and interacts with the CoinGecko API. Anything returned or logged by the function is included in the response.

**(2) intent: Optional**
Default: null
Natural language description of the task being performed. Used for improving the service.

---

### JSON input alternatives

```json
{
  "intent": "Get the current USD price of Bitcoin and Ethereum",
  "params": {
    "code": "async function run(client) { return await client.simple.price.get({ ids: 'bitcoin,ethereum', vs_currencies: 'usd' }); }"
  }
}

{
  "intent": "Retrieve the top 10 coins ranked by market cap",
  "params": {
    "code": "async function run(client) { return await client.coins.markets.get({ vs_currency: 'usd', order: 'market_cap_desc', per_page: 10, page: 1 }); }"
  }
}
```
