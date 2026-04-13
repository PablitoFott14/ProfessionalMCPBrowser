## courtlistener-mcp_get_audio

### What this tool is used for
Retrieves oral argument audio information by ID from CourtListener. Use it when details or metadata about a specific oral argument recording are needed.

---

### Used parameters

**(18) audio_id: Required**
Default: No default
CourtListener oral argument audio recording ID to retrieve.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve oral argument audio information by recording ID",
  "params": {
    "audio_id": "12345"
  }
}
```

```json
{
  "intent": "Fetch metadata for a known oral argument audio recording",
  "params": {
    "audio_id": "67890"
  }
}
```
