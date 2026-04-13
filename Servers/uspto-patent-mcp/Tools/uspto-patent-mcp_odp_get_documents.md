## uspto-patent-mcp_odp_get_documents

### What this tool is used for
Gets the list of documents in a patent application file wrapper. Use it when you need to see which documents are available for an application.

---

### Used parameters

**(10) app_num - Required**
Default: No default
Application number to look up for this document-list request.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve the file wrapper document list for a known application",
  "params": {
    "app_num": "14412875"
  }
}
```

```json
{
  "intent": "Check available file wrapper documents for another application",
  "params": {
    "app_num": "16987654"
  }
}
```
