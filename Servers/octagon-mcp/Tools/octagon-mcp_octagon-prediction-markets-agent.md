## octagon-mcp_octagon-prediction-markets-agent

### What this tool is for
A specialized prediction markets research agent for Kalshi events. Use this when the user needs a focused research report on what may be driving a market, how market and model probabilities compare, or where potential mispricings may exist.

---

### Used parameters

**(1) prompt - Required**  
Default: No default  
Natural language research request passed to the agent.

**(8) cache - Optional**  
Default: null  
Flag indicating whether the response should be cached.

---

### JSON input alternatives

```json
{
  "tool": "octagon-mcp_octagon-prediction-markets-agent",
  "intent": "Research what is driving a specific Kalshi event",
  "params": {
    "prompt": "Create a research report on the current drivers of the BTC end-of-month Kalshi market"
  }
}
```

```json
{
  "tool": "octagon-mcp_octagon-prediction-markets-agent",
  "intent": "Analyze a Kalshi event for potential mispricing and cache the response",
  "params": {
    "prompt": "Compare market-implied and model-implied probabilities for this Kalshi election event and identify possible mispricings",
    "cache": true
  }
}
```
