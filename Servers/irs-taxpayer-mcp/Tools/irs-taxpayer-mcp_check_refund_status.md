## irs-taxpayer-mcp_check_refund_status

### What this tool is for
Provides instructions for checking IRS refund status, including the official path and required information. Use this when the user needs guidance on how to check refund status rather than account access or direct refund data.

---

### Used parameters

**(34) filedElectronically - Optional**  
Default: No default  
Flag indicating whether the return was e-filed.

---

### JSON input alternatives

```json
{
  "tool": "irs-taxpayer-mcp_check_refund_status",
  "intent": "Get refund status instructions for an electronically filed return",
  "params": {
    "filedElectronically": true
  }
}
```

```json
{
  "tool": "irs-taxpayer-mcp_check_refund_status",
  "intent": "Get general IRS refund status instructions",
  "params": {}
}
```
