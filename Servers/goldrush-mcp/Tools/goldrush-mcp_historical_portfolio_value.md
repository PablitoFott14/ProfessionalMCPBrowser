## goldrush-mcp_historical_portfolio_value

### What this tool is used for
Renders a daily portfolio balance broken down by token for a wallet address over a configurable time window. It is used when the user needs to visualize or analyze how a portfolio's value has changed over time on a specific chain, with per-token granularity.

---

### Used parameters

**(12) chainName: Required**
Default: No default
Allowed: eth-mainnet, eth-sepolia, eth-holesky, matic-mainnet, avalanche-mainnet, avalanche-testnet, bsc-mainnet, bsc-testnet, moonbeam-mainnet, moonbeam-moonriver, arbitrum-mainnet, arbitrum-nova-mainnet, arbitrum-sepolia, fantom-mainnet, fantom-testnet, btc-mainnet, solana-mainnet, axie-mainnet, optimism-mainnet, optimism-sepolia, cronos-zkevm-mainnet, emerald-paratime-mainnet, monad-testnet, monad-mainnet, megaeth-mainnet, berachain-mainnet, berachain-testnet, hypercore-mainnet, plasma-mainnet, unichain-mainnet, plasma-testnet, arc-testnet, adi-testnet, canto-mainnet, linea-mainnet, linea-sepolia-testnet, polygon-amoy-testnet, mantle-mainnet, base-mainnet, base-sepolia-testnet, oasis-sapphire-mainnet, celo-mainnet, hyperevm-mainnet, adi-mainnet, redstone-mainnet, sei-mainnet, apechain-mainnet, unichain-sepolia-testnet, sonic-mainnet, world-mainnet, world-sepolia-testnet, manta-sepolia-testnet, ink-sepolia-testnet, ink-mainnet, zksync-mainnet, bnb-opbnb-mainnet, zetachain-mainnet, gnosis-mainnet, gnosis-testnet, viction-mainnet, taiko-mainnet, blast-mainnet, scroll-mainnet
The name of the chain to query.

**(9) walletAddress: Required**
Default: No default
The wallet address to retrieve portfolio history for. ENS, RNS, Lens Handle, and Unstoppable Domain names resolve automatically.

**(8) quoteCurrency: Optional**
Default: null
Allowed: USD, CAD, EUR, SGD, INR, JPY, VND, CNY, KRW, RUB, TRY, NGN, ARS, AUD, CHF, GBP
Currency used for portfolio value conversions in the response.

**(26) days: Optional**
Default: null
The number of days to return daily portfolio data for. Defaults to 30 days if omitted.

---

### JSON input alternatives

```json
{
  "intent": "Render a 30-day daily portfolio breakdown for a wallet on Ethereum in USD",
  "params": {
    "chainName": "eth-mainnet",
    "walletAddress": "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045",
    "quoteCurrency": "USD"
  }
}

{
  "intent": "Get a 90-day portfolio value history for an ENS address on Base",
  "params": {
    "chainName": "base-mainnet",
    "walletAddress": "vitalik.eth",
    "quoteCurrency": "USD",
    "days": 90
  }
}
```
