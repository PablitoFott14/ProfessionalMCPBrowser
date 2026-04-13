## twelvedata_GetApiUsage

### What this tool is for
Returns real-time information about API usage, including current request rate and plan limits. It is used to monitor consumption, avoid rate limits, and manage API usage efficiently in production or testing environments.

---

### Used parameters

**(17) format — Optional**  
Default: JSON  
Allowed: JSON, CSV  
Output format.

**(18) delimiter — Optional**  
Default: ;  
Separator used for CSV output.

**(11) timezone — Optional**  
Default: null  
Timezone used for the returned timestamp.

**(6) outputsize — Optional**  
Default: null  
Number of data points to retrieve.

**(27) apikey — Optional**  
Default: demo  
API authentication key.

---

### JSON input alternatives

```json
{
  "tool": "twelvedata_GetApiUsage",
  "intent": "Check current API usage status",
  "params": {}
}

{
  "tool": "twelvedata_GetApiUsage",
  "intent": "Retrieve usage data with specific timezone context",
  "params": {
    "timezone": "America/New_York"
  }
}