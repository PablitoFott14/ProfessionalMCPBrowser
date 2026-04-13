## open-legal-compliance-mcp_search_state_law

### What this tool is used for
Searches state law for California, New York, or Illinois by query string. Use it when researching state-level statutory requirements or compliance obligations in one of the supported states.

---

### Used parameters

**(5) state: Required**
Default: No default
State to search within.
Allowed: ca, ny, il

**(1) query: Required**
Default: No default
Search query for state law content.

---

### JSON input alternatives

```json
{
  "intent": "Search California law for provisions on a compliance topic",
  "params": {
    "state": "ca",
    "query": "consumer privacy rights"
  }
}
```

```json
{
  "intent": "Search New York law for provisions on a business topic",
  "params": {
    "state": "ny",
    "query": "limited liability company formation"
  }
}
```
