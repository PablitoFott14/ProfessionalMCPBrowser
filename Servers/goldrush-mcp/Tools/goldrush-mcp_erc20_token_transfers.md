## goldrush-mcp_erc20_token_transfers

### What this tool is used for
Retrieves the inbound and outbound ERC-20 token transfer history for a wallet address on a specific chain, including historical prices at the time of each transfer. It is used when the user needs a token-level transaction history for a wallet, optionally scoped to a specific token contract.

---

### Used parameters

**(12) chainName: Required**
Default: No default
Allowed: eth-mainnet, eth-sepolia, eth-holesky, matic-mainnet, avalanche-mainnet, avalanche-testnet, bsc-mainnet, bsc-testnet, moonbeam-mainnet, moonbeam-moonriver, arbitrum-mainnet, arbitrum-nova-mainnet, arbitrum-sepolia, fantom-mainnet, fantom-testnet, btc-mainnet, solana-mainnet, axie-mainnet, optimism-mainnet, optimism-sepolia, cronos-zkevm-mainnet, emerald-paratime-mainnet, monad-testnet, monad-mainnet, megaeth-mainnet, berachain-mainnet, berachain-testnet, hypercore-mainnet, plasma-mainnet, unichain-mainnet, plasma-testnet, arc-testnet, adi-testnet, canto-mainnet, linea-mainnet, linea-sepolia-testnet, polygon-amoy-testnet, mantle-mainnet, base-mainnet, base-sepolia-testnet, oasis-sapphire-mainnet, celo-mainnet, hyperevm-mainnet, adi-mainnet, redstone-mainnet, sei-mainnet, apechain-mainnet, unichain-sepolia-testnet, sonic-mainnet, world-mainnet, world-sepolia-testnet, manta-sepolia-testnet, ink-sepolia-testnet, ink-mainnet, zksync-mainnet, bnb-opbnb-mainnet, zetachain-mainnet, gnosis-mainnet, gnosis-testnet, viction-mainnet, taiko-mainnet, blast-mainnet, scroll-mainnet
The name of the chain to query.

**(9) walletAddress: Required**
Default: No default
The wallet address to retrieve token transfers for. ENS, RNS, Lens Handle, and Unstoppable Domain names resolve automatically.

**(19) contractAddress: Required**
Default: No default
The token contract address to filter transfers by. Pass null to retrieve transfers across all ERC-20 tokens. ENS, RNS, Lens Handle, and Unstoppable Domain names resolve automatically.

**(8) quoteCurrency: Optional**
Default: null
Allowed: USD, CAD, EUR, SGD, INR, JPY, VND, CNY, KRW, RUB, TRY, NGN, ARS, AUD, CHF, GBP
Currency used for historical price conversions in the response.

**(20) startingBlock: Optional**
Default: null
The block height to start from. Defaults to block 0 if omitted.

**(21) endingBlock: Optional**
Default: null
The block height to end at. Defaults to the current block height if omitted.

**(17) pageSize: Optional**
Default: null
Number of transfer records to return per page. Defaults to 100 if omitted.

**(18) pageNumber: Optional**
Default: null
0-indexed page number to begin pagination.

---

### JSON input alternatives

```json
{
  "intent": "Get the full USDC transfer history for a wallet on Ethereum",
  "params": {
    "chainName": "eth-mainnet",
    "walletAddress": "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045",
    "contractAddress": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
    "quoteCurrency": "USD"
  }
}

{
  "intent": "Retrieve all ERC-20 transfers for a wallet on Arbitrum within a specific block range",
  "params": {
    "chainName": "arbitrum-mainnet",
    "walletAddress": "vitalik.eth",
    "contractAddress": null,
    "startingBlock": 180000000,
    "endingBlock": 185000000,
    "quoteCurrency": "USD",
    "pageSize": 50
  }
}
```
