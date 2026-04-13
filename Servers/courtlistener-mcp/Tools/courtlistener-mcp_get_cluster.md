## courtlistener-mcp_get_cluster

### What this tool is used for
Retrieves an opinion cluster by ID from CourtListener. Use it when a cluster ID is already known and the full cluster record — including its nested opinions — is needed.

---

### Used parameters

**(17) cluster_id: Required**
Default: No default
CourtListener opinion cluster ID to retrieve.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve an opinion cluster by its CourtListener ID",
  "params": {
    "cluster_id": "108713"
  }
}
```

```json
{
  "intent": "Fetch a specific opinion cluster to access its nested opinion documents",
  "params": {
    "cluster_id": "2812209"
  }
}
```
