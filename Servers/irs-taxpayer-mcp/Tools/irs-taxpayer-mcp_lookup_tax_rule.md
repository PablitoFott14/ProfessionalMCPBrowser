## irs-taxpayer-mcp_lookup_tax_rule

### What this tool is for
Up IRS tax rules, definitions, and common tax questions by topic. Use this when the user needs a topic-level explanation or rule lookup rather than a numeric tax calculation.

---

### Used parameters

**(183) topic - Required**  
Default: No default  
Tax topic to look up.

---

### JSON input alternatives

```json
{
  "intent": "Look up the wash sale rule",
  "params": {
    "topic": "wash sale rule"
  }
}
```

```json
{
  "intent": "Look up stock-option and credit-related tax rules",
  "params": {
    "topic": "ISO vs NSO and AMT"
  }
}
