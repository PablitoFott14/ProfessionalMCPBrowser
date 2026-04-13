## uspto-patent-mcp_ppubs_get_full_document

### What this tool is used for
Retrieves a full patent document from USPTO Patent Public Search by GUID. Use it when a search result already provides the GUID and you need the complete document.

---

### Used parameters

**(7) guid: Required**
Default: No default
Document GUID for the patent or published application to retrieve.

**(8) source_type: Required**
Default: No default
Allowed: USPAT, US-PGPUB
Selects whether the GUID belongs to a granted patent (`USPAT`) or a published application (`US-PGPUB`).

---

### JSON input alternatives

```json
{
  "intent": "Retrieve the full document for a granted patent from its GUID",
  "params": {
    "guid": "US-9876543-B2",
    "source_type": "USPAT"
  }
}
```

```json
{
  "intent": "Retrieve the full document for a published application from its GUID",
  "params": {
    "guid": "US-20220123456-A1",
    "source_type": "US-PGPUB"
  }
}
```
