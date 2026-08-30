# Work-native operations

This reference defines Sol Advisor Work's runtime-safe operating rules.

## Capability tiers

Run the `WORK CAPABILITY CHECK` from `SKILL.md` before relying on delegation.

| Tier | What is proven | Allowed claims |
|---|---|---|
| A | Multi-agent plus observable per-agent model routing | Exact Luna/Terra/Sol lane names; reasoning only if separately observable |
| B | Multi-agent/parallel Work execution, exact worker model not proven | Semantic roles only: mechanical-worker, implementation-worker, complex-specialist, independent-reviewer |
| C | No plugin-visible multi-agent execution | Parent-only execution; no delegation claims |

Never promote a runtime to Tier A because Work Ultra exists. Tier A requires observable controls/evidence in the current session.

## Work constraints

- Agents may inherit tools and permissions from the parent Work session.
- Do not depend on Codex-local custom-agent TOML registration, local rollout inspectors, or per-agent sandbox enforcement.
- A request for a model or reasoning level is not proof that it ran.
- Parallelize independent read-heavy work; serialize shared-state writes.
- Never claim model, effort, freshness, or isolation evidence the host did not expose.

## Route matrix

| Route | Typical use | Writer | Helpers | Review |
|---|---|---|---|---|
| solo | clear task | parent | none | parent self-review |
| delegate | bounded implementation | exactly one worker, or parent in Tier C | none | parent verification |
| parallel-read | independent research/exploration | parent/none | parallel readers in Tier A/B | parent synthesis |
| audit | elevated-risk parent implementation | parent | none | separate reviewer in A/B; disclosed second pass in C |
| full | broad/high-risk task | exactly one writer | optional read scouts | independent reviewer when A/B supports it |

## Tier A routing defaults

Only when exact routing is observable:

- Luna / light: mechanical, deterministic, repetitive work.
- Luna / medium: routine bounded implementation or extraction.
- Terra / medium: normal non-trivial implementation and integration.
- Terra / high: difficult debugging/refactor/integration with wider blast radius.
- Sol / high: architecture, ambiguous systems reasoning, critical decisions, independent review.

If exact identity becomes unavailable after spawn, reclassify that lane to Tier B and stop making exact-model claims.

## Tier B routing defaults

Use role contracts rather than model names:

- `mechanical-worker`
- `implementation-worker`
- `complex-specialist`
- `independent-reviewer`

The same scope, interface, verification, and one-writer rules apply.

## Parallel read pattern

Good:

~~~text
Scout A: map relevant files/interfaces; no writes.
Scout B: inspect tests/regressions; no writes.
Scout C: research external documentation; no writes.
Parent: synthesize evidence and settle architecture.
One writer: implement the final packet.
~~~

Avoid overlapping writers. Multiple writers are acceptable only with disjoint ownership and parent reconciliation.

## Parent verification

For every delegated result, verify as much as the current Work environment permits:

1. Inspect actual changed files/artifacts/state.
2. Compare changed scope with declared ownership.
3. Re-run checks or equivalent validations when available.
4. Resolve worker-reported gaps and judgment calls.
5. Escalate if evidence reveals higher risk.
6. Report anything that could not be independently verified.

## Reviewer isolation

A Work reviewer is behaviorally read-only unless the host explicitly proves stronger isolation. Instruct the reviewer not to mutate state and compare observable before/after state when practical. If mutation occurs, discard the verdict.

In Tier B never call the reviewer "Fresh Sol". In Tier C never call a self-audit independent.

## Failure policy

If a requested capability/model/effort is unavailable:

- If the user required a hard guarantee, stop that lane and report the limitation.
- Otherwise downgrade the capability tier, preserve safety semantics, and disclose the fallback.

If a worker exposes architectural ambiguity, return control to the parent or complex-specialist path rather than allowing silent redesign.
