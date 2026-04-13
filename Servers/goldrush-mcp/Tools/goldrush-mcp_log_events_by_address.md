## goldrush-mcp_log_events_by_address

### What this tool is used for
Retrieves all event logs emitted from a specific contract address on a given chain. It is used when the user needs to examine on-chain interactions for a contract, such as tracking transfers, swaps, mints, or other contract-level activity within a block range.

---

### Used parameters

**(12) chainName — Required**
Default: No default
Allowed: eth-mainnet, eth-sepolia, eth-holesky, matic-mainnet, avalanche-mainnet, avalanche-testnet, bsc-mainnet, bsc-testnet, moonbeam-mainnet, moonbeam-moonriver, arbitrum-mainnet, arbitrum-nova-mainnet, arbitrum-sepolia, fantom-mainnet, fantom-testnet, btc-mainnet, solana-mainnet, axie-mainnet, optimism-mainnet, optimism-sepolia, cronos-zkevm-mainnet, emerald-paratime-mainnet, monad-testnet, monad-mainnet, megaeth-mainnet, berachain-mainnet, berachain-testnet, hypercore-mainnet, plasma-mainnet, unichain-mainnet, plasma-testnet, arc-testnet, adi-testnet, canto-mainnet, linea-mainnet, linea-sepolia-testnet, polygon-amoy-testnet, mantle-mainnet, base-mainnet, base-sepolia-testnet, oasis-sapphire-mainnet, celo-mainnet, hyperevm-mainnet, adi-mainnet, redstone-mainnet, sei-mainnet, apechain-mainnet, unichain-sepolia-testnet, sonic-mainnet, world-mainnet, world-sepolia-testnet, manta-sepolia-testnet, ink-sepolia-testnet, ink-mainnet, zksync-mainnet, bnb-opbnb-mainnet, zetachain-mainnet, gnosis-mainnet, gnosis-testnet, viction-mainnet, taiko-mainnet, blast-mainnet, scroll-mainnet
The name of the chain to query.

**(19) contractAddress — Required**
Default: No default
The contract address to retrieve event logs for. ENS, RNS, Lens Handle, and Unstoppable Domain names resolve automatically.

**(20) startingBlock — Optional**
Default: null
The first block to retrieve log events from. Accepts a decimal, hexadecimal, or the strings "earliest" or "latest".

**(21) endingBlock — Optional**
Default: null
The last block to retrieve log events from. Accepts a decimal, hexadecimal, or the strings "earliest" or "latest".

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
  "intent": "Fetch recent event logs from a Uniswap v3 pool contract on Ethereum",
  "params": {
    "chainName": "eth-mainnet",
    "contractAddress": "0x88e6A0c2dDD26FEEb64F039a2c41296FcB3f5640",
    "startingBlock": 19000000,
    "endingBlock": "latest"
  }
}

{
  "intent": "Paginate through all historical event logs for an NFT contract on Polygon",
  "params": {
    "chainName": "matic-mainnet",
    "contractAddress": "0x2953399124F0cBB46d2CbACD8A89cF0599974963",
    "startingBlock": "earliest",
    "endingBlock": "latest",
    "pageSize": 50,
    "pageNumber": 2
  }
}
```
