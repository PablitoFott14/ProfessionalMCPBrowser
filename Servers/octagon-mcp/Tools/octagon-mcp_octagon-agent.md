## octagon-mcp_octagon-agent

### What this tool is for
A comprehensive market intelligence agent that combines multiple data sources into a broader research analysis. Use this when the user needs a more holistic market intelligence view spanning multiple research domains across public and private markets.

---

### Used parameters

**(1) prompt: Required**  
Default: No default  
Natural language research request passed to the agent.

---

### JSON input alternatives

```json
{
  "intent": "Research a public company across filings, earnings, and ownership signals",
  "params": {
    "prompt": "Provide a comprehensive market intelligence analysis of Nvidia, including filings, earnings, financial metrics, and institutional ownership trends"
  }
}
```

```json
{
  "intent": "Research a broader market theme across public and private markets",
  "params": {
    "prompt": "Analyze the current AI infrastructure market across public companies, private funding activity, and recent M&A trends"
  }
}
```
