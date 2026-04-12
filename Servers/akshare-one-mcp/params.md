(1) symbol
 Stock symbol or ticker to retrieve historical data for (e.g., 000001).
 Required. No default value.

(2) interval
 Time interval of the historical series (minute, hour, day, week, month, year).
 Optional. Default: day.

(3) interval_multiplier
 Multiplier applied to the chosen interval.
 Optional. Default: 1.

(4) start_date
 Start date of the requested history in YYYY-MM-DD format.
 Optional. Default: 1970-01-01.

(5) end_date
 End date of the requested history in YYYY-MM-DD format.
 Optional. Default: 2030-12-31.

(6) adjust
 Adjustment mode for the price series.
 Optional. Default: none.

(7) source
 Market data source used to fetch the history.
 Optional. Default: eastmoney.

(8) indicators_list
 Technical indicators to calculate and add to the returned historical data.
 Optional. Default: null.

(9) recent_n
 Number of most recent records to return.
 Optional. Default: 100.
