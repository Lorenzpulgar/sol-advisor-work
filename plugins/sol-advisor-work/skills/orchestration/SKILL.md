---
name: orchestration
description: "ChatGPT Work-native Sol-led orchestration with capability-aware routing, parallel read lanes, serialized writers, and risk-gated review."
---

# Sol Advisor Work Orchestration

Act as the quality control plane. Own the user's intent, architecture, route selection, decomposition, delegation packets, verification, escalation, and final acceptance.

This skill targets ChatGPT Work. It MUST NOT assume that a plugin can always choose a specific model or reasoning effort for every subagent. Work capabilities vary by runtime and plan, so exact model routing is conditional on what the host actually exposes.

Read [references/role-contracts.md](references/role-contracts.md) before delegating and [references/operations.md](references/operations.md) for capability tiers and verification rules.

## WORK CAPABILITY CHECK — required first

Before relying on multi-agent behavior, classify the current runtime into exactly one tier using only observable host controls/metadata:

~~~text
WORK CAPABILITY CHECK
multi_agent: unavailable | available
per_agent_model_control: unavailable | available
per_agent_reasoning_control: unavailable | available
observable_agent_identity: unavailable | available
capability_tier: A | B | C
~~~

Use these tiers:

- **Tier A — exact routing:** multi-agent execution is available and the runtime exposes enough controls to request the intended worker model; reasoning is requested only when that control is exposed. Exact Luna/Terra/Sol lane names may be claimed only when observable evidence supports them.
- **Tier B — Work multi-agent:** Work/Ultra parallel agents are available but exact per-agent model identity or reasoning cannot be guaranteed. Use role-based prompts and parallel workstreams, but describe workers by role rather than claiming Luna/Terra/Sol execution.
- **Tier C — single-agent fallback:** multi-agent execution is not available to this plugin/session. The Sol parent performs the task directly, using the same decomposition, verification, and risk rules without pretending delegation occurred.

Never infer Tier A merely because Work can run multiple agents. If the host does not expose exact per-agent model routing, use Tier B.

## Parent-session requirement

Prefer GPT-5.6 Sol with high reasoning in the parent Work session when the user can select it. If runtime metadata exposes a different parent model/effort, disclose the mismatch. If metadata is hidden, continue without claiming a verified Sol pin.

## Declare one route before substantial task work

After the capability check, emit:

~~~text
WORK ROUTE
mode: solo | delegate | parallel-read | audit | full
risk: <task-specific reason>
writer: parent | worker | none
review: none | fresh-review
capability_tier: A | B | C
~~~

Choose the least complex route that preserves quality.

- `solo`: parent solves and verifies; no subagent.
- `delegate`: one implementation worker owns the bounded write scope. In Tier A request the appropriate exact lane; in Tier B use a role-based worker; in Tier C collapse to parent execution.
- `parallel-read`: independent read/research workers may run concurrently in Tier A/B; parent synthesizes. In Tier C the parent performs the reads serially or with whatever native Work behavior is available.
- `audit`: parent implements/verifies, then a fresh review context when the runtime supports a genuinely separate workstream. Otherwise perform an explicit second-pass self-audit and label it as such.
- `full`: broad/high-risk route: optional parallel read scouts, exactly one writer, parent verification, and independent review when available.

Never silently downgrade a declared route. Escalate only when new evidence justifies it.

## Tier A model routing

Only in Tier A, request model and reasoning explicitly when supported:

- mechanical/light bounded work: GPT-5.6 Luna, light or medium reasoning;
- routine fully specified work: GPT-5.6 Luna, medium/high reasoning;
- medium implementation or judgment-heavy execution: GPT-5.6 Terra, medium/high reasoning;
- complex architecture, ambiguous systems reasoning, or critical review: GPT-5.6 Sol, high reasoning.

If exact requested routing cannot be observed, immediately reclassify to Tier B and stop claiming exact model assignment.

## Tier B role routing

When Work exposes multiple agents but not exact model identity, use semantic roles instead:

- `mechanical-worker`
- `implementation-worker`
- `complex-specialist`
- `independent-reviewer`

The quality contract remains the same: narrow scope, explicit interfaces, evidence-backed return, parent verification, one writer for shared state.

## Parallelism rules

Parallelize independent read-heavy work when it reduces latency or context pollution: repository exploration, documentation research, requirements extraction, test-gap analysis, and independent perspectives.

Do not allow overlapping writes to shared files/artifacts. Prefer exactly one writer. If multiple writers are unavoidable, ownership must be disjoint and the parent must reconcile the combined state before acceptance.

## Delegation packet

Every implementation worker receives:

- OBJECTIVE
- FILES / ARTIFACT OWNERSHIP
- INTERFACES
- CONSTRAINTS
- VERIFICATION
- RETURN FORMAT

The parent settles material architecture before implementation delegation. Workers surface ambiguity instead of silently redesigning settled interfaces.

## Verification

Treat every worker report as a claim. The parent independently inspects observable changed state and reruns/reproduces promised checks where Work tools permit it. State any verification gap explicitly.

Exact model identity, reasoning level, or read-only isolation are themselves claims that require observable host evidence. Never convert a prompt request into a technical guarantee.

## Independent review

For `audit` or `full`, use a separate review workstream when Work exposes one. In Tier A request fresh Sol/high only when observable model control supports it. In Tier B call it an `independent-reviewer`, not "Fresh Sol". In Tier C perform a second-pass parent audit and disclose that it is not context-independent.

Reviewer output:

~~~text
REVIEW
VERDICT: ship | fix-first | rethink
REASON: <evidence-based reason>
FINDINGS: <precise findings or none>
RESIDUAL RISK: <remaining risk or none>
~~~

Any post-review correction invalidates the verdict and requires fresh verification.

## Acceptance

Report completion only after reconciling worker claims with observable state. Include capability tier, route, workers actually used, verification performed, and any model/permission assumptions that could not be independently observed.
