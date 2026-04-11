(1) symbol
 Ticker symbol of the instrument (e.g., AAPL, EUR/USD, ETH/BTC).
 Required. No default value.

(2) isin
 International Securities Identification Number used to uniquely identify a financial instrument.
 Default: null

(3) figi
 Financial Instrument Global Identifier.
 Default: null

(4) cusip
 CUSIP identifier for financial instruments (primarily US-based).
 Default: null

(5) interval
 Time interval between data points (e.g., 1min, 1h, 1day).
 Default: 1day

(6) outputsize
 Number of data points to retrieve (range: 1–5000).
 Default: 10 (or max when date filters are used)

(7) exchange
 Exchange where the instrument is traded.
 Default: null

(8) mic_code
 Market Identifier Code (ISO 10383).
 Default: null

(9) country
 Country where the instrument is traded.
 Default: null

(10) type
 Asset class of the instrument (e.g., ETF, stock, crypto).
 Default: null

(11) timezone
 Timezone used for output timestamps.
 Default: Exchange

(12) start_date
 Start date and time for the data range.
 Default: null

(13) end_date
 End date and time for the data range.
 Default: null

(14) date
 Specific date to retrieve data for.
 Default: null

(15) order
 Sorting order of the output (asc or desc).
 Default: desc

(16) prepost
 Include pre-market and post-market data.
 Default: false

(17) format
 Response format (JSON or CSV).
 Default: JSON

(18) delimiter
 Separator used in CSV responses.
 Default: ;

(19) dp
 Number of decimal places for numeric values (0–11).
 Default: -1 (auto-determined)

(20) previous_close
 Include previous closing price in the response.
 Default: false

(21) adjust
 Price adjustment mode (all, splits, dividends, none).
 Default: splits

(22) series_type
 Price type used for calculations.
 Default: close

(23) fast_period
 Periods for fast moving average.
 Default: 12

(24) slow_period
 Periods for slow moving average.
 Default: 26

(25) signal_period
 Periods for signal line calculation.
 Default: 9

(26) include_ohlc
 Include OHLC values in the response.
 Default: false

(27) apikey
 API key for authentication.
 Default: demo

(28) volume_time_period
 Number of periods used to calculate average volume.
 Default: 9

(29) eod
 Boolean flag indicating whether the tool should return data for the closed day.
 Default: false

(30) rolling_period
 Number of hours used to calculate rolling period change. The schema states it can range from 1 to 168.
 Default: 24

(31) time_period
 Number of periods used for the moving average.
 Default: 20

(32) sd
 Number of standard deviations used to calculate the bands.
 Default: 2

(33) ma_type
 Type of moving average used (e.g., SMA, EMA).
 Default: SMA

(34) figi
 Financial Instrument Global Identifier used to uniquely identify the asset.
 Default: null

(35) isin
 International Securities Identification Number of the instrument.
 Default: null

(36) cusip
 CUSIP identifier for the instrument.
 Default: null

(37) exchange
 Exchange where the instrument is traded.
 Default: null

(38) mic_code
 Market Identifier Code following ISO 10383 standard.
 Default: null

(39) country
 Country where the instrument is traded.
 Default: null

(40) code
Market Identifier Code (MIC) of the exchange.
Default: null

(41) show_plan
Includes information about plan availability for each symbol.
Default: false

(42) type
 Asset class of the instrument (e.g., ETF, Common Stock, Digital Currency).
 Default: null

(43) prepost
 Includes pre and post market data for supported intervals.
 Default: false

(44) previous_close
 Includes previous closing price in the response.
 Default: false

(45) adjust
 Adjustment mode for price data.
 Default: splits

(46) currency_base
 Filters results by base currency.
 Default: null

(47) currency_quote
 Filters results by quote currency.
 Default: null

(48) range
Time range for dividend data (e.g., 1y, 5y, full). Takes precedence over dates.
Default: last

(49) period
Specifies type of earnings to retrieve (e.g., latest, next). Overrides dates and outputsize.
Default: null

(50) amount
Amount of base currency to convert into the quote currency.
Default: No default

(51) name
Filters results by exchange name.
Default: null

(52) include_delisted
Includes delisted ETF identifiers in the results.
Default: false

(53) category
Filters commodities by category (e.g., Precious Metal, Energy).
Default: null

(54) page
Page number of the results to fetch.
Default: 1

(55) base
 Base instrument or currency.
 Default: No default

(56) quote
 Quote instrument or currency.
 Default: No default

(57) base_type
 Type of the base instrument.
 Default: null

(58) base_exchange
 Exchange of the base instrument.
 Default: null

(59) base_mic_code
 MIC code of the base instrument.
 Default: null

(60) quote_type
 Type of the quote instrument.
 Default: null

(61) quote_exchange
 Exchange of the quote instrument.
 Default: null

(62) quote_mic_code
 MIC code of the quote instrument.
 Default: null
