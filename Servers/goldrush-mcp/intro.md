## goldrush-mcp

The goldrush-mcp server is a comprehensive on-chain data layer for EVM chains, Bitcoin, and NFTs. It covers wallet balances, transaction history, token transfers, event logs, block data, NFT ownership, DeFi pool prices, gas estimates, and historical snapshots — all accessible through a consistent set of address- and chain-scoped tools. It is the right server when the goal is to retrieve, inspect, or analyze blockchain state across one or many chains without writing direct RPC calls.

### How it works

- Most tools are scoped to a `chainName` plus a wallet address, contract address, or block identifier. Multi-chain tools accept arrays of up to 10 chains and addresses in a single call; single-chain tools take one chain and one address.
- Domain name resolution (ENS, RNS, Lens Handle, Unstoppable Domains) is supported natively in most wallet and contract address fields, but not in all tools — `multichain_balances` explicitly requires a raw address.
- Bitcoin is covered through dedicated tools that accept either an extended public key (HD wallets) or a standard non-HD address, separate from the EVM tool set.
- Pagination varies by tool: some use `page`/`pageNumber`/`pageSize`, others use cursor-based `before`/`after` parameters.

### Potential resolution paths

- **Build a cross-chain wallet dashboard:** Use `multichain_address_activity` to discover which chains a wallet is active on, then call `multichain_balances` or `multichain_transactions` scoped to only those chains.
- **Inspect a single-chain wallet in depth:** Start with `token_balances` or `native_token_balance` for the current holdings, then use `erc20_token_transfers` for token-level history, `transaction_summary` for a quick activity overview, and `transactions_for_address` for full paginated transaction history.
- **Audit wallet exposure and security:** Use `token_approvals` to surface which contracts have spending permissions, then cross-reference with `erc20_token_transfers` to understand what activity those approvals have generated.
- **Explore blocks and transactions:** Use `block_heights` to map a date range to block numbers, `block` or `transactions_for_block` to inspect block contents, and `transaction` to drill into a specific hash with decoded logs, internal transfers, and state changes.
- **Analyze contract-level on-chain activity:** Use `log_events_by_address` to retrieve all events from a specific contract, or `log_events_by_topic` to find all instances of a given event type across the entire chain.
- **Work with NFTs:** Use `nft_for_address` to retrieve a wallet's full NFT holdings, `nft_check_ownership` to verify collection-level ownership, and `nft_check_ownership_token_id` to confirm ownership of a specific token.
- **Reconstruct historical portfolio state:** Use `historical_token_balances` or `historical_portfolio_value` to snapshot a wallet at a past date or block, and `historical_token_prices` to retrieve the price series for the relevant tokens over that window.
- **Query Bitcoin wallets:** Use `bitcoin_hd_wallet_balances` for HD wallets via an extended public key, or `bitcoin_non_hd_wallet_balances` and `bitcoin_transactions` for standard non-HD addresses.

### Best practices

- **Use `multichain_address_activity` before multi-chain queries when the active chains are unknown:** Scoping `multichain_balances` or `multichain_transactions` to only the chains where a wallet has activity avoids unnecessary calls and reduces response size.
- **Use `resolve_address` before tools that do not support automatic domain resolution:** Tools such as `multichain_balances` require a raw address — passing an ENS name directly will fail, so resolving it first with `resolve_address` is necessary when starting from a human-readable name.
