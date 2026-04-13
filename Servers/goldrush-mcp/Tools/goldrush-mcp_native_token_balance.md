## goldrush-mcp_native_token_balance

### What this tool is used for
Is a lightweight endpoint that returns only the native token balance for a single EVM address on a given chain. It is used when the user needs a fast, minimal check of an address's native asset holdings (e.g. ETH, MATIC, BNB) without the overhead of a full token balance response.

---

### Used parameters

**(12) chainName — Required**
Default: No default
Allowed: eth-mainnet, eth-sepolia, eth-holesky, matic-mainnet, avalanche-mainnet, avalanche-testnet, bsc-mainnet, bsc-testnet, moonbeam-mainnet, moonbeam-moonriver, arbitrum-mainnet, arbitrum-nova-mainnet, arbitrum-sepolia, fantom-mainnet, fantom-testnet, btc-mainnet, solana-mainnet, axie-mainnet, optimism-mainnet, optimism-sepolia, cronos-zkevm-mainnet, emerald-paratime-mainnet, monad-testnet, monad-mainnet, megaeth-mainnet, berachain-mainnet, berachain-testnet, hypercore-mainnet, plasma-mainnet, unichain-mainnet, plasma-testnet, arc-testnet, adi-testnet, canto-mainnet, linea-mainnet, linea-sepolia-testnet, polygon-amoy-testnet, mantle-mainnet, base-mainnet, base-sepolia-testnet, oasis-sapphire-mainnet, celo-mainnet, hyperevm-mainnet, adi-mainnet, redstone-mainnet, sei-mainnet, apechain-mainnet, unichain-sepolia-testnet, sonic-mainnet, world-mainnet, world-sepolia-testnet, manta-sepolia-testnet, ink-sepolia-testnet, ink-mainnet, zksync-mainnet, bnb-opbnb-mainnet, zetachain-mainnet, gnosis-mainnet, gnosis-testnet, viction-mainnet, taiko-mainnet, blast-mainnet, scroll-mainnet
The name of the chain to query.

**(9) walletAddress — Required**
Default: No default
The wallet address to retrieve the native token balance for. ENS, RNS, Lens Handle, and Unstoppable Domain names resolve automatically.

**(8) quoteCurrency — Optional**
Default: null
Allowed: USD, CAD, EUR, SGD, INR, JPY, VND, CNY, KRW, RUB, TRY, NGN, ARS, AUD, CHF, GBP
Currency used for native token value conversion in the response.

**(14) blockHeight — Optional**
Default: null
Block height to use as the upper bound for the balance lookup. Defaults to the latest block if omitted. Accepts a block number or string.

---

### JSON input alternatives

```json
{
  "intent": "Check the current ETH balance for a wallet on Ethereum mainnet",
  "params": {
    "chainName": "eth-mainnet",
    "walletAddress": "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045",
    "quoteCurrency": "USD"
  }
}

{
  "intent": "Get the MATIC balance of an ENS address on Polygon at a specific block",
  "params": {
    "chainName": "matic-mainnet",
    "walletAddress": "vitalik.eth",
    "blockHeight": 55000000,
    "quoteCurrency": "USD"
  }
}
```
