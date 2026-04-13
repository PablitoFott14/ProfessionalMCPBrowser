## goldrush-mcp_nft_for_address

### What this tool is used for
Retrieves the ERC-721 and ERC-1155 NFTs held by a wallet address on a given chain. It is used when the user needs to render or inspect an NFT portfolio, with options to strip spam tokens and control the level of metadata detail returned.

---

### Used parameters

**(12) chainName — Required**
Default: No default
Allowed: eth-mainnet, eth-sepolia, eth-holesky, matic-mainnet, avalanche-mainnet, avalanche-testnet, bsc-mainnet, bsc-testnet, moonbeam-mainnet, moonbeam-moonriver, arbitrum-mainnet, arbitrum-nova-mainnet, arbitrum-sepolia, fantom-mainnet, fantom-testnet, btc-mainnet, solana-mainnet, axie-mainnet, optimism-mainnet, optimism-sepolia, cronos-zkevm-mainnet, emerald-paratime-mainnet, monad-testnet, monad-mainnet, megaeth-mainnet, berachain-mainnet, berachain-testnet, hypercore-mainnet, plasma-mainnet, unichain-mainnet, plasma-testnet, arc-testnet, adi-testnet, canto-mainnet, linea-mainnet, linea-sepolia-testnet, polygon-amoy-testnet, mantle-mainnet, base-mainnet, base-sepolia-testnet, oasis-sapphire-mainnet, celo-mainnet, hyperevm-mainnet, adi-mainnet, redstone-mainnet, sei-mainnet, apechain-mainnet, unichain-sepolia-testnet, sonic-mainnet, world-mainnet, world-sepolia-testnet, manta-sepolia-testnet, ink-sepolia-testnet, ink-mainnet, zksync-mainnet, bnb-opbnb-mainnet, zetachain-mainnet, gnosis-mainnet, gnosis-testnet, viction-mainnet, taiko-mainnet, blast-mainnet, scroll-mainnet
The name of the chain to query.

**(9) walletAddress — Required**
Default: No default
The wallet address to retrieve NFTs for. ENS, RNS, Lens Handle, and Unstoppable Domain names resolve automatically.

**(24) noSpam — Optional**
Default: true
If true, suspected spam NFTs are removed from the response. Supported on all Foundational Chains.

**(41) noNftAssetMetadata — Optional**
Default: true
If true, limits the response to a list of collections and token IDs only, omitting metadata and asset information. Set to false to include full NFT metadata. Recommended to keep true for wallets holding a large number of NFTs.

---

### JSON input alternatives

```json
{
  "intent": "Fetch a full NFT portfolio with metadata for a wallet on Ethereum",
  "params": {
    "chainName": "eth-mainnet",
    "walletAddress": "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045",
    "noNftAssetMetadata": false
  }
}

{
  "intent": "Get a lightweight NFT holdings list for an ENS address on Base, spam filtered",
  "params": {
    "chainName": "base-mainnet",
    "walletAddress": "vitalik.eth",
    "noSpam": true,
    "noNftAssetMetadata": true
  }
}
```
