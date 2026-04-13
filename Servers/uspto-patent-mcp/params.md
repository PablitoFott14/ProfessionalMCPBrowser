(1) cpc_code
CPC code to look up (e.g., "G06" for computing, "G06N3/08" for neural networks).
Required. No default value.

(2) code
Status code number to look up (e.g., "30" for "Docketed New Case").
Required. No default value.

(3) query
Search query string using USPTO syntax (e.g., TTL/"neural network", IN/Smith AND AN/IBM, CPC/G06N3/08).
Required. No default value.

(4) offset
Starting position for pagination.
Optional. Default: 0.

(5) limit
Maximum number of results to return.
Optional. Default varies by tool.

(6) sort
Sort order for results.
Optional. Default: date_publ desc.

(7) guid
Document GUID (e.g., "US-9876543-B2").
Required. No default value.

(8) source_type
Document type. Accepted values: USPAT for granted patents, US-PGPUB for published applications.
Required. No default value.

(9) patent_number
Patent number.
Required or optional depending on the tool. No default value unless stated in the tool schema.

(10) app_num
Patent application number without slashes or commas (e.g., "14412875").
Required. No default value.

(11) application_number
Application number.
Optional. Default: null.

(12) inventor_name
Inventor name.
Optional. Default: null.

(13) assignee_name
Assignee or applicant name.
Optional. Default: null.

(14) filing_date_from
Filing date range start.
Optional. Default: null.

(15) filing_date_to
Filing date range end.
Optional. Default: null.

(16) product_id
Dataset product identifier.
Required. No default value.

(17) trial_type
Trial type. Accepted values: IPR, PGR, CBM, DER.
Optional. Default: null.

(18) party_name
Party name.
Optional. Default: null.

(19) status
Proceeding status. Accepted values: Pending, Instituted, Terminated, FWD Entered.
Optional. Default: null.

(20) proceeding_number
Proceeding number (e.g., "IPR2023-00001").
Required or optional depending on the tool. No default value unless stated in the tool schema.

(21) document_type
Document type.
Optional. Default: null.

(22) decision_type
Decision type. Accepted values: institution, final, termination.
Optional. Default: null.

(23) decision_date_from
Decision date range start.
Optional. Default: null.

(24) decision_date_to
Decision date range end.
Optional. Default: null.

(25) decision_id
Decision identifier.
Required. No default value.

(26) appeal_number
Appeal number.
Required. No default value.

(27) search_type
Search type. Accepted values: any, all, phrase.
Optional. Default varies by tool.

(28) patent_id
Patent ID or number.
Required. No default value.

(29) name
Name.
Required. No default value.

(30) assignee_id
Disambiguated assignee ID.
Required. No default value.

(31) inventor_id
Disambiguated inventor ID.
Required. No default value.

(32) attorney_id
Attorney ID.
Required. No default value.

(33) ipc_code
IPC code.
Required. No default value.

(34) mail_date
Mail date.
Optional. Default: null.

(35) examiner_name
Examiner name.
Optional. Default: null.

(36) art_unit
Art unit number.
Optional. Default: null.

(37) mail_date_from
Mail date range start.
Optional. Default: null.

(38) mail_date_to
Mail date range end.
Optional. Default: null.

(39) include_forward
Whether to include forward citations.
Optional. Default: true.

(40) include_backward
Whether to include backward citations.
Optional. Default: true.

(41) citing_patent
Citing patent.
Optional. Default: null.

(42) cited_patent
Cited patent.
Optional. Default: null.

(43) assignee
Assignee name.
Optional. Default: null.

(44) date_from
Date range start.
Optional. Default: null.

(45) date_to
Date range end.
Optional. Default: null.

(46) role
Role filter. Accepted values: plaintiff, defendant.
Optional. Default: null.

(47) case_id
Case identifier.
Required. No default value.

(48) plaintiff
Plaintiff name.
Optional. Default: null.

(49) defendant
Defendant name.
Optional. Default: null.

(50) court
Court or district.
Optional. Default: null.
