## propublica-mcp_search_similar_nonprofits

### What this tool is used for
Finds nonprofits similar to a reference organization based on NTEE category, geographic proximity, and revenue range. Use it when benchmarking an organization against peers or identifying comparable nonprofits in the same sector or region.

---

### Used parameters

**(7) ein: Required**
Default: No default
EIN of the reference nonprofit to find similar organizations for (9 digits, with or without hyphen).

**(10) radius_miles: Optional**
Default: null
Limits results to organizations within this distance in miles from the reference organization.

**(11) same_ntee: Optional**
Default: true
Whether to restrict results to nonprofits in the same NTEE category as the reference organization.

**(12) min_revenue: Optional**
Default: null
Filters out organizations with annual revenue below this amount.

**(13) max_revenue: Optional**
Default: null
Filters out organizations with annual revenue above this amount.

**(9) limit: Optional**
Default: 10
Maximum number of similar organizations to return. Maximum: 25 for this tool.

---

### JSON input alternatives

```json
{
  "intent": "Find nonprofits similar to a reference organization in the same NTEE category",
  "params": {
    "ein": "131655952"
  }
}
```

```json
{
  "intent": "Find nearby nonprofits in the same category within a revenue range",
  "params": {
    "ein": "131655952",
    "radius_miles": 50,
    "min_revenue": 1000000,
    "max_revenue": 10000000,
    "limit": 20
  }
}
```
