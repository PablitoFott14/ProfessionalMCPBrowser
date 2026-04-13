## goldrush-mcp_token_balances

### What this tool is used for
Token_balances fetches the native and ERC-20 token holdings for a wallet address on a specific chain, including spot prices and token metadata. It is used when the user needs a single-chain portfolio snapshot with enriched token data rather than a cross-chain view.

---

### Used parameters

**(12) chainName — Required**
Default: No default
Allowed: eth-mainnet, eth-sepolia, eth-holesky, matic-mainnet, avalanche-mainnet, avalanche-testnet, bsc-mainnet, bsc-testnet, moonbeam-mainnet, moonbeam-moonriver, arbitrum-mainnet, arbitrum-nova-mainnet, arbitrum-sepolia, fantom-mainnet, fantom-testnet, btc-mainnet, solana-mainnet, axie-mainnet, optimism-mainnet, optimism-sepolia, cronos-zkevm-mainnet, emerald-paratime-mainnet, monad-testnet, monad-mainnet, megaeth-mainnet, berachain-mainnet, berachain-testnet, hypercore-mainnet, plasma-mainnet, unichain-mainnet, plasma-testnet, arc-testnet, adi-testnet, canto-mainnet, linea-mainnet, linea-sepolia-testnet, polygon-amoy-testnet, mantle-mainnet, base-mainnet, base-sepolia-testnet, oasis-sapphire-mainnet, celo-mainnet, hyperevm-mainnet, adi-mainnet, redstone-mainnet, sei-mainnet, apechain-mainnet, unichain-sepolia-testnet, sonic-mainnet, world-mainnet, world-sepolia-testnet, manta-sepolia-testnet, ink-sepolia-testnet, ink-mainnet, zksync-mainnet, bnb-opbnb-mainnet, zetachain-mainnet, gnosis-mainnet, gnosis-testnet, viction-mainnet, taiko-mainnet, blast-mainnet, scroll-mainnet
The name of the chain to query.

**(9) walletAddress — Required**
Default: No default
The wallet address to retrieve token balances for. ENS, RNS, Lens Handle, and Unstoppable Domain names resolve automatically.

**(8) quoteCurrency — Optional**
Default: null
Allowed: USD, CAD, EUR, SGD, INR, JPY, VND, CNY, KRW, RUB, TRY, NGN, ARS, AUD, CHF, GBP
Currency used for spot price conversions in the response.

**(24) noSpam — Optional**
Default: null
If true, suspected spam tokens are removed from the response. Supported on all Foundational Chains.

---

### JSON input alternatives

```json
{
  "intent": "Get all token balances for a wallet on Ethereum with spam tokens filtered out",
  "params": {
    "chainName": "eth-mainnet",
    "walletAddress": "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045",
    "quoteCurrency": "USD",
    "noSpam": true
  }
}

{
  "intent": "Fetch token holdings for an ENS name on Arbitrum",
  "params": {
    "chainName": "arbitrum-mainnet",
    "walletAddress": "vitalik.eth",
    "quoteCurrency": "EUR"
  }
}
```
