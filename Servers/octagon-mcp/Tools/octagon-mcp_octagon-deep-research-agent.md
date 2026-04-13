## octagon-mcp_octagon-deep-research-agent

### What this tool is for
A deep research agent that aggregates and synthesizes investment research across multiple sources. Use this when the user needs a broad, up-to-date research answer rather than a narrow lookup from a single data source.

---

### Used parameters

**(1) prompt - Required**  
Default: No default  
Natural language research request passed to the agent.

---

### JSON input alternatives

```json
{
  "tool": "octagon-mcp_octagon-deep-research-agent",
  "intent": "Research the current investment case for semiconductor stocks",
  "params": {
    "prompt": "Provide a deep investment research overview of the current semiconductor sector outlook"
  }
}
```

```json
{
  "tool": "octagon-mcp_octagon-deep-research-agent",
  "intent": "Research a company with a focus on risks and catalysts",
  "params": {
    "prompt": "Analyze the current investment thesis for Tesla, including key risks and near-term catalysts"
  }
}
```
