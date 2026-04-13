## goldrush-mcp_nft_check_ownership

### What this tool is used for
Nft_check_ownership verifies whether a wallet address owns any NFTs within a specific collection, supporting both ERC-721 and ERC-1155 standards. It is used when the user needs to confirm ownership of a collection, optionally filtered down to NFTs with a particular trait and value.

---

### Used parameters

**(12) chainName — Required**
Default: No default
Allowed: eth-mainnet, eth-sepolia, eth-holesky, matic-mainnet, avalanche-mainnet, avalanche-testnet, bsc-mainnet, bsc-testnet, moonbeam-mainnet, moonbeam-moonriver, arbitrum-mainnet, arbitrum-nova-mainnet, arbitrum-sepolia, fantom-mainnet, fantom-testnet, btc-mainnet, solana-mainnet, axie-mainnet, optimism-mainnet, optimism-sepolia, cronos-zkevm-mainnet, emerald-paratime-mainnet, monad-testnet, monad-mainnet, megaeth-mainnet, berachain-mainnet, berachain-testnet, hypercore-mainnet, plasma-mainnet, unichain-mainnet, plasma-testnet, arc-testnet, adi-testnet, canto-mainnet, linea-mainnet, linea-sepolia-testnet, polygon-amoy-testnet, mantle-mainnet, base-mainnet, base-sepolia-testnet, oasis-sapphire-mainnet, celo-mainnet, hyperevm-mainnet, adi-mainnet, redstone-mainnet, sei-mainnet, apechain-mainnet, unichain-sepolia-testnet, sonic-mainnet, world-mainnet, world-sepolia-testnet, manta-sepolia-testnet, ink-sepolia-testnet, ink-mainnet, zksync-mainnet, bnb-opbnb-mainnet, zetachain-mainnet, gnosis-mainnet, gnosis-testnet, viction-mainnet, taiko-mainnet, blast-mainnet, scroll-mainnet
The name of the chain to query.

**(9) walletAddress — Required**
Default: No default
The wallet address to verify ownership for. ENS, RNS, Lens Handle, and Unstoppable Domain names resolve automatically.

**(38) collectionContract — Required**
Default: No default
The NFT collection contract address to check ownership against.

**(39) traitsFilter — Optional**
Default: null
Filters results to NFTs with a specific trait name. Must be used together with valuesFilter. Case-sensitive.

**(40) valuesFilter — Optional**
Default: null
Filters results to NFTs with a specific trait value. Must be used together with traitsFilter. Case-sensitive.

---

### JSON input alternatives

```json
{
  "intent": "Check whether a wallet owns any NFTs in the Bored Ape Yacht Club collection",
  "params": {
    "chainName": "eth-mainnet",
    "walletAddress": "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045",
    "collectionContract": "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D"
  }
}

{
  "intent": "Verify ownership of NFTs with a specific trait in a collection on Polygon",
  "params": {
    "chainName": "matic-mainnet",
    "walletAddress": "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045",
    "collectionContract": "0x2953399124F0cBB46d2CbACD8A89cF0599974963",
    "traitsFilter": "Background",
    "valuesFilter": "Blue"
  }
}
```
