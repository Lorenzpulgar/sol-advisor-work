# Work-native role contracts

These contracts are for ChatGPT Work. Apply them according to the capability tier declared by `SKILL.md`.

## Naming rule

- Tier A may use exact model lane names only when the runtime exposes evidence for them.
- Tier B uses semantic role names and never claims hidden model identity.
- Tier C collapses worker execution into the parent while preserving the same packet and verification discipline.

A requested model, reasoning level, fresh context, or read-only behavior is not a technical guarantee unless the host exposes supporting evidence.

## Shared implementation packet

Every implementation worker receives all sections below.

~~~text
ROLE
<mechanical-worker | implementation-worker | complex-specialist>

OBJECTIVE
<Observable outcome and why it matters.>

FILES / ARTIFACT OWNERSHIP
You own only:
- <exact file, folder, document, spreadsheet, slide deck, or artifact scope>

Preserve concurrent edits. Do not broaden scope or modify unowned artifacts.

INTERFACES
- <APIs, types, schemas, links, formats, visual rules, or behavior to preserve.>

CONSTRAINTS
- <settled architecture, safety boundaries, excluded scope, style, performance, compatibility.>

VERIFICATION
- Check: <command, inspection, query, render, or consistency test>
  Success: <observable evidence>

RETURN
IMPLEMENTATION REPORT
STATUS: complete | partial | blocked
OBJECTIVE: <one-line restatement>
CHANGES: <artifact-by-artifact summary>
VERIFIED: <checks and concrete evidence>
JUDGMENT CALLS: <choices left open by the packet, or none>
GAPS: <remaining issues or none>
~~~

The parent independently verifies observable state before acceptance.

## Mechanical lane

Tier A may request GPT-5.6 Luna for mechanical/light or tightly bounded work. Tier B uses `mechanical-worker`. Use it for repetitive edits, renames, formatting, simple wiring, well-specified CRUD, extraction, routine research, bounded document transformation, and similar deterministic work.

The worker must not silently change architecture.

## Implementation lane

Tier A may request GPT-5.6 Terra for medium implementation and work requiring local judgment, integration, debugging, non-trivial refactors, or wider context. Tier B uses `implementation-worker`.

The worker may resolve implementation details left open by the packet, but must surface architectural ambiguity instead of redefining interfaces.

## Complex specialist

Tier A may request GPT-5.6 Sol/high when exact routing is proven. Tier B uses `complex-specialist`. This lane should normally return a decision packet rather than perform routine implementation.

~~~text
COMPLEX DECISION
PROBLEM: <root problem>
DECISION: <recommended architecture/approach>
INVARIANTS: <must remain true>
IMPLEMENTATION PLAN: <ordered steps>
RISKS: <material risks>
ACCEPTANCE CRITERIA: <observable success conditions>
~~~

## Independent reviewer

For audit/full routes, use a separate review workstream when the runtime supports one. Tier A may request Sol/high when observable; Tier B uses `independent-reviewer`; Tier C performs a disclosed second-pass parent audit.

~~~text
ROLE
Act as an independent final reviewer when you are in a separate workstream. Do not edit or implement fixes.

STATED GOAL
<user outcome>

ACCUMULATED CHANGE SET
<exact artifacts/files and observable state>

INTERFACES AND CONSTRAINTS
<requirements that must hold>

VERIFICATION EVIDENCE
<parent-observed checks>

REVIEW
VERDICT: ship | fix-first | rethink
REASON: <decisive evidence>
FINDINGS: <precise findings or none>
RESIDUAL RISK: <remaining risk or none>
~~~

A fix invalidates the prior verdict. Never claim enforced read-only isolation unless Work exposes proof.

## Parallel read workers

Parallel readers receive disjoint questions and no mutation objective. Require concise evidence-backed output. The parent synthesizes, resolves conflicts, and owns final decisions.
