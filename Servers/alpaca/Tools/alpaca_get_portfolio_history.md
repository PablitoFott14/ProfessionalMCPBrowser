## alpaca_get_portfolio_history

### What this tool is for
The account's portfolio history, including equity value and P/L over a specified time window and resolution. Use this when the user wants to review how their portfolio has performed over time, analyze drawdowns, or visualize equity curves.

---

### Used parameters

**(14) timeframe — Optional**
Default: null
Resolution of each data point (e.g., 1Min, 5Min, 15Min, 1H, 1D).

**(15) period — Optional**
Default: null
Length of the time window to retrieve (e.g., 1W, 1M, 3M, 6M, 1Y, all).

**(7) start — Optional**
Default: null
Start time in ISO format (YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS).

**(8) end — Optional**
Default: null
End time in ISO format (YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS).

**(16) date_end — Optional**
Default: null
Alternative end date for the range, as ISO date or datetime.

**(17) intraday_reporting — Optional**
Default: null
Allowed: market_hours, extended_hours, continuous
Controls which hours are included in intraday data.

**(18) pnl_reset — Optional**
Default: null
Defines when P/L resets within the period (e.g., daily, weekly, no_reset).

**(19) extended_hours — Optional**
Default: null
Whether to include extended trading hours data where applicable.

**(20) cashflow_types — Optional**
Default: null
List of cashflow categories to include in the response.

---

### JSON input alternatives

```json
{
  "tool": "alpaca_get_portfolio_history",
  "intent": "Get daily equity and P/L for the past 3 months",
  "params": {
    "period": "3M",
    "timeframe": "1D"
  }
}
```

```json
{
  "tool": "alpaca_get_portfolio_history",
  "intent": "Retrieve 1-hour resolution portfolio history for a specific date range including extended hours",
  "params": {
    "start": "2024-01-01",
    "end": "2024-03-31",
    "timeframe": "1H",
    "intraday_reporting": "extended_hours"
  }
}
```
