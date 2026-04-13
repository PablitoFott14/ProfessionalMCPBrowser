## goldrush-mcp_multichain_balances

### What this tool is used for
Fetches paginated spot and historical native and token balances for a single wallet address across up to 10 EVM chains in one call. It is used when the user needs a consolidated portfolio view or a historical balance snapshot across multiple chains without querying each one separately.

---

### Used parameters

**(9) walletAddress — Required**
Default: No default
The wallet address to retrieve balances for. Domain names (e.g. demo.eth) are not supported.

**(1) chains — Optional**
Default: all foundational chains
Allowed: eth-mainnet, eth-sepolia, eth-holesky, matic-mainnet, avalanche-mainnet, avalanche-testnet, bsc-mainnet, bsc-testnet, moonbeam-mainnet, moonbeam-moonriver, arbitrum-mainnet, arbitrum-nova-mainnet, arbitrum-sepolia, fantom-mainnet, fantom-testnet, btc-mainnet, solana-mainnet, axie-mainnet, optimism-mainnet, optimism-sepolia, cronos-zkevm-mainnet, emerald-paratime-mainnet, monad-testnet, monad-mainnet, megaeth-mainnet, berachain-mainnet, berachain-testnet, hypercore-mainnet, plasma-mainnet, unichain-mainnet, plasma-testnet, arc-testnet, adi-testnet, canto-mainnet, linea-mainnet, linea-sepolia-testnet, polygon-amoy-testnet, mantle-mainnet, base-mainnet, base-sepolia-testnet, oasis-sapphire-mainnet, celo-mainnet, hyperevm-mainnet, adi-mainnet, redstone-mainnet, sei-mainnet, apechain-mainnet, unichain-sepolia-testnet, sonic-mainnet, world-mainnet, world-sepolia-testnet, manta-sepolia-testnet, ink-sepolia-testnet, ink-mainnet, zksync-mainnet, bnb-opbnb-mainnet, zetachain-mainnet, gnosis-mainnet, gnosis-testnet, viction-mainnet, taiko-mainnet, blast-mainnet, scroll-mainnet, or any numeric chain ID
List of chains to retrieve balances from. Accepts up to 10 entries.

**(8) quoteCurrency — Optional**
Default: null
Allowed: USD, CAD, EUR, SGD, INR, JPY, VND, CNY, KRW, RUB, TRY, NGN, ARS, AUD, CHF, GBP
Currency used for value conversions in the response.

**(3) limit — Optional**
Default: 10
Number of token balances to return per page, up to a maximum of 100.

**(4) before — Optional**
Default: null
Pagination cursor for fetching balances before a certain point.

**(10) cutoffTimestamp — Optional**
Default: null
UNIX timestamp used to retrieve a balance snapshot from the nearest block before the specified time.

---

### JSON input alternatives

```json
{
  "intent": "Get current token balances for a wallet across Ethereum, Optimism, and Base in USD",
  "params": {
    "walletAddress": "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045",
    "chains": ["eth-mainnet", "optimism-mainnet", "base-mainnet"],
    "quoteCurrency": "USD"
  }
}

{
  "intent": "Retrieve a historical balance snapshot for a wallet at a specific point in time",
  "params": {
    "walletAddress": "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045",
    "chains": ["eth-mainnet", "matic-mainnet"],
    "cutoffTimestamp": 1704067200,
    "quoteCurrency": "USD"
  }
}
```
