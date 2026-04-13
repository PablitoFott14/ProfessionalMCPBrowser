## uspto-patent-mcp_odp_get_dataset

### What this tool is used for
Gets details of a specific USPTO bulk dataset product. Use it when you need metadata for one dataset after identifying its product identifier.

---

### Used parameters

**(16) product_id: Required**
Default: No default
Dataset product identifier to look up.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve details for a specific USPTO bulk dataset product",
  "params": {
    "product_id": "PTBL2024"
  }
}
```

```json
{
  "intent": "Look up another USPTO dataset product by identifier",
  "params": {
    "product_id": "ASSIGNMENT-BULK"
  }
}
```
