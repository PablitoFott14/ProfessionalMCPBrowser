## twelvedata_GetTechnicalIndicators

### What this tool is for
Returns an array of objects with available technical indicators. It is used when the user needs to discover which indicators are supported, explore their parameters and output values, or build an abstract interface to make more convenient API calls from the application.

---

### Used parameters

**(6) outputsize — Optional**  
Default: 10  
Number of data points to retrieve.

**(27) apikey — Optional**  
Default: demo  
API authentication key.

---

### JSON input alternatives

```json
{
  "intent": "Retrieve the full catalog of available technical indicators",
  "params": {}
}

{
  "intent": "Retrieve a limited set of technical indicator metadata",
  "params": {
    "outputsize": 50
  }
}