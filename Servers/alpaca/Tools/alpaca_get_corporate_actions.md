## alpaca_get_corporate_actions

### What this tool is for
Retrieves corporate action announcements from Alpaca, such as splits, dividends, mergers, and spin-offs. Use this when the user needs to track events that affect share structure or value for one or more stocks.

---

### Used parameters

**(6) ca_types — Optional**
Default: null (all types)
List of corporate action types to filter by. Available values: reverse_split, forward_split, unit_split, cash_dividend, stock_dividend, spin_off, cash_merger, stock_merger, stock_and_cash_merger, redemption, name_change, worthless_removal, rights_distribution.

**(7) start — Optional**
Default: null (current day)
Start date for the announcements (e.g., 2024-01-01).

**(8) end — Optional**
Default: null (current day)
End date for the announcements (e.g., 2024-12-31).

**(9) symbols — Optional**
Default: null
List of ticker symbols to filter results by.

**(10) cusips — Optional**
Default: null
List of CUSIP identifiers to filter results by.

**(11) ids — Optional**
Default: null
List of corporate action IDs to retrieve. Mutually exclusive with other filters.

**(12) limit — Optional**
Default: 1000
Maximum number of results to return.

**(13) sort — Optional**
Default: asc
Sort order of the results (asc or desc).

---

### JSON input alternatives

```json
{
  "intent": "Get all cash dividends and stock splits announced in Q1 2024",
  "params": {
    "ca_types": ["cash_dividend", "forward_split"],
    "start": "2024-01-01",
    "end": "2024-03-31"
  }
}
```

```json
{
  "intent": "Retrieve all corporate actions for Apple and Tesla over the past year",
  "params": {
    "symbols": ["AAPL", "TSLA"],
    "start": "2024-01-01",
    "end": "2024-12-31",
    "sort": "desc"
  }
}
```
