## goldrush-mcp_multichain_transactions

### What this tool is used for
Fetches paginated transactions for up to 10 EVM addresses across up to 10 chains in a single call. It is used when the user needs a unified activity feed across multiple wallets or chains, rather than querying each chain individually.

---

### Used parameters

**(1) chains — Optional**
Default: all foundational chains
Allowed: eth-mainnet, eth-sepolia, eth-holesky, matic-mainnet, avalanche-mainnet, avalanche-testnet, bsc-mainnet, bsc-testnet, moonbeam-mainnet, moonbeam-moonriver, arbitrum-mainnet, arbitrum-nova-mainnet, arbitrum-sepolia, fantom-mainnet, fantom-testnet, btc-mainnet, solana-mainnet, axie-mainnet, optimism-mainnet, optimism-sepolia, cronos-zkevm-mainnet, emerald-paratime-mainnet, monad-testnet, monad-mainnet, megaeth-mainnet, berachain-mainnet, berachain-testnet, hypercore-mainnet, plasma-mainnet, unichain-mainnet, plasma-testnet, arc-testnet, adi-testnet, canto-mainnet, linea-mainnet, linea-sepolia-testnet, polygon-amoy-testnet, mantle-mainnet, base-mainnet, base-sepolia-testnet, oasis-sapphire-mainnet, celo-mainnet, hyperevm-mainnet, adi-mainnet, redstone-mainnet, sei-mainnet, apechain-mainnet, unichain-sepolia-testnet, sonic-mainnet, world-mainnet, world-sepolia-testnet, manta-sepolia-testnet, ink-sepolia-testnet, ink-mainnet, zksync-mainnet, bnb-opbnb-mainnet, zetachain-mainnet, gnosis-mainnet, gnosis-testnet, viction-mainnet, taiko-mainnet, blast-mainnet, scroll-mainnet, or any numeric chain ID
List of chains to retrieve transactions from. Accepts up to 10 entries.

**(2) addresses — Optional**
Default: null
List of wallet addresses to retrieve transactions for. Accepts up to 10 entries.

**(3) limit — Optional**
Default: 10
Number of transactions to return per page, up to a maximum of 100.

**(4) before — Optional**
Default: null
Pagination cursor for fetching transactions before a certain point.

**(5) after — Optional**
Default: null
Pagination cursor for fetching transactions after a certain point.

**(6) withLogs — Optional**
Default: false
Whether to include raw logs in the response.

**(7) withDecodedLogs — Optional**
Default: false
Whether to include decoded logs in the response.

**(8) quoteCurrency — Optional**
Default: null
Allowed: USD, CAD, EUR, SGD, INR, JPY, VND, CNY, KRW, RUB, TRY, NGN, ARS, AUD, CHF, GBP
Currency used for value conversions in the response.

---

### JSON input alternatives

```json
{
  "intent": "Build a cross-chain activity feed for a single wallet across Ethereum, Base, and Arbitrum",
  "params": {
    "addresses": ["0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"],
    "chains": ["eth-mainnet", "base-mainnet", "arbitrum-mainnet"],
    "quoteCurrency": "USD",
    "limit": 25
  }
}

{
  "intent": "Fetch the next page of transactions for two wallets on Polygon and BSC with decoded logs",
  "params": {
    "addresses": ["0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045", "0xAb5801a7D398351b8bE11C439e05C5B3259aeC9B"],
    "chains": ["matic-mainnet", "bsc-mainnet"],
    "withDecodedLogs": true,
    "after": "cursor_abc123"
  }
}
```
