## fred-mcp-server

The fred-mcp-server is an economic data research server centered on FRED series discovery, catalog browsing, and direct series retrieval. It is useful when the user needs to find relevant economic indicators, explore the structure of the FRED catalog, or pull observations for a known series.

### How it works
- The server supports three main workflows: keyword and filter-based series search, catalog browsing through categories, releases, or sources, and direct retrieval of series observations by `series_id`.
- Common inputs include search fields such as `search_text`, `tag_names`, and search filters, browse controls such as `browse_type`, `category_id`, and `release_id`, and retrieval controls such as `observation_start`, `observation_end`, `units`, `frequency`, and `aggregation_method`.
- It can be used either for discovery, when the user does not yet know the series ID, or for direct data retrieval once the target series has already been identified.

### Potential resolution paths
- **Search for an indicator, then retrieve its data:** Start with `fred_search` to locate relevant series by keyword or filter, then move into `fred_get_series` once the correct `series_id` is known.
- **Browse the catalog before narrowing to a series:** Use `fred_browse` to explore categories, releases, sources, or series collections, then pick a series from those results for direct retrieval with `fred_get_series`.
- **Move from raw observations into transformed views:** Pull a known series with `fred_get_series`, then use options such as `units`, `frequency`, or `aggregation_method` when the user needs a transformed or resampled version of the same series.

### Best practices
- **Use search or browse before direct retrieval when the series ID is uncertain:** `fred_search` and `fred_browse` are better starting points than guessing a `series_id`.
- **Match retrieval settings to the question being asked:** Use date filters for time-bounded requests, `units` for transformed values, and `frequency` plus `aggregation_method` when the user needs data at a different cadence.
