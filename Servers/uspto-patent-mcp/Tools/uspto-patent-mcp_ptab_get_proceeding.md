## uspto-patent-mcp_ptab_get_proceeding

### What this tool is used for
Gets details of a specific PTAB proceeding. Use it when you already know the proceeding number and need the proceeding details.

---

### Used parameters

**(20) proceeding_number - Required**
Default: No default
Proceeding number to look up.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve details for a known PTAB proceeding",
  "params": {
    "proceeding_number": "IPR2023-00001"
  }
}
```

```json
{
  "intent": "Look up another PTAB proceeding by its proceeding number",
  "params": {
    "proceeding_number": "PGR2024-00005"
  }
}
```
