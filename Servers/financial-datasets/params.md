(1) ticker
 Ticker symbol of the company (e.g., AAPL, GOOGL).
 Required. No default value.

(2) limit
 Number of results to return.
 Default: 10

(3) filing_type
 Type of SEC filing to filter by (e.g., 10-K, 10-Q, 8-K).
 Default: null

(4) start_date
 Start date of the data range (e.g., 2020-01-01).
 Required (when applicable). No default value.

(5) end_date
 End date of the data range (e.g., 2020-12-31).
 Required (when applicable). No default value.

(6) interval
 Interval granularity of the price data (e.g., minute, hour, day, week, month).
 Default: day

(7) interval_multiplier
 Multiplier applied to the interval (e.g., 1, 2, 3).
 Default: 1

(8) period
 Reporting period for financial statements (e.g., annual, quarterly, ttm).
 Default: annual
