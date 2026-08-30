# Work-native operations

This reference adapts Sol Advisor to ChatGPT Work hosted subagents.

## Work constraints

- Hosted subagents may be requested with a target model and reasoning effort when the host exposes those controls.
- Hosted agents may inherit tools and permissions from the parent Work session.
- Do not assume Codex-local `.toml` custom-agent registration, local session inspectors, or per-agent sandbox enforcement.
- Parallelize read-heavy tasks; serialize shared-state writes.
- Never claim an observed model, reasoning effort, or isolation guarantee unless the runtime exposes evidence.

## Route matrix

| Route | Typical use | Writer | Optional helpers | Review |
|---|---|---|---|---|
| solo | clear task, parent efficient | parent | none | self-review |
| delegate | bounded implementation | Luna or Terra | none | parent verification |
| parallel-read | independent research/exploration | parent/none | multiple read workers | parent synthesis |
| audit | parent implementation with elevated risk | parent | none | fresh Sol |
| full | broad/high-risk task | exactly one writer | parallel read scouts allowed | fresh Sol |

## Routing defaults

- Luna / light: mechanical, deterministic, repetitive work.
- Luna / medium: routine bounded implementation or extraction.
- Terra / medium: normal non-trivial implementation and integration.
- Terra / high: difficult debugging/refactor/integration with wider blast radius.
- Sol / high: architecture, ambiguous systems reasoning, critical decisions, fresh review.

Use the cheapest lane that preserves correctness. Escalate based on observed complexity, not prestige.

## Parallel read pattern

Good:

~~~text
Scout A: map relevant files and interfaces; read-only.
Scout B: inspect tests and likely regressions; read-only.
Scout C: research external documentation; read-only.
Parent: synthesize evidence and settle architecture.
One writer: implement the final packet.
~~~

Avoid:

~~~text
Writer A edits shared module X.
Writer B edits shared module X concurrently.
~~~

If multiple writers are necessary, assign disjoint ownership and inspect the combined state before acceptance.

## Parent verification

For every delegated result, the parent should verify as much as the current Work environment permits:

1. Inspect the actual changed files/artifacts/state.
2. Compare changed scope with declared ownership.
3. Re-run checks or equivalent validations when available.
4. Resolve worker-reported gaps and judgment calls.
5. Escalate if evidence reveals higher risk.
6. Report anything that could not be independently verified.

## Reviewer isolation

A Work reviewer is behaviorally read-only unless the host explicitly proves stronger isolation. Before review, instruct the agent not to mutate files/artifacts. After review, compare observable state when practical. If a mutation occurred, discard the verdict and verify the resulting state before proceeding.

## Failure policy

If a requested model/effort is unavailable:

- Hard-pin requested by user: stop that lane and report the limitation.
- No hard-pin requirement: continue only if an appropriate fallback exists, disclose the fallback, and preserve the route semantics.

If the worker exposes architectural ambiguity, return control to the Sol parent rather than asking the worker to redesign the system silently.
