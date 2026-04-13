## alphavantage

The `alphavantage` server is a schema-driven gateway for discovering, inspecting, and executing Alpha Vantage tools. It is useful when the user needs to explore what Alpha Vantage capabilities are available first, understand the required parameters for a specific tool, and then make the call in a structured way.

### How it works
- The server follows a three-step interaction flow: list available tools, retrieve the full schema for the relevant tool, then execute it with the proper arguments.
- It does not expose domain-specific endpoints directly in this layer; instead, it provides a controlled way to navigate and call the underlying Alpha Vantage tool set.
- Requests stay generic at the wrapper level, using `tool_name` to identify the target tool and `arguments` to pass the tool-specific inputs.

### Potential resolution paths
- **Explore before choosing a tool:** Start with `TOOL_LIST` to see the available Alpha Vantage tool catalog, then use `TOOL_GET` on the most relevant options before deciding which one to call.
- **Clarify schema before execution:** If the user already has a likely target such as a time series tool, use `TOOL_GET` to inspect the exact parameter structure, then move into `TOOL_CALL` with only the arguments that match that schema.
- **Compare multiple candidate tools before calling one:** Use `TOOL_GET` with a list of tool names when the correct endpoint is uncertain, compare their schemas, and then send the final request through `TOOL_CALL`.

### Best practices
- **Do not skip the schema step when the target tool is unfamiliar:** `TOOL_GET` reduces avoidable mistakes by confirming the exact input shape before execution.
- **Use discovery progressively:** Start broad with `TOOL_LIST`, narrow with `TOOL_GET`, and only then move into `TOOL_CALL` once the correct Alpha Vantage endpoint is clear.
