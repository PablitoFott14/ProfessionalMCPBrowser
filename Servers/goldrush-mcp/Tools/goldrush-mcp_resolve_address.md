## goldrush-mcp_resolve_address

### What this tool is used for
Resolves a registered domain name — ENS, RNS, or Unstoppable Domain — to its underlying wallet address on a given chain. It is used when the user has a human-readable domain and needs the corresponding on-chain address before querying balances, transactions, or other address-specific data.

---

### Used parameters

**(12) chainName — Required**
Default: No default
Allowed: eth-mainnet, eth-sepolia, eth-holesky, matic-mainnet, avalanche-mainnet, avalanche-testnet, bsc-mainnet, bsc-testnet, moonbeam-mainnet, moonbeam-moonriver, arbitrum-mainnet, arbitrum-nova-mainnet, arbitrum-sepolia, fantom-mainnet, fantom-testnet, btc-mainnet, solana-mainnet, axie-mainnet, optimism-mainnet, optimism-sepolia, cronos-zkevm-mainnet, emerald-paratime-mainnet, monad-testnet, monad-mainnet, megaeth-mainnet, berachain-mainnet, berachain-testnet, hypercore-mainnet, plasma-mainnet, unichain-mainnet, plasma-testnet, arc-testnet, adi-testnet, canto-mainnet, linea-mainnet, linea-sepolia-testnet, polygon-amoy-testnet, mantle-mainnet, base-mainnet, base-sepolia-testnet, oasis-sapphire-mainnet, celo-mainnet, hyperevm-mainnet, adi-mainnet, redstone-mainnet, sei-mainnet, apechain-mainnet, unichain-sepolia-testnet, sonic-mainnet, world-mainnet, world-sepolia-testnet, manta-sepolia-testnet, ink-sepolia-testnet, ink-mainnet, zksync-mainnet, bnb-opbnb-mainnet, zetachain-mainnet, gnosis-mainnet, gnosis-testnet, viction-mainnet, taiko-mainnet, blast-mainnet, scroll-mainnet
The name of the chain to resolve the domain on.

**(9) walletAddress — Required**
Default: No default
The domain name to resolve. Supports ENS, RNS, Lens Handle, and Unstoppable Domain formats.

---

### JSON input alternatives

```json
{
  "intent": "Resolve an ENS name to its Ethereum mainnet address",
  "params": {
    "chainName": "eth-mainnet",
    "walletAddress": "vitalik.eth"
  }
}

{
  "intent": "Resolve an Unstoppable Domain to an address on Polygon",
  "params": {
    "chainName": "matic-mainnet",
    "walletAddress": "mydomain.crypto"
  }
}
```
