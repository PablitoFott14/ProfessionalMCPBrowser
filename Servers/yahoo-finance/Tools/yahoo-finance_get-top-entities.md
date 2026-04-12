## yahoo-finance_get-top-entities

### What this tool is for
Gets top entities in a sector, including ETFs, mutual funds, companies, growth companies, or performing companies. Use this when the user wants a sector-level view of leading instruments or organizations rather than a single ticker lookup.

---

### Used parameters

**(4) entity_type — Required**  
Default: No default  
Type of entities to retrieve.

**(5) sector — Optional**  
Default: ""  
Sector name used to filter the returned entities.

**(2) count — Optional**  
Default: 10  
Number of entities to return.

---

### JSON input alternatives

```json
{
  "intent": "Get top ETFs in the technology sector",
  "params": {
    "entity_type": "etfs",
    "sector": "technology"
  }
}
```

```json
{
  "intent": "Retrieve more top performing companies in healthcare",
  "params": {
    "entity_type": "performing_companies",
    "sector": "healthcare",
    "count": 15
  }
}
```
