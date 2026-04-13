## goldrush-mcp_transaction

### What this tool is used for
Fetches and renders a single transaction by hash on a given chain, including its decoded event logs. For foundational chains it can also return internal transactions, state changes, and the method ID where available. It is used when the user needs to inspect or display the full details of a specific on-chain transaction.

---

### Used parameters

**(12) chainName: Required**
Default: No default
Allowed: eth-mainnet, eth-sepolia, eth-holesky, matic-mainnet, avalanche-mainnet, avalanche-testnet, bsc-mainnet, bsc-testnet, moonbeam-mainnet, moonbeam-moonriver, arbitrum-mainnet, arbitrum-nova-mainnet, arbitrum-sepolia, fantom-mainnet, fantom-testnet, btc-mainnet, solana-mainnet, axie-mainnet, optimism-mainnet, optimism-sepolia, cronos-zkevm-mainnet, emerald-paratime-mainnet, monad-testnet, monad-mainnet, megaeth-mainnet, berachain-mainnet, berachain-testnet, hypercore-mainnet, plasma-mainnet, unichain-mainnet, plasma-testnet, arc-testnet, adi-testnet, canto-mainnet, linea-mainnet, linea-sepolia-testnet, polygon-amoy-testnet, mantle-mainnet, base-mainnet, base-sepolia-testnet, oasis-sapphire-mainnet, celo-mainnet, hyperevm-mainnet, adi-mainnet, redstone-mainnet, sei-mainnet, apechain-mainnet, unichain-sepolia-testnet, sonic-mainnet, world-mainnet, world-sepolia-testnet, manta-sepolia-testnet, ink-sepolia-testnet, ink-mainnet, zksync-mainnet, bnb-opbnb-mainnet, zetachain-mainnet, gnosis-mainnet, gnosis-testnet, viction-mainnet, taiko-mainnet, blast-mainnet, scroll-mainnet
The name of the chain to query.

**(29) txHash: Required**
Default: No default
The transaction hash to retrieve.

**(8) quoteCurrency: Optional**
Default: null
Allowed: USD, CAD, EUR, SGD, INR, JPY, VND, CNY, KRW, RUB, TRY, NGN, ARS, AUD, CHF, GBP
Currency used for value conversions in the response.

**(30) noLogs: Optional**
Default: true
If true, omits log events from the response. Set to false to include decoded event logs.

**(31) withInternal: Optional**
Default: null
Whether to include internal transfers and transactions. Available on foundational chains.

**(32) withState: Optional**
Default: null
Whether to include all transaction state changes with before and after values. Available on foundational chains.

**(33) withInputData: Optional**
Default: null
Whether to include the transaction's input data such as the Method ID. Available on foundational chains.

---

### JSON input alternatives

```json
{
  "intent": "Fetch a transaction on Ethereum with decoded event logs included",
  "params": {
    "chainName": "eth-mainnet",
    "txHash": "0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060",
    "noLogs": false,
    "quoteCurrency": "USD"
  }
}

{
  "intent": "Retrieve a transaction on Base with internal transfers and input data for debugging",
  "params": {
    "chainName": "base-mainnet",
    "txHash": "0xabc123def456abc123def456abc123def456abc123def456abc123def456abc1",
    "noLogs": false,
    "withInternal": true,
    "withInputData": true,
    "quoteCurrency": "USD"
  }
}
```
