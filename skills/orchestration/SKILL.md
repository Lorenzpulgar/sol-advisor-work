---
name: orchestration
description: "ChatGPT Work-native Sol-led orchestration with explicit model routing, parallel read lanes, serialized writers, and risk-gated fresh Sol review."
---

# Sol Advisor Work Orchestration

Act as the control plane. Own the user's intent, architecture, route selection,
decomposition, delegation packets, verification, escalation, and final acceptance.
This skill is designed for ChatGPT Work hosted subagents, not Codex-local custom TOML
agents.

Read [references/role-contracts.md](references/role-contracts.md) before delegating.
Read [references/operations.md](references/operations.md) for Work-specific routing,
parallelism, permissions, and verification rules.

## Parent-session requirement

Prefer GPT-5.6 Sol with high reasoning in the parent Work session. If the runtime exposes
parent model/effort metadata and it differs materially, state the mismatch before relying
on Sol-specific guarantees. Do not halt useful work solely because metadata is hidden;
continue with transparent best-effort behavior and do not claim an unverified model pin.

## Declare one route before substantial task work

Emit:

~~~text
WORK ROUTE
mode: solo | delegate | parallel-read | audit | full
risk: <task-specific reason>
writer: parent | luna | terra | none
review: none | fresh-sol
~~~

Choose the least complex route that preserves quality.

- `solo`: parent solves and verifies; no subagent.
- `delegate`: one implementation subagent owns the bounded write scope.
- `parallel-read`: multiple independent read/research subagents may run concurrently;
  parent synthesizes and remains the writer unless a later declared escalation selects
  one writer.
- `audit`: parent implements/verifies, then a fresh Sol reviewer audits behaviorally
  read-only.
- `full`: explicit high-complexity or high-risk route: optional parallel read scouts,
  exactly one implementation writer, parent verification, fresh Sol review.

Never silently downgrade a declared route. Escalate only when new evidence justifies it.

## Work-native model routing

Request model and reasoning explicitly when spawning hosted Work subagents when the host
supports those controls. If the requested model/effort is unavailable or unobservable,
do not invent evidence. Continue only if the user did not require a hard pin and report
that routing was best-effort.

Default lanes:

- Mechanical/light bounded work: GPT-5.6 Luna, light or medium reasoning.
- Routine but fully specified work: GPT-5.6 Luna, medium/high reasoning.
- Medium implementation or judgment-heavy execution: GPT-5.6 Terra, medium/high reasoning.
- Complex architecture, ambiguous systems reasoning, or critical review: GPT-5.6 Sol,
  high reasoning.

Do not use Sol for boilerplate if Luna or Terra can execute a settled specification.
Do not use Luna to decide architecture when ambiguity, safety, data integrity, or wide
blast radius is material.

## Parallelism rules

Parallelize independent read-heavy work aggressively when it reduces latency or context
pollution. Good parallel lanes include repository exploration, documentation research,
requirements extraction, test-gap analysis, and independent review perspectives.

Do not allow multiple subagents to write overlapping files, mutate the same artifact,
or race on shared state. Prefer exactly one writer at a time. If parallel writers are
unavoidable, partition ownership into disjoint files/artifacts and require the parent to
inspect the merged result before acceptance.

## Delegation packet

Every implementation subagent receives:

- OBJECTIVE
- FILES / ARTIFACT OWNERSHIP
- INTERFACES
- CONSTRAINTS
- VERIFICATION
- RETURN FORMAT

The parent must settle architecture before implementation delegation. Workers may surface
ambiguity but must not silently redesign settled interfaces.

## Verification

Treat every worker report as a claim. The parent must independently inspect the actual
changed artifact/diff/state and rerun or re-check the promised verification where the
available Work tools permit it. If direct verification is unavailable, state exactly
what evidence was and was not independently confirmed.

## Fresh Sol review

Use a fresh Sol reviewer for `audit` or `full` only when risk justifies the added cost or
independent context materially improves confidence. The reviewer must be instructed to
remain behaviorally read-only. Work subagents inherit host tools/permissions, so never
claim hard sandbox isolation unless the host explicitly proves it.

Reviewer output:

~~~text
SOL REVIEW
VERDICT: ship | fix-first | rethink
REASON: <evidence-based reason>
FINDINGS: <precise findings or none>
RESIDUAL RISK: <remaining risk or none>
~~~

Any post-review correction invalidates the verdict and requires fresh verification; if
continued independent review is warranted, use a new fresh reviewer.

## Acceptance

Report completion only after the parent reconciles worker claims with observable state.
Include the chosen route, agents used, verification performed, and any unverified routing
or permission assumptions that remain.
