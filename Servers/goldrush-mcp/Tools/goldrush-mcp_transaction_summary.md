## goldrush-mcp_transaction_summary

### What this tool is used for
Fetches a high-level activity overview for a wallet address on a given chain, including the earliest and latest transactions, total transaction count, ERC-20 token transfer count, and optionally a gas expenditure breakdown. It is used when the user needs a quick wallet activity profile rather than a full paginated transaction history.

---

### Used parameters

**(12) chainName: Required**
Default: No default
Allowed: eth-mainnet, eth-sepolia, eth-holesky, matic-mainnet, avalanche-mainnet, avalanche-testnet, bsc-mainnet, bsc-testnet, moonbeam-mainnet, moonbeam-moonriver, arbitrum-mainnet, arbitrum-nova-mainnet, arbitrum-sepolia, fantom-mainnet, fantom-testnet, btc-mainnet, solana-mainnet, axie-mainnet, optimism-mainnet, optimism-sepolia, cronos-zkevm-mainnet, emerald-paratime-mainnet, monad-testnet, monad-mainnet, megaeth-mainnet, berachain-mainnet, berachain-testnet, hypercore-mainnet, plasma-mainnet, unichain-mainnet, plasma-testnet, arc-testnet, adi-testnet, canto-mainnet, linea-mainnet, linea-sepolia-testnet, polygon-amoy-testnet, mantle-mainnet, base-mainnet, base-sepolia-testnet, oasis-sapphire-mainnet, celo-mainnet, hyperevm-mainnet, adi-mainnet, redstone-mainnet, sei-mainnet, apechain-mainnet, unichain-sepolia-testnet, sonic-mainnet, world-mainnet, world-sepolia-testnet, manta-sepolia-testnet, ink-sepolia-testnet, ink-mainnet, zksync-mainnet, bnb-opbnb-mainnet, zetachain-mainnet, gnosis-mainnet, gnosis-testnet, viction-mainnet, taiko-mainnet, blast-mainnet, scroll-mainnet
The name of the chain to query.

**(9) walletAddress: Required**
Default: No default
The wallet address to summarize. ENS, RNS, Lens Handle, and Unstoppable Domain names resolve automatically.

**(8) quoteCurrency: Optional**
Default: null
Allowed: USD, CAD, EUR, SGD, INR, JPY, VND, CNY, KRW, RUB, TRY, NGN, ARS, AUD, CHF, GBP
Currency used for value conversions in the response.

**(34) withGas: Optional**
Default: null
If true, includes a gas expenditure summary. Note: may increase response time for wallets with a large number of transactions.

---

### JSON input alternatives

```json
{
  "intent": "Get a transaction activity overview for a wallet on Ethereum",
  "params": {
    "chainName": "eth-mainnet",
    "walletAddress": "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045",
    "quoteCurrency": "USD"
  }
}

{
  "intent": "Summarize wallet activity on Arbitrum including total gas spent",
  "params": {
    "chainName": "arbitrum-mainnet",
    "walletAddress": "vitalik.eth",
    "quoteCurrency": "USD",
    "withGas": true
  }
}
```
