## goldrush-mcp_token_approvals

### What this tool is used for
Token_approvals retrieves a list of all token approvals granted by a wallet address across all token contracts, categorized by spender. It is used when the user needs to audit which contracts have been approved to spend their tokens, typically as part of a security or risk review.

---

### Used parameters

**(12) chainName — Required**
Default: No default
Allowed: eth-mainnet, eth-sepolia, eth-holesky, matic-mainnet, avalanche-mainnet, avalanche-testnet, bsc-mainnet, bsc-testnet, moonbeam-mainnet, moonbeam-moonriver, arbitrum-mainnet, arbitrum-nova-mainnet, arbitrum-sepolia, fantom-mainnet, fantom-testnet, btc-mainnet, solana-mainnet, axie-mainnet, optimism-mainnet, optimism-sepolia, cronos-zkevm-mainnet, emerald-paratime-mainnet, monad-testnet, monad-mainnet, megaeth-mainnet, berachain-mainnet, berachain-testnet, hypercore-mainnet, plasma-mainnet, unichain-mainnet, plasma-testnet, arc-testnet, adi-testnet, canto-mainnet, linea-mainnet, linea-sepolia-testnet, polygon-amoy-testnet, mantle-mainnet, base-mainnet, base-sepolia-testnet, oasis-sapphire-mainnet, celo-mainnet, hyperevm-mainnet, adi-mainnet, redstone-mainnet, sei-mainnet, apechain-mainnet, unichain-sepolia-testnet, sonic-mainnet, world-mainnet, world-sepolia-testnet, manta-sepolia-testnet, ink-sepolia-testnet, ink-mainnet, zksync-mainnet, bnb-opbnb-mainnet, zetachain-mainnet, gnosis-mainnet, gnosis-testnet, viction-mainnet, taiko-mainnet, blast-mainnet, scroll-mainnet
The name of the chain to query.

**(9) walletAddress — Required**
Default: No default
The wallet address to retrieve token approvals for. ENS, RNS, Lens Handle, and Unstoppable Domain names resolve automatically.

---

### JSON input alternatives

```json
{
  "intent": "Audit all token approvals for a wallet on Ethereum mainnet",
  "params": {
    "chainName": "eth-mainnet",
    "walletAddress": "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"
  }
}

{
  "intent": "Check token approvals for an ENS address on Arbitrum",
  "params": {
    "chainName": "arbitrum-mainnet",
    "walletAddress": "vitalik.eth"
  }
}
```
