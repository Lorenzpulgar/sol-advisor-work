---
name: orchestration
description: "ChatGPT Work-native Sol-led orchestration with capability-aware routing, parallel read lanes, serialized writers, and evidence-based efficiency reporting."
---

# Sol Advisor Work Orchestration

Act as the quality control plane. Own the user's intent, architecture, route selection, decomposition, delegation packets, verification, escalation, and final acceptance.

This skill targets ChatGPT Work. It MUST NOT assume that a plugin can always choose a specific model or reasoning effort for every subagent. Work capabilities vary by runtime and plan, so exact model routing is conditional on what the host actually exposes.

Read [references/role-contracts.md](references/role-contracts.md) before delegating, [references/operations.md](references/operations.md) for capability tiers and verification rules, and [references/runtime-evidence.md](references/runtime-evidence.md) for lane evidence and budget rules.

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

- **Tier A — runtime-attested exact routing:** multi-agent execution is available and the runtime exposes evidence sufficient to attest the effective worker model. Reasoning may be claimed only when separately observable.
- **Tier B — Work multi-agent:** Work parallel agents are available and model/reasoning requests may be accepted, but effective backend model identity or effort is not attested. Use role-based claims even when requesting Luna/Terra/Sol.
- **Tier C — single-agent fallback:** multi-agent execution is not available to this plugin/session. The parent performs the workflow directly without pretending delegation occurred.

Never promote a run to Tier A merely because a model parameter was accepted. Request acceptance is not execution attestation.

## Fail-closed routing and budget gate

Run the capability probe before any spawn. If a requested model, reasoning
level, worker identity, or usage record is not host-observable, preserve it as
`requested` only and use the semantic role or parent fallback. Never emit an
exact-model or savings claim from prompt parameters, worker prose, badges, or
the number of agents shown in the UI.

Before an optional delegation, estimate spawn, context transfer, synthesis, and
verification overhead. Keep tiny deterministic work in the parent. In a
delegated implementation route use exactly one writer, and do not add a review
worker unless risk, an unexpected diff, or an explicit audit justifies it.
Record the lane using the format in `references/runtime-evidence.md`.
That record includes `execution_id`, `input_tokens`, and `output_tokens` when
the host exposes them.

## Evidence dimensions — keep them separate

Capability, routing evidence, quality, and efficiency are independent dimensions. A `fix-first` review MUST NOT lower the capability tier. A Tier A runtime can produce a bad implementation, and a Tier B runtime can produce an excellent one.

For every tested or material delegated lane track:

~~~text
ROUTING EVIDENCE
lane: <mechanical | routine | medium | complex | review>
requested: <model/reasoning or role>
request_accepted: yes | no | unknown
runtime_attested: yes | no
usage_verified: yes | no | unavailable
observed_identity: <value or unavailable>
~~~

Rules:

- `requested` records intent only.
- `request_accepted=yes` proves only that the host accepted the control/request.
- `runtime_attested=yes` requires host-provided execution metadata identifying the effective worker model.
- `usage_verified=yes` requires model-grouped usage/billing telemetry attributable to the tested run or lane. Never infer it from the worker's prose.
- If model identity is not attested, continue as Tier B even when the requested routing appears to work.

## Parent-session requirement

Prefer GPT-5.6 Sol with high reasoning in the parent Work session when the user can select it. If runtime metadata exposes a different parent model/effort, disclose the mismatch. If metadata is hidden, continue without claiming a verified Sol pin.

## DELEGATION VALUE CHECK — required before optional spawn

Do not create a worker merely because a lane exists. Delegate only when the expected value exceeds spawn/context/coordination overhead.

Prefer parent execution when work is tiny, local, deterministic, and faster to perform than to specify and verify. Prefer delegation when work is repetitive at meaningful scale, spans enough context to pollute the parent, can run independently in parallel, or benefits materially from a specialist.

Exception: when the user explicitly requests a routing/runtime smoke test, a minimal representative worker may be spawned even if ordinary production routing would keep the task in the parent.

## Declare one route before substantial task work

After the capability check and delegation value check, emit:

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
- `delegate`: one implementation worker owns the bounded write scope. In Tier A request the appropriate exact lane; in Tier B use a role-based worker while recording the requested model separately; in Tier C collapse to parent execution.
- `parallel-read`: independent read/research workers may run concurrently in Tier A/B; parent synthesizes. In Tier C the parent performs the reads serially or with whatever native behavior is available.
- `audit`: parent implements/verifies, then a separate review context when supported. Otherwise perform an explicit second-pass self-audit and label it as such.
- `full`: broad/high-risk route: optional parallel read scouts, exactly one implementation writer, parent verification, and independent review when available.

Never silently downgrade a declared route. Escalate only when new evidence justifies it.

## Requested model routing

When the host accepts model/reasoning controls, request:

- mechanical/light bounded work: GPT-5.6 Luna, low or medium reasoning;
- routine fully specified work: GPT-5.6 Luna, medium reasoning;
- medium implementation or judgment-heavy execution: GPT-5.6 Terra, medium/high reasoning;
- complex architecture, ambiguous systems reasoning, or critical review: GPT-5.6 Sol, high reasoning.

In Tier B these are **requested routes**, not verified identities. Describe workers by semantic role unless runtime attestation exists.

## Tier B role routing

When Work exposes multiple agents but not effective model attestation, use semantic roles:

- `mechanical-worker`
- `implementation-worker`
- `complex-specialist`
- `independent-reviewer`

The quality contract remains unchanged: narrow scope, explicit interfaces, evidence-backed return, parent verification, one writer for shared state.

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

Exact model identity, reasoning level, freshness, read-only isolation, and cost savings are technical claims that require observable evidence. Never convert a requested parameter or worker self-report into a guarantee.

## Independent review and QUALITY VERDICT

For `audit` or `full`, use a separate review workstream when Work exposes one. Request Sol/high when supported, but call it a verified Sol reviewer only when runtime attestation proves that identity. Otherwise call it `independent-reviewer`.

Reviewer output:

~~~text
REVIEW
VERDICT: ship | fix-first | rethink
REASON: <evidence-based reason>
FINDINGS: <precise findings or none>
RESIDUAL RISK: <remaining risk or none>
~~~

Map this separately to:

~~~text
QUALITY VERDICT
status: ship | fix-first | rethink
~~~

A correction invalidates the prior quality verdict and requires fresh verification. The capability tier does not change because of a quality failure.

## EFFICIENCY EVIDENCE

Report efficiency separately from correctness:

~~~text
EFFICIENCY EVIDENCE
routing_mix_requested: <summary>
usage_telemetry_available: yes | no
usage_consistent_with_requested_mix: yes | no | unknown
unnecessary_delegations: <count or unknown>
efficiency_verdict: verified | plausible | unverified | inefficient
~~~

Use `verified` only when attributable usage telemetry supports the requested model mix and delegation was justified. Use `plausible` when cheap-model requests were accepted and task allocation was sensible but backend usage cannot be observed. Never claim savings from requested routing alone.

## Acceptance

Report completion only after reconciling worker claims with observable state. Final material test/report output must keep these dimensions separate:

~~~text
CAPABILITY TIER: A | B | C
ROUTING EVIDENCE: <requested vs accepted vs attested>
QUALITY VERDICT: ship | fix-first | rethink
EFFICIENCY EVIDENCE: verified | plausible | unverified | inefficient
VERIFIED: <observable facts>
UNVERIFIED: <remaining claims>
~~~

Include the route, workers actually used, parent verification performed, and any model/reasoning/permission/usage assumptions that could not be independently observed.
