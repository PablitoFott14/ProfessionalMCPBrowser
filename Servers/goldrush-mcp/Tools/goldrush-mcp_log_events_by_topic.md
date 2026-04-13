## goldrush-mcp_log_events_by_topic

### What this tool is used for
Log_events_by_topic retrieves all event logs matching a given topic hash across all contracts on a chain. It is used when the user needs cross-sectional analysis of a specific event type — such as all ERC-20 Transfer events or all Uniswap Swap events — regardless of which contract emitted them.

---

### Used parameters

**(12) chainName — Required**
Default: No default
Allowed: eth-mainnet, eth-sepolia, eth-holesky, matic-mainnet, avalanche-mainnet, avalanche-testnet, bsc-mainnet, bsc-testnet, moonbeam-mainnet, moonbeam-moonriver, arbitrum-mainnet, arbitrum-nova-mainnet, arbitrum-sepolia, fantom-mainnet, fantom-testnet, btc-mainnet, solana-mainnet, axie-mainnet, optimism-mainnet, optimism-sepolia, cronos-zkevm-mainnet, emerald-paratime-mainnet, monad-testnet, monad-mainnet, megaeth-mainnet, berachain-mainnet, berachain-testnet, hypercore-mainnet, plasma-mainnet, unichain-mainnet, plasma-testnet, arc-testnet, adi-testnet, canto-mainnet, linea-mainnet, linea-sepolia-testnet, polygon-amoy-testnet, mantle-mainnet, base-mainnet, base-sepolia-testnet, oasis-sapphire-mainnet, celo-mainnet, hyperevm-mainnet, adi-mainnet, redstone-mainnet, sei-mainnet, apechain-mainnet, unichain-sepolia-testnet, sonic-mainnet, world-mainnet, world-sepolia-testnet, manta-sepolia-testnet, ink-sepolia-testnet, ink-mainnet, zksync-mainnet, bnb-opbnb-mainnet, zetachain-mainnet, gnosis-mainnet, gnosis-testnet, viction-mainnet, taiko-mainnet, blast-mainnet, scroll-mainnet
The name of the chain to query.

**(22) topicHash — Required**
Default: No default
The topic hash to filter event logs by. Returns all logs across all contracts that contain this topic hash.

**(20) startingBlock — Optional**
Default: null
The first block to retrieve log events from. Accepts a decimal, hexadecimal, or the strings "earliest" or "latest".

**(21) endingBlock — Optional**
Default: null
The last block to retrieve log events from. Accepts a decimal, hexadecimal, or the strings "earliest" or "latest".

**(23) secondaryTopics — Optional**
Default: null
Additional topic hash(es) to narrow results. Padded and unpadded address fields are supported. Separate multiple topics with a comma.

**(17) pageSize — Optional**
Default: 10
Number of log events to return per page.

**(18) pageNumber — Optional**
Default: 0
0-indexed page number to begin pagination.

---

### JSON input alternatives

```json
{
  "intent": "Fetch all ERC-20 Transfer events across Ethereum mainnet within a block range",
  "params": {
    "chainName": "eth-mainnet",
    "topicHash": "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",
    "startingBlock": 19000000,
    "endingBlock": 19001000
  }
}

{
  "intent": "Find all Transfer events for a specific token by filtering on a secondary topic address",
  "params": {
    "chainName": "eth-mainnet",
    "topicHash": "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",
    "startingBlock": 19000000,
    "endingBlock": "latest",
    "secondaryTopics": "0x000000000000000000000000d8dA6BF26964aF9D7eEd9e03E53415D37aA96045",
    "pageSize": 50
  }
}
```
