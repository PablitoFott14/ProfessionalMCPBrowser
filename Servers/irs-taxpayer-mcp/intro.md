## irs-taxpayer-mcp

The irs-taxpayer-mcp server covers the full range of US federal and state tax workflows: calculating liability, comparing filing options, planning deductions and credits, estimating withholding and quarterly payments, assessing audit risk, and projecting taxes across multiple years. It is the server to use when the goal is not just to look up a tax rule, but to apply it to a specific taxpayer situation and produce an actionable result.

### How it works

- The server spans both reference and computation: some tools return reference data such as brackets, deadlines, forms, and rules, while others perform calculations or comparisons based on the taxpayer's specific income, filing status, deductions, and credits.
- Most tools are self-contained and accept the taxpayer's situation directly as input, so they can be used in isolation or chained together to build a progressively fuller tax picture.
- The server covers federal taxes, state taxes, self-employment, retirement, capital gains, 1099 income, and education benefits, making it broadly applicable across different taxpayer profiles without switching servers.

### Potential resolution paths

- **Move from a broad tax estimate to a complete picture:** Start with `calculate_federal_tax` or `calculate_total_tax` for an initial liability estimate, then add `standard_vs_itemized`, `check_credit_eligibility`, and `list_deductions` to refine deductions and credits before calling `generate_full_tax_report` for a consolidated summary.
- **Assess withholding and adjust accordingly:** Use `analyze_paycheck` to check whether current withholding is accurate, then call `calculate_w4_withholding` to get revised W-4 settings, and `estimate_quarterly_tax` if additional estimated payments are needed.
- **Run a filing-status or state-level comparison before committing:** Use `compare_filing_statuses` or `compare_mfj_vs_mfs` to find the most favorable federal status, `compare_state_taxes` or `analyze_relocation_taxes` to evaluate state-level impact, and `estimate_state_tax` or `get_state_tax_info` for a deeper look at a specific state.
- **Build a multi-year or retirement-focused tax plan:** Combine `plan_multi_year_taxes`, `get_retirement_strategy`, `plan_retirement_withdrawals`, and `optimize_capital_gains` to project and optimize tax exposure across a longer horizon.
- **Prepare for filing from scratch:** Use `get_tax_document_checklist` to identify what documents are needed, `get_tax_deadlines` to confirm relevant dates, `get_irs_form_info` or `get_form_filing_guide` for form-level guidance, and `run_tax_health_check` to surface risks before submitting.

### Best practices

- **Start with reference tools when the taxpayer situation is not fully defined:** Tools such as `get_tax_brackets`, `list_deductions`, `list_tax_credits`, and `lookup_tax_rule` provide the grounding needed before moving into calculation or planning tools that require specific inputs.
- **Use computation tools in sequence rather than in isolation:** The server produces the most useful results when tools are layered — for example, running a liability estimate first, then refining it with deduction and credit tools, and only then generating a report or multi-year projection.
