## goldrush-mcp_transactions_for_address

### What this tool is used for
Transactions_for_address retrieves paginated transactions involving a wallet address on a given chain, optionally including decoded log events. It is used when the user needs to browse or display a wallet's full on-chain transaction history in a paginated format, with control over sort order and log inclusion.

---

### Used parameters

**(12) chainName — Required**
Default: No default
Allowed: eth-mainnet, eth-sepolia, eth-holesky, matic-mainnet, avalanche-mainnet, avalanche-testnet, bsc-mainnet, bsc-testnet, moonbeam-mainnet, moonbeam-moonriver, arbitrum-mainnet, arbitrum-nova-mainnet, arbitrum-sepolia, fantom-mainnet, fantom-testnet, btc-mainnet, solana-mainnet, axie-mainnet, optimism-mainnet, optimism-sepolia, cronos-zkevm-mainnet, emerald-paratime-mainnet, monad-testnet, monad-mainnet, megaeth-mainnet, berachain-mainnet, berachain-testnet, hypercore-mainnet, plasma-mainnet, unichain-mainnet, plasma-testnet, arc-testnet, adi-testnet, canto-mainnet, linea-mainnet, linea-sepolia-testnet, polygon-amoy-testnet, mantle-mainnet, base-mainnet, base-sepolia-testnet, oasis-sapphire-mainnet, celo-mainnet, hyperevm-mainnet, adi-mainnet, redstone-mainnet, sei-mainnet, apechain-mainnet, unichain-sepolia-testnet, sonic-mainnet, world-mainnet, world-sepolia-testnet, manta-sepolia-testnet, ink-sepolia-testnet, ink-mainnet, zksync-mainnet, bnb-opbnb-mainnet, zetachain-mainnet, gnosis-mainnet, gnosis-testnet, viction-mainnet, taiko-mainnet, blast-mainnet, scroll-mainnet
The name of the chain to query.

**(9) walletAddress — Required**
Default: No default
The wallet address to retrieve transactions for. ENS, RNS, Lens Handle, and Unstoppable Domain names resolve automatically.

**(35) page — Required**
Default: No default
The page number to retrieve, 0-indexed.

**(8) quoteCurrency — Optional**
Default: null
Allowed: USD, CAD, EUR, SGD, INR, JPY, VND, CNY, KRW, RUB, TRY, NGN, ARS, AUD, CHF, GBP
Currency used for value conversions in the response.

**(30) noLogs — Optional**
Default: true
If true, omits log events from the response. Set to false to include decoded event logs.

**(36) blockSignedAtAsc — Optional**
Default: null
If true, returns transactions in ascending chronological order. Defaults to descending order if omitted.

---

### JSON input alternatives

```json
{
  "intent": "Fetch the first page of transactions for a wallet on Ethereum in descending order",
  "params": {
    "chainName": "eth-mainnet",
    "walletAddress": "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045",
    "page": 0,
    "quoteCurrency": "USD"
  }
}

{
  "intent": "Retrieve the second page of transactions for an ENS address on Base with logs, in chronological order",
  "params": {
    "chainName": "base-mainnet",
    "walletAddress": "vitalik.eth",
    "page": 1,
    "noLogs": false,
    "blockSignedAtAsc": true,
    "quoteCurrency": "USD"
  }
}
```
