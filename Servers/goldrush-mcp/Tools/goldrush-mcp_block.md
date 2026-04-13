## goldrush-mcp_block

### What this tool is used for
Block fetches a single block by height for a given chain. It is used when the user needs to inspect or render the details of a specific block, such as for a block explorer view, or to check the state of the latest block on a network.

---

### Used parameters

**(12) chainName — Required**
Default: No default
Allowed: eth-mainnet, eth-sepolia, eth-holesky, matic-mainnet, avalanche-mainnet, avalanche-testnet, bsc-mainnet, bsc-testnet, moonbeam-mainnet, moonbeam-moonriver, arbitrum-mainnet, arbitrum-nova-mainnet, arbitrum-sepolia, fantom-mainnet, fantom-testnet, btc-mainnet, solana-mainnet, axie-mainnet, optimism-mainnet, optimism-sepolia, cronos-zkevm-mainnet, emerald-paratime-mainnet, monad-testnet, monad-mainnet, megaeth-mainnet, berachain-mainnet, berachain-testnet, hypercore-mainnet, plasma-mainnet, unichain-mainnet, plasma-testnet, arc-testnet, adi-testnet, canto-mainnet, linea-mainnet, linea-sepolia-testnet, polygon-amoy-testnet, mantle-mainnet, base-mainnet, base-sepolia-testnet, oasis-sapphire-mainnet, celo-mainnet, hyperevm-mainnet, adi-mainnet, redstone-mainnet, sei-mainnet, apechain-mainnet, unichain-sepolia-testnet, sonic-mainnet, world-mainnet, world-sepolia-testnet, manta-sepolia-testnet, ink-sepolia-testnet, ink-mainnet, zksync-mainnet, bnb-opbnb-mainnet, zetachain-mainnet, gnosis-mainnet, gnosis-testnet, viction-mainnet, taiko-mainnet, blast-mainnet, scroll-mainnet
The name of the chain to query.

**(14) blockHeight — Required**
Default: No default
The block height to retrieve. Pass "latest" to fetch the most recent block available.

---

### JSON input alternatives

```json
{
  "intent": "Fetch a specific block by height on Ethereum mainnet",
  "params": {
    "chainName": "eth-mainnet",
    "blockHeight": "19000000"
  }
}

{
  "intent": "Retrieve the latest block on Base",
  "params": {
    "chainName": "base-mainnet",
    "blockHeight": "latest"
  }
}
```
