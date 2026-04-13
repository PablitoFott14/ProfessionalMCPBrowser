## goldrush-mcp_block_heights

### What this tool is used for
Retrieves all block heights within a given date range for a specific chain. It is used when the user needs to map blocks to calendar dates, such as for sorting or displaying blocks by day in a block explorer or analytics view.

---

### Used parameters

**(12) chainName: Required**
Default: No default
Allowed: eth-mainnet, eth-sepolia, eth-holesky, matic-mainnet, avalanche-mainnet, avalanche-testnet, bsc-mainnet, bsc-testnet, moonbeam-mainnet, moonbeam-moonriver, arbitrum-mainnet, arbitrum-nova-mainnet, arbitrum-sepolia, fantom-mainnet, fantom-testnet, btc-mainnet, solana-mainnet, axie-mainnet, optimism-mainnet, optimism-sepolia, cronos-zkevm-mainnet, emerald-paratime-mainnet, monad-testnet, monad-mainnet, megaeth-mainnet, berachain-mainnet, berachain-testnet, hypercore-mainnet, plasma-mainnet, unichain-mainnet, plasma-testnet, arc-testnet, adi-testnet, canto-mainnet, linea-mainnet, linea-sepolia-testnet, polygon-amoy-testnet, mantle-mainnet, base-mainnet, base-sepolia-testnet, oasis-sapphire-mainnet, celo-mainnet, hyperevm-mainnet, adi-mainnet, redstone-mainnet, sei-mainnet, apechain-mainnet, unichain-sepolia-testnet, sonic-mainnet, world-mainnet, world-sepolia-testnet, manta-sepolia-testnet, ink-sepolia-testnet, ink-mainnet, zksync-mainnet, bnb-opbnb-mainnet, zetachain-mainnet, gnosis-mainnet, gnosis-testnet, viction-mainnet, taiko-mainnet, blast-mainnet, scroll-mainnet
The name of the chain to query.

**(15) startDate: Required**
Default: No default
The start of the date range in YYYY-MM-DD format.

**(16) endDate: Required**
Default: No default
The end of the date range in YYYY-MM-DD format, or "latest" to extend to the most recent block available.

**(17) pageSize: Optional**
Default: 10
Number of block heights to return per page.

**(18) pageNumber: Optional**
Default: 0
0-indexed page number to begin pagination.

---

### JSON input alternatives

```json
{
  "intent": "Get all block heights on Ethereum mainnet for a specific week",
  "params": {
    "chainName": "eth-mainnet",
    "startDate": "2024-01-01",
    "endDate": "2024-01-07"
  }
}

{
  "intent": "Paginate through block heights on Base from a start date up to the latest block",
  "params": {
    "chainName": "base-mainnet",
    "startDate": "2024-06-01",
    "endDate": "latest",
    "pageSize": 50,
    "pageNumber": 1
  }
}
```
