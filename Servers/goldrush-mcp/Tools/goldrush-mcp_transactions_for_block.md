## goldrush-mcp_transactions_for_block

### What this tool is used for
Fetches all transactions in a given block on a specific chain, including their decoded log events. It is used when the user needs to inspect the full contents of a block — for example, to flag interesting wallets or transactions, analyze block-level activity, or build a block explorer view.

---

### Used parameters

**(12) chainName: Required**
Default: No default
Allowed: eth-mainnet, eth-sepolia, eth-holesky, matic-mainnet, avalanche-mainnet, avalanche-testnet, bsc-mainnet, bsc-testnet, moonbeam-mainnet, moonbeam-moonriver, arbitrum-mainnet, arbitrum-nova-mainnet, arbitrum-sepolia, fantom-mainnet, fantom-testnet, btc-mainnet, solana-mainnet, axie-mainnet, optimism-mainnet, optimism-sepolia, cronos-zkevm-mainnet, emerald-paratime-mainnet, monad-testnet, monad-mainnet, megaeth-mainnet, berachain-mainnet, berachain-testnet, hypercore-mainnet, plasma-mainnet, unichain-mainnet, plasma-testnet, arc-testnet, adi-testnet, canto-mainnet, linea-mainnet, linea-sepolia-testnet, polygon-amoy-testnet, mantle-mainnet, base-mainnet, base-sepolia-testnet, oasis-sapphire-mainnet, celo-mainnet, hyperevm-mainnet, adi-mainnet, redstone-mainnet, sei-mainnet, apechain-mainnet, unichain-sepolia-testnet, sonic-mainnet, world-mainnet, world-sepolia-testnet, manta-sepolia-testnet, ink-sepolia-testnet, ink-mainnet, zksync-mainnet, bnb-opbnb-mainnet, zetachain-mainnet, gnosis-mainnet, gnosis-testnet, viction-mainnet, taiko-mainnet, blast-mainnet, scroll-mainnet
The name of the chain to query.

**(14) blockHeight: Required**
Default: No default
The block height to retrieve transactions for. Accepts a block number, hexadecimal string, or "latest".

**(8) quoteCurrency: Optional**
Default: null
Allowed: USD, CAD, EUR, SGD, INR, JPY, VND, CNY, KRW, RUB, TRY, NGN, ARS, AUD, CHF, GBP
Currency used for value conversions in the response.

**(30) noLogs: Optional**
Default: null
If true, omits decoded log events from the response.

---

### JSON input alternatives

```json
{
  "intent": "Fetch all transactions in a specific Ethereum block with decoded logs",
  "params": {
    "chainName": "eth-mainnet",
    "blockHeight": 19000000,
    "noLogs": false,
    "quoteCurrency": "USD"
  }
}

{
  "intent": "Retrieve all transactions in the latest Base block",
  "params": {
    "chainName": "base-mainnet",
    "blockHeight": "latest",
    "quoteCurrency": "USD"
  }
}
```
