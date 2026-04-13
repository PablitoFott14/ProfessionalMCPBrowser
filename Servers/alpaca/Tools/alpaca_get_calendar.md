## alpaca_get_calendar

### What this tool is for
The market calendar for a specified date range, showing trading days, market open and close times. Use this when the user needs to verify which days markets are open, plan around holidays, or determine session times for a given period.

---

### Used parameters

**(23) start_date — Required**
Default: No default
Start date of the calendar range in YYYY-MM-DD format.

**(24) end_date — Required**
Default: No default
End date of the calendar range in YYYY-MM-DD format.

---

### JSON input alternatives

```json
{
  "tool": "alpaca_get_calendar",
  "intent": "Check which days markets are open during the holiday season",
  "params": {
    "start_date": "2024-12-20",
    "end_date": "2025-01-05"
  }
}
```

```json
{
  "tool": "alpaca_get_calendar",
  "intent": "Get the full market calendar for Q1 2025",
  "params": {
    "start_date": "2025-01-01",
    "end_date": "2025-03-31"
  }
}
```
