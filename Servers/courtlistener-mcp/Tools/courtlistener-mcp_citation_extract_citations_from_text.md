## courtlistener-mcp_citation_extract_citations_from_text

### What this tool is used for
Extracts and parses all legal citations from a block of text using citeurl. Use it when processing a document, brief, or opinion to identify every citation it contains, including both long-form and short-form references such as "id." citations.

---

### Used parameters

**(12) text: Required**
Default: No default
Block of text containing the legal citations to extract.

---

### JSON input alternatives

```json
{
  "intent": "Extract all citations from a legal document or opinion text",
  "params": {
    "text": "The Court held in Brown v. Board of Education, 347 U.S. 483 (1954), that segregation was unconstitutional. Id. at 495."
  }
}
```

```json
{
  "intent": "Extract citations from a brief to identify all cited authorities",
  "params": {
    "text": "As established in Miranda v. Arizona, 384 U.S. 436 (1966), and reaffirmed in Dickerson v. United States, 530 U.S. 428 (2000), the warnings are constitutionally required."
  }
}
```
