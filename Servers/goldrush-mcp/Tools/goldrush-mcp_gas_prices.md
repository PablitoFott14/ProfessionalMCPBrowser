## goldrush-mcp_gas_prices

### What this tool is used for
Returns real-time gas estimates for different transaction speeds on a specific network. It is used when the user needs to understand current network fees before submitting a transaction, or wants to compare costs across transaction types such as token transfers, native sends, or Uniswap swaps.

---

### Used parameters

**(12) chainName: Required**
Default: No default
Allowed: eth-mainnet, eth-sepolia, eth-holesky, matic-mainnet, avalanche-mainnet, avalanche-testnet, bsc-mainnet, bsc-testnet, moonbeam-mainnet, moonbeam-moonriver, arbitrum-mainnet, arbitrum-nova-mainnet, arbitrum-sepolia, fantom-mainnet, fantom-testnet, btc-mainnet, solana-mainnet, axie-mainnet, optimism-mainnet, optimism-sepolia, cronos-zkevm-mainnet, emerald-paratime-mainnet, monad-testnet, monad-mainnet, megaeth-mainnet, berachain-mainnet, berachain-testnet, hypercore-mainnet, plasma-mainnet, unichain-mainnet, plasma-testnet, arc-testnet, adi-testnet, canto-mainnet, linea-mainnet, linea-sepolia-testnet, polygon-amoy-testnet, mantle-mainnet, base-mainnet, base-sepolia-testnet, oasis-sapphire-mainnet, celo-mainnet, hyperevm-mainnet, adi-mainnet, redstone-mainnet, sei-mainnet, apechain-mainnet, unichain-sepolia-testnet, sonic-mainnet, world-mainnet, world-sepolia-testnet, manta-sepolia-testnet, ink-sepolia-testnet, ink-mainnet, zksync-mainnet, bnb-opbnb-mainnet, zetachain-mainnet, gnosis-mainnet, gnosis-testnet, viction-mainnet, taiko-mainnet, blast-mainnet, scroll-mainnet
The name of the chain to retrieve gas prices for.

**(13) eventType: Required**
Default: No default
Allowed: erc20, nativetokens, uniswapv3
The transaction event type to retrieve gas estimates for. Use erc20 for token transfers, nativetokens for native asset sends, and uniswapv3 for Uniswap swap events.

**(8) quoteCurrency: Optional**
Default: null
Allowed: USD, CAD, EUR, SGD, INR, JPY, VND, CNY, KRW, RUB, TRY, NGN, ARS, AUD, CHF, GBP
Currency used for gas cost conversions in the response.

---

### JSON input alternatives

```json
{
  "intent": "Get current gas prices for ERC-20 token transfers on Ethereum mainnet in USD",
  "params": {
    "chainName": "eth-mainnet",
    "eventType": "erc20",
    "quoteCurrency": "USD"
  }
}

{
  "intent": "Check gas estimates for a Uniswap v3 swap on Base",
  "params": {
    "chainName": "base-mainnet",
    "eventType": "uniswapv3",
    "quoteCurrency": "USD"
  }
}
```
