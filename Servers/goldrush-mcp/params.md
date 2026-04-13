(1) chains
Comma separated list of chain names or IDs to retrieve data from.
Optional. Default: all foundational chains.

(2) addresses
Comma separated list of wallet addresses to retrieve data for.
Optional. Default: null.

(3) limit
Number of items to return per page, up to a maximum of 100.
Optional. Default: 10.

(4) before
Pagination cursor pointing to fetch results before a certain point.
Optional. Default: null.

(5) after
Pagination cursor pointing to fetch results after a certain point.
Optional. Default: null.

(6) withLogs
Whether to include raw logs in the response.
Optional. Default: false.

(7) withDecodedLogs
Whether to include decoded logs in the response.
Optional. Default: false.

(8) quoteCurrency
The currency to use for value conversions in the response.
Optional. Default: null.

(9) walletAddress
The wallet address to retrieve data for. Domain name resolution support varies by tool.
Required. No default value.

(10) cutoffTimestamp
UNIX timestamp used to retrieve a balance snapshot from the nearest block before the specified time.
Optional. Default: null.

(11) testnets
Whether to include testnet chains in the response.
Optional. Default: false.

(12) chainName
The name of the chain to query.
Required. No default value.

(13) eventType
The transaction event type to retrieve gas prices for.
Required. No default value.

(14) blockHeight
A block height used to scope the query. Accepts a block number. Required or optional depending on the tool.
No default value.

(15) startDate
The start date in YYYY-MM-DD format.
Required. No default value.

(16) endDate
The end date in YYYY-MM-DD format, or "latest" for the most recent block available.
Required. No default value.

(17) pageSize
Number of items to return per page.
Optional. Default: 10.

(18) pageNumber
0-indexed page number to begin pagination.
Optional. Default: 0.

(19) contractAddress
The contract address to retrieve data for. ENS, RNS, Lens Handle, and Unstoppable Domain names resolve automatically.
Required. No default value.

(20) startingBlock
The first block to retrieve data from. Accepts decimals, hexadecimals, or the strings "earliest" and "latest".
Optional. Default: null.

(21) endingBlock
The last block to retrieve data from. Accepts decimals, hexadecimals, or the strings "earliest" and "latest".
Optional. Default: null.

(22) topicHash
The topic hash to filter event logs by. Returns all logs across contracts that contain this topic hash.
Required. No default value.

(23) secondaryTopics
Additional topic hash(es) to filter on. Padded and unpadded address fields are supported. Separate multiple topics with a comma.
Optional. Default: null.

(24) noSpam
If true, suspected spam tokens are removed from the response. Supported on all Foundational Chains.
Optional. Default: null.

(25) date
A date in YYYY-MM-DD format used to scope the query to a specific point in time.
Optional. Default: null.

(26) days
The number of days to return data for.
Optional. Default: null.

(27) tokenAddress
The token contract address to retrieve data for. ENS, RNS, Lens Handle, and Unstoppable Domain names resolve automatically.
Required. No default value.

(28) noSnapshot
If true, bypasses the last snapshot and returns the latest token holders list.
Optional. Default: null.

(29) txHash
The transaction hash to retrieve.
Required. No default value.

(30) noLogs
If true, omits log events from the response.
Optional. Default: true.

(31) withInternal
Whether to include internal transfers and transactions in the response.
Optional. Default: null.

(32) withState
Whether to include all transaction state changes with before and after values.
Optional. Default: null.

(33) withInputData
Whether to include the transaction's input data such as the Method ID.
Optional. Default: null.

(34) withGas
Whether to include gas expenditure summary details in the response. May impact response times for wallets with a large number of transactions.
Optional. Default: null.

(35) page
The requested page number, 0-indexed.
Required. No default value.

(36) blockSignedAtAsc
If true, sorts transactions in ascending chronological order. Defaults to descending order if omitted.
Optional. Default: null.

(37) address
A single blockchain address to query.
Required. No default value.

(38) collectionContract
The NFT collection contract address to query.
Required. No default value.

(39) traitsFilter
Filters NFTs by a specific trait name. Must be used together with valuesFilter. Case-sensitive and requires proper URL encoding.
Optional. Default: null.

(40) valuesFilter
Filters NFTs by a specific trait value. Must be used together with traitsFilter. Case-sensitive and requires proper URL encoding.
Optional. Default: null.

(41) noNftAssetMetadata
If true, limits the response to a list of collections and token IDs, omitting metadata and asset information. Useful for faster responses with large NFT portfolios.
Optional. Default: true.

(42) tokenId
The specific NFT token ID to query within a collection.
Required. No default value.

(43) from
The start date of the date range in YYYY-MM-DD format.
Required. No default value.

(44) to
The end date of the date range in YYYY-MM-DD format.
Required. No default value.

(45) pricesAtAsc
If true, sorts prices in ascending chronological order. Defaults to descending order if omitted.
Optional. Default: null.
