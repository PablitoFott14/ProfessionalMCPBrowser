## TwelveData

The TwelveData server does not follow the typical flat parameter–value structure used by many other tools. Instead, all inputs must be passed within a dedicated `params` dictionary.

### How it works
- Every tool call must include a `params` object.
- The required inputs for the request are provided as properties inside this dictionary.
- Each property comes with a default value, meaning not all parameters need to be explicitly set.

### Potential resolution paths
- **Analyze a symbol's price trend with technical confirmation:** Fetch `GetTimeSeries` for the price history, then layer in `GetRSI` or `GetMACD` over the same interval to identify momentum or divergence.
- **Get a full market snapshot before acting:** Use `GetQuote` or `GetPrice` for the current state, then pull `GetTimeSeries` with a short lookback to understand recent context without making multiple separate calls.
- **Build an intraday chart with indicators:** Call `GetTimeSeries` with a minute or hourly interval, then request `GetBollingerBands` or `GetSTOCH` over the same range to overlay signals on the price series.

### Best practices
- **Only include parameters that directly impact the user's intent.**
  Avoid passing unnecessary fields that rely on defaults, as this can introduce noise and rubric redundancy.
- **Be intentional with overrides.**
  Since defaults are already defined, only override a parameter when it meaningfully changes the outcome.
