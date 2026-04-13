## goldrush-mcp_historical_token_balances

### What this tool is used for
Historical_token_balances fetches the native and ERC-20 token holdings for a wallet address at a specific historical point in time, defined by either a block height or a date. It is used when the user needs to reconstruct a past portfolio snapshot rather than the current state, including daily prices and token metadata at that point.

---

### Used parameters

**(12) chainName — Required**
Default: No default
Allowed: eth-mainnet, eth-sepolia, eth-holesky, matic-mainnet, avalanche-mainnet, avalanche-testnet, bsc-mainnet, bsc-testnet, moonbeam-mainnet, moonbeam-moonriver, arbitrum-mainnet, arbitrum-nova-mainnet, arbitrum-sepolia, fantom-mainnet, fantom-testnet, btc-mainnet, solana-mainnet, axie-mainnet, optimism-mainnet, optimism-sepolia, cronos-zkevm-mainnet, emerald-paratime-mainnet, monad-testnet, monad-mainnet, megaeth-mainnet, berachain-mainnet, berachain-testnet, hypercore-mainnet, plasma-mainnet, unichain-mainnet, plasma-testnet, arc-testnet, adi-testnet, canto-mainnet, linea-mainnet, linea-sepolia-testnet, polygon-amoy-testnet, mantle-mainnet, base-mainnet, base-sepolia-testnet, oasis-sapphire-mainnet, celo-mainnet, hyperevm-mainnet, adi-mainnet, redstone-mainnet, sei-mainnet, apechain-mainnet, unichain-sepolia-testnet, sonic-mainnet, world-mainnet, world-sepolia-testnet, manta-sepolia-testnet, ink-sepolia-testnet, ink-mainnet, zksync-mainnet, bnb-opbnb-mainnet, zetachain-mainnet, gnosis-mainnet, gnosis-testnet, viction-mainnet, taiko-mainnet, blast-mainnet, scroll-mainnet
The name of the chain to query.

**(9) walletAddress — Required**
Default: No default
The wallet address to retrieve historical balances for. ENS, RNS, Lens Handle, and Unstoppable Domain names resolve automatically.

**(8) quoteCurrency — Optional**
Default: null
Allowed: USD, CAD, EUR, SGD, INR, JPY, VND, CNY, KRW, RUB, TRY, NGN, ARS, AUD, CHF, GBP
Currency used for price conversions in the response.

**(24) noSpam — Optional**
Default: null
If true, suspected spam tokens are removed from the response. Supported on all Foundational Chains.

**(14) blockHeight — Optional**
Default: null
Ending block height to define the historical snapshot. Defaults to the latest block if omitted.

**(25) date — Optional**
Default: null
Ending date in YYYY-MM-DD format to define the historical snapshot. Defaults to the current date if omitted.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve a wallet's token holdings on Ethereum as of a specific past date",
  "params": {
    "chainName": "eth-mainnet",
    "walletAddress": "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045",
    "date": "2024-01-01",
    "quoteCurrency": "USD",
    "noSpam": true
  }
}

{
  "intent": "Reconstruct a portfolio snapshot at a specific block height on Arbitrum",
  "params": {
    "chainName": "arbitrum-mainnet",
    "walletAddress": "vitalik.eth",
    "blockHeight": 180000000,
    "quoteCurrency": "USD"
  }
}
```
