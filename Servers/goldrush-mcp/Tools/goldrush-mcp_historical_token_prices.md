## goldrush-mcp_historical_token_prices

### What this tool is used for
Retrieves daily historical prices for one or more large-cap ERC-20 or native tokens within a specified date range on a given chain. It is used when the user needs price history for valuation, charting, or portfolio analysis across a defined time window.

---

### Used parameters

**(12) chainName — Required**
Default: No default
Allowed: eth-mainnet, eth-sepolia, eth-holesky, matic-mainnet, avalanche-mainnet, avalanche-testnet, bsc-mainnet, bsc-testnet, moonbeam-mainnet, moonbeam-moonriver, arbitrum-mainnet, arbitrum-nova-mainnet, arbitrum-sepolia, fantom-mainnet, fantom-testnet, btc-mainnet, solana-mainnet, axie-mainnet, optimism-mainnet, optimism-sepolia, cronos-zkevm-mainnet, emerald-paratime-mainnet, monad-testnet, monad-mainnet, megaeth-mainnet, berachain-mainnet, berachain-testnet, hypercore-mainnet, plasma-mainnet, unichain-mainnet, plasma-testnet, arc-testnet, adi-testnet, canto-mainnet, linea-mainnet, linea-sepolia-testnet, polygon-amoy-testnet, mantle-mainnet, base-mainnet, base-sepolia-testnet, oasis-sapphire-mainnet, celo-mainnet, hyperevm-mainnet, adi-mainnet, redstone-mainnet, sei-mainnet, apechain-mainnet, unichain-sepolia-testnet, sonic-mainnet, world-mainnet, world-sepolia-testnet, manta-sepolia-testnet, ink-sepolia-testnet, ink-mainnet, zksync-mainnet, bnb-opbnb-mainnet, zetachain-mainnet, gnosis-mainnet, gnosis-testnet, viction-mainnet, taiko-mainnet, blast-mainnet, scroll-mainnet
The name of the chain to query.

**(8) quoteCurrency — Required**
Default: No default
Allowed: USD, CAD, EUR, SGD, INR, JPY, VND, CNY, KRW, RUB, TRY, NGN, ARS, AUD, CHF, GBP
Currency used for historical price values in the response.

**(19) contractAddress — Required**
Default: No default
The token contract address to retrieve price history for. ENS, RNS, Lens Handle, and Unstoppable Domain names resolve automatically. Supports multiple addresses separated by commas.

**(43) from — Required**
Default: No default
The start date of the historical price range in YYYY-MM-DD format.

**(44) to — Required**
Default: No default
The end date of the historical price range in YYYY-MM-DD format.

**(45) pricesAtAsc — Optional**
Default: null
If true, returns prices in ascending chronological order. Defaults to descending order if omitted.

---

### JSON input alternatives

```json
{
  "intent": "Get daily USDC price history on Ethereum for Q1 2024",
  "params": {
    "chainName": "eth-mainnet",
    "quoteCurrency": "USD",
    "contractAddress": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
    "from": "2024-01-01",
    "to": "2024-03-31",
    "pricesAtAsc": true
  }
}

{
  "intent": "Retrieve historical prices for two tokens on Base over a 30-day window",
  "params": {
    "chainName": "base-mainnet",
    "quoteCurrency": "USD",
    "contractAddress": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913,0x4200000000000000000000000000000000000006",
    "from": "2024-06-01",
    "to": "2024-06-30"
  }
}
```
