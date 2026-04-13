## alpaca_exercise_options_position

### What this tool is for
A held option contract, converting it into the underlying asset position. Use this when the user wants to exercise an in-the-money option rather than selling it on the market.

---

### Used parameters

**(65) symbol_or_contract_id — Required**
Default: No default
Option contract symbol in OCC format (e.g., NVDA250919C001680) or the contract UUID.

---

### JSON input alternatives

```json
{
  "tool": "alpaca_exercise_options_position",
  "intent": "Exercise a held Nvidia call option contract",
  "params": {
    "symbol_or_contract_id": "NVDA250919C001680"
  }
}
```
