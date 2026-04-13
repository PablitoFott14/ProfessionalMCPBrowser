## goldrush-mcp_pool_spot_prices

### What this tool is used for
Pool_spot_prices returns the current spot token pair prices for a specified liquidity pool contract address. It supports pools on Uniswap V2, V3, and their forks. It is used when the user needs the live exchange rate between a token pair in a specific DEX pool.

---

### Used parameters

**(12) chainName — Required**
Default: No default
Allowed: eth-mainnet, eth-sepolia, eth-holesky, matic-mainnet, avalanche-mainnet, avalanche-testnet, bsc-mainnet, bsc-testnet, moonbeam-mainnet, moonbeam-moonriver, arbitrum-mainnet, arbitrum-nova-mainnet, arbitrum-sepolia, fantom-mainnet, fantom-testnet, btc-mainnet, solana-mainnet, axie-mainnet, optimism-mainnet, optimism-sepolia, cronos-zkevm-mainnet, emerald-paratime-mainnet, monad-testnet, monad-mainnet, megaeth-mainnet, berachain-mainnet, berachain-testnet, hypercore-mainnet, plasma-mainnet, unichain-mainnet, plasma-testnet, arc-testnet, adi-testnet, canto-mainnet, linea-mainnet, linea-sepolia-testnet, polygon-amoy-testnet, mantle-mainnet, base-mainnet, base-sepolia-testnet, oasis-sapphire-mainnet, celo-mainnet, hyperevm-mainnet, adi-mainnet, redstone-mainnet, sei-mainnet, apechain-mainnet, unichain-sepolia-testnet, sonic-mainnet, world-mainnet, world-sepolia-testnet, manta-sepolia-testnet, ink-sepolia-testnet, ink-mainnet, zksync-mainnet, bnb-opbnb-mainnet, zetachain-mainnet, gnosis-mainnet, gnosis-testnet, viction-mainnet, taiko-mainnet, blast-mainnet, scroll-mainnet
The name of the chain to query.

**(19) contractAddress — Required**
Default: No default
The liquidity pool contract address to retrieve spot prices for.

**(8) quoteCurrency — Optional**
Default: null
Allowed: USD, CAD, EUR, SGD, INR, JPY, VND, CNY, KRW, RUB, TRY, NGN, ARS, AUD, CHF, GBP
Currency used for price conversions in the response.

---

### JSON input alternatives

```json
{
  "intent": "Get the current spot price for the USDC/ETH Uniswap V3 pool on Ethereum",
  "params": {
    "chainName": "eth-mainnet",
    "contractAddress": "0x88e6A0c2dDD26FEEb64F039a2c41296FcB3f5640",
    "quoteCurrency": "USD"
  }
}

{
  "intent": "Fetch spot prices for a Uniswap V2 pool on Base",
  "params": {
    "chainName": "base-mainnet",
    "contractAddress": "0x4C36388bE6F416A29C8d8Eee81C771cE6bE14B18",
    "quoteCurrency": "USD"
  }
}
```
