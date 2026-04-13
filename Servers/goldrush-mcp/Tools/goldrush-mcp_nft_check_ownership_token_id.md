## goldrush-mcp_nft_check_ownership_token_id

### What this tool is used for
Verifies whether a wallet address owns a specific token ID within an NFT collection, supporting both ERC-721 and ERC-1155 standards. It is used when the user needs to confirm ownership of a precise token rather than any NFT within a collection.

---

### Used parameters

**(12) chainName: Required**
Default: No default
Allowed: eth-mainnet, eth-sepolia, eth-holesky, matic-mainnet, avalanche-mainnet, avalanche-testnet, bsc-mainnet, bsc-testnet, moonbeam-mainnet, moonbeam-moonriver, arbitrum-mainnet, arbitrum-nova-mainnet, arbitrum-sepolia, fantom-mainnet, fantom-testnet, btc-mainnet, solana-mainnet, axie-mainnet, optimism-mainnet, optimism-sepolia, cronos-zkevm-mainnet, emerald-paratime-mainnet, monad-testnet, monad-mainnet, megaeth-mainnet, berachain-mainnet, berachain-testnet, hypercore-mainnet, plasma-mainnet, unichain-mainnet, plasma-testnet, arc-testnet, adi-testnet, canto-mainnet, linea-mainnet, linea-sepolia-testnet, polygon-amoy-testnet, mantle-mainnet, base-mainnet, base-sepolia-testnet, oasis-sapphire-mainnet, celo-mainnet, hyperevm-mainnet, adi-mainnet, redstone-mainnet, sei-mainnet, apechain-mainnet, unichain-sepolia-testnet, sonic-mainnet, world-mainnet, world-sepolia-testnet, manta-sepolia-testnet, ink-sepolia-testnet, ink-mainnet, zksync-mainnet, bnb-opbnb-mainnet, zetachain-mainnet, gnosis-mainnet, gnosis-testnet, viction-mainnet, taiko-mainnet, blast-mainnet, scroll-mainnet
The name of the chain to query.

**(9) walletAddress: Required**
Default: No default
The wallet address to verify ownership for. ENS, RNS, Lens Handle, and Unstoppable Domain names resolve automatically.

**(38) collectionContract: Required**
Default: No default
The NFT collection contract address. ENS, RNS, Lens Handle, and Unstoppable Domain names resolve automatically.

**(42) tokenId: Required**
Default: No default
The specific token ID to verify ownership of within the collection.

---

### JSON input alternatives

```json
{
  "intent": "Check whether a wallet owns a specific Bored Ape token by ID",
  "params": {
    "chainName": "eth-mainnet",
    "walletAddress": "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045",
    "collectionContract": "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D",
    "tokenId": "1234"
  }
}

{
  "intent": "Verify ERC-1155 token ownership for an ENS address on Polygon",
  "params": {
    "chainName": "matic-mainnet",
    "walletAddress": "vitalik.eth",
    "collectionContract": "0x2953399124F0cBB46d2CbACD8A89cF0599974963",
    "tokenId": "42"
  }
}
```
