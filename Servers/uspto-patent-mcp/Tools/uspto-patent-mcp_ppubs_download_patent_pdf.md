## uspto-patent-mcp_ppubs_download_patent_pdf

### What this tool is used for
Downloads the official USPTO PDF for a granted patent by patent number. Use it when the PDF version is needed instead of the text document.

---

### Used parameters

**(9) patent_number — Required**
Default: No default
Granted patent number to download as a PDF.

---

### JSON input alternatives

```json
{
  "intent": "Download the official PDF for a granted patent",
  "params": {
    "patent_number": "7123456"
  }
}
```

```json
{
  "intent": "Download the official PDF for another granted patent",
  "params": {
    "patent_number": "11500000"
  }
}
```
