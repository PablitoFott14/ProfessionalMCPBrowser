## uspto-patent-mcp_ptab_get_documents

### What this tool is used for
Gets documents filed in a PTAB proceeding. Use it when you need to review petitions, responses, declarations, or other PTAB case documents.

---

### Used parameters

**(20) proceeding_number: Required**
Default: No default
Proceeding number to retrieve documents for.

**(21) document_type: Optional**
Default: null
Filters the document list by document type.

**(4) offset: Optional**
Default: 0
Starting position for pagination in this PTAB document list.

**(5) limit: Optional**
Default: 25
Maximum number of PTAB documents to return in this tool.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve documents filed in a known PTAB proceeding",
  "params": {
    "proceeding_number": "IPR2023-00001",
    "limit": 10
  }
}
```

```json
{
  "intent": "Retrieve declaration documents from a PTAB proceeding and continue to a later page",
  "params": {
    "proceeding_number": "IPR2023-00001",
    "document_type": "declaration",
    "offset": 25,
    "limit": 25
  }
}
```
