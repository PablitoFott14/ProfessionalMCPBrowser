(1) prompt
 Natural language query or request used to drive the research agent.
 Required. No default value.

(2) event_ticker
 Event ticker used to identify a specific prediction market event.
 Required. No default value.

(3) limit
 Maximum number of history records to return.
 Optional. Default: null.

(4) cursor
 Pagination cursor used to continue from a previous history response.
 Optional. Default: null.

(5) captured_from
 Start of the historical time window used to filter returned records.
 Optional. Default: null.

(6) captured_to
 End of the historical time window used to filter returned records.
 Optional. Default: null.

(7) include_analysis
 Flag indicating whether analysis columns should be included in the response.
 Optional. Default: null.

(8) cache
 Flag indicating whether the agent response should be cached.
 Optional. Default: null.
