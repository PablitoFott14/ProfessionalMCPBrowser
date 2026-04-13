(1) q
Full-text search query.
Required. No default value.

(2) court
Court ID filter (e.g., "scotus", "ca9").
Optional. Default: "".

(3) case_name
Case name filter.
Optional. Default: "".

(4) judge
Judge name filter.
Optional. Default: "".

(5) filed_after
Date filter — only results filed after this date (YYYY-MM-DD).
Optional. Default: "".

(6) filed_before
Date filter — only results filed before this date (YYYY-MM-DD).
Optional. Default: "".

(7) cited_gt
Minimum citation count filter.
Optional. Default: 0.

(8) cited_lt
Maximum citation count filter.
Optional. Default: 0.

(9) order_by
Sort order for results.
Optional. Default: score desc.

(10) citation
Legal citation string to look up or analyze (e.g., "410 U.S. 113").
Required. No default value.

(11) include_courtlistener
Whether to include a CourtListener API lookup alongside local citation parsing.
Optional. Default: true.

(12) text
Block of text to process (e.g., for citation extraction).
Required. No default value.

(13) broad
Whether to use broad matching for more flexible citation parsing.
Optional. Default: true.

(14) citations
List of legal citation strings to look up. Maximum 100 items.
Required. No default value.

(15) court_id
Court identifier (e.g., "scotus", "ca9").
Required. No default value.

(16) person_id
Judge or legal professional ID in CourtListener.
Required. No default value.

(17) cluster_id
Opinion cluster ID in CourtListener.
Required. No default value.

(18) audio_id
Oral argument audio recording ID in CourtListener.
Required. No default value.

(19) docket_id
Court docket ID in CourtListener.
Required. No default value.

(20) opinion_id
Court opinion ID in CourtListener.
Required. No default value.

(21) name
Name filter for people searches.
Optional. Default: "".

(22) position_type
Position type filter (e.g., "jud" for judge).
Optional. Default: "".

(23) political_affiliation
Political affiliation filter.
Optional. Default: "".

(24) school
School attended filter.
Optional. Default: "".

(25) appointed_by
Appointing authority filter.
Optional. Default: "".

(26) selection_method
Selection method filter.
Optional. Default: "".

(27) argued_after
Date filter — only results argued after this date (YYYY-MM-DD).
Optional. Default: "".

(28) argued_before
Date filter — only results argued before this date (YYYY-MM-DD).
Optional. Default: "".

(29) docket_number
Docket number filter.
Optional. Default: "".

(30) document_number
Document number filter.
Optional. Default: "".

(31) attachment_number
Attachment number filter.
Optional. Default: "".

(32) party_name
Party name filter.
Optional. Default: "".

(33) date_filed_after
Date filter — only results with a filing date after this date (YYYY-MM-DD).
Optional. Default: "".

(34) date_filed_before
Date filter — only results with a filing date before this date (YYYY-MM-DD).
Optional. Default: "".
