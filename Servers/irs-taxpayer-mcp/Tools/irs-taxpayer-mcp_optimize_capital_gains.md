## irs-taxpayer-mcp_optimize_capital_gains

### What this tool is for
Analyzes investment lots and suggests which positions to sell to reduce tax impact. Use this when the user wants to compare lot-level sale choices around long-term versus short-term treatment, gain realization, or loss harvesting.

---

### Used parameters

**(1) taxYear - Required**  
Default: No default  
Tax year used for the optimization analysis.

**(2) filingStatus - Required**  
Default: No default  
Allowed: single, married_filing_jointly, married_filing_separately, head_of_household, qualifying_surviving_spouse  
Filing status used for the optimization analysis.

**(155) ordinaryIncome - Required**  
Default: No default  
Ordinary income before investment sales.

**(156) lots - Required**  
Default: No default  
Array of investment lots to analyze.

**(157) name - Required**  
Default: No default  
Investment name within a lot entry.

**(158) shares - Required**  
Default: No default  
Number of shares within a lot entry.

**(159) costBasis - Required**  
Default: No default  
Total cost basis within a lot entry.

**(160) currentValue - Required**  
Default: No default  
Current market value within a lot entry.

**(161) holdingMonths - Required**  
Default: No default  
Number of months the lot has been held.

**(162) targetGainOrLoss - Optional**  
Default: No default  
Target net gain or loss to realize.

---

### JSON input alternatives

```json
{
  "tool": "irs-taxpayer-mcp_optimize_capital_gains",
  "intent": "Identify which lots to sell to realize losses for tax-loss harvesting",
  "params": {
    "taxYear": 2025,
    "filingStatus": "single",
    "ordinaryIncome": 98000,
    "targetGainOrLoss": -5000,
    "lots": [
      {
        "name": "AAPL",
        "shares": 40,
        "costBasis": 9800,
        "currentValue": 8400,
        "holdingMonths": 18
      },
      {
        "name": "ARKK",
        "shares": 25,
        "costBasis": 3200,
        "currentValue": 2100,
        "holdingMonths": 9
      }
    ]
  }
}
```

```json
{
  "tool": "irs-taxpayer-mcp_optimize_capital_gains",
  "intent": "Review lots for a joint filer trying to realize gains efficiently",
  "params": {
    "taxYear": 2025,
    "filingStatus": "married_filing_jointly",
    "ordinaryIncome": 110000,
    "targetGainOrLoss": 12000,
    "lots": [
      {
        "name": "VTI",
        "shares": 120,
        "costBasis": 24000,
        "currentValue": 33600,
        "holdingMonths": 36
      },
      {
        "name": "NVDA",
        "shares": 15,
        "costBasis": 6200,
        "currentValue": 9100,
        "holdingMonths": 7
      }
    ]
  }
}
