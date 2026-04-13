## goldrush-mcp_token_holders

### What this tool is used for
Returns a paginated list of current or historical holders for a specified ERC-20 or ERC-721 token. It is used when the user needs to analyze token ownership distribution, track holder counts over time, or retrieve a snapshot of holders at a specific block or date.

---

### Used parameters

**(12) chainName: Required**
Default: No default
Allowed: eth-mainnet, eth-sepolia, eth-holesky, matic-mainnet, avalanche-mainnet, avalanche-testnet, bsc-mainnet, bsc-testnet, moonbeam-mainnet, moonbeam-moonriver, arbitrum-mainnet, arbitrum-nova-mainnet, arbitrum-sepolia, fantom-mainnet, fantom-testnet, btc-mainnet, solana-mainnet, axie-mainnet, optimism-mainnet, optimism-sepolia, cronos-zkevm-mainnet, emerald-paratime-mainnet, monad-testnet, monad-mainnet, megaeth-mainnet, berachain-mainnet, berachain-testnet, hypercore-mainnet, plasma-mainnet, unichain-mainnet, plasma-testnet, arc-testnet, adi-testnet, canto-mainnet, linea-mainnet, linea-sepolia-testnet, polygon-amoy-testnet, mantle-mainnet, base-mainnet, base-sepolia-testnet, oasis-sapphire-mainnet, celo-mainnet, hyperevm-mainnet, adi-mainnet, redstone-mainnet, sei-mainnet, apechain-mainnet, unichain-sepolia-testnet, sonic-mainnet, world-mainnet, world-sepolia-testnet, manta-sepolia-testnet, ink-sepolia-testnet, ink-mainnet, zksync-mainnet, bnb-opbnb-mainnet, zetachain-mainnet, gnosis-mainnet, gnosis-testnet, viction-mainnet, taiko-mainnet, blast-mainnet, scroll-mainnet
The name of the chain to query.

**(27) tokenAddress: Required**
Default: No default
The token contract address to retrieve holders for. ENS, RNS, Lens Handle, and Unstoppable Domain names resolve automatically.

**(28) noSnapshot: Optional**
Default: null
If true, bypasses the last snapshot and returns the latest token holders list in real time.

**(14) blockHeight: Optional**
Default: null
Block height to use as the upper bound for the holders snapshot. Defaults to the latest block if omitted. Accepts a block number or string.

**(25) date: Optional**
Default: null
Date in YYYY-MM-DD format to use as the upper bound for the holders snapshot. Defaults to the current date if omitted.

**(17) pageSize: Optional**
Default: null
Number of holders to return per page. Only values of 100 and 1000 are supported. Defaults to 100 if omitted.

**(18) pageNumber: Optional**
Default: null
0-indexed page number to begin pagination.

---

### JSON input alternatives

```json
{
  "intent": "Get the current top holders of USDC on Ethereum mainnet",
  "params": {
    "chainName": "eth-mainnet",
    "tokenAddress": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
    "noSnapshot": true
  }
}

{
  "intent": "Retrieve historical token holders for an ERC-721 NFT collection at a specific past date",
  "params": {
    "chainName": "eth-mainnet",
    "tokenAddress": "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D",
    "date": "2024-01-01",
    "pageSize": 1000,
    "pageNumber": 0
  }
}
```
