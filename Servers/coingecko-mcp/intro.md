## coingecko-mcp

The `coingecko-mcp` server provides access to the full CoinGecko API through a code execution model. Rather than exposing individual endpoints as separate tools, it gives access to the entire API surface through a single execution tool backed by a documentation search tool. It is the right server when the goal is to query any CoinGecko data — prices, market caps, historical charts, trending assets, coin metadata, exchanges, or token details — with full control over what is retrieved and how results are shaped.

### How it works

- All API interaction goes through `coingecko-mcp_execute`, which runs a TypeScript async function against an initialized SDK client. The function must be named `run`, accept the client as its single argument, and return or log whatever data is needed.
- `coingecko-mcp_search_docs` is a companion discovery tool that searches the SDK documentation for methods, parameters, and usage examples before code is written. It supports multiple languages but TypeScript is the relevant choice for this server.
- Because the server exposes the full CoinGecko API rather than a fixed set of endpoints, the range of queries is broad — but each call requires knowing the correct SDK method and parameter structure.

### Potential resolution paths

- **Look up a method, then execute it:** Use `coingecko-mcp_search_docs` to find the right SDK method and its parameter shape for a given topic (e.g., coin market chart, trending, exchanges), then pass the corresponding code to `coingecko-mcp_execute`.
- **Query current market data for one or more assets:** Call `coingecko-mcp_execute` directly with `client.simple.price.get` when the method is already known, passing the target coin IDs and currency.
- **Retrieve historical price or volume data for a coin:** Use `coingecko-mcp_search_docs` to confirm the correct chart endpoint, then call `coingecko-mcp_execute` with the appropriate coin ID, currency, and date range parameters.
- **Explore trending or top-ranked coins:** Call `coingecko-mcp_execute` with a markets or trending endpoint to retrieve ranked lists, optionally filtering by category, order, or page.

### Best practices

- **Search the documentation before executing when the SDK method is not known:** `coingecko-mcp_search_docs` eliminates guesswork about method names and parameter shapes — using it first avoids failed or malformed execute calls.
- **Return data explicitly from the `run` function:** The execute tool captures both return values and console output, but returning structured data directly produces cleaner results than relying on logging alone.
