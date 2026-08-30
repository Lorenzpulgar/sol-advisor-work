# Work-native role contracts

These contracts are for ChatGPT Work hosted subagents. They intentionally avoid Codex-local
custom-agent TOML assumptions, local runtime inspectors, and per-agent sandbox guarantees.

## Shared implementation packet

Every implementation worker receives all sections below.

~~~text
ROLE
<mechanical implementer | medium implementer | complex specialist>

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

## Luna lane

Request GPT-5.6 Luna for mechanical/light or tightly bounded work. Prefer light/medium
reasoning for deterministic edits and medium/high reasoning when the spec is complete but
execution spans more context. Luna must not silently change architecture.

Use Luna for examples such as repetitive edits, renames, formatting, simple wiring,
well-specified CRUD, extraction, routine research, bounded document transformation, or
other work where the specification largely determines the solution.

## Terra lane

Request GPT-5.6 Terra for medium implementation and work requiring local judgment,
integration across components, debugging, non-trivial refactors, or wider context. Prefer
medium reasoning by default and high when evidence shows material complexity.

Terra may resolve implementation details left open by the packet, but must surface any
architectural ambiguity rather than silently redefine interfaces.

## Sol specialist lane

Request GPT-5.6 Sol / high when the parent wants an independent architecture specialist,
complex debugger, or deep reasoning pass. This lane should normally return a decision or
analysis packet rather than perform routine implementation.

~~~text
SOL DECISION
PROBLEM: <root problem>
DECISION: <recommended architecture/approach>
INVARIANTS: <must remain true>
IMPLEMENTATION PLAN: <ordered steps>
RISKS: <material risks>
ACCEPTANCE CRITERIA: <observable success conditions>
~~~

## Fresh Sol reviewer

For audit/full routes, spawn a fresh Sol context after parent verification. Instruct it
to remain behaviorally read-only. Do not claim hard isolation because Work subagents may
inherit available tools and permissions.

~~~text
ROLE
Act as an independent final reviewer. Do not edit or implement fixes.

STATED GOAL
<user outcome>

ACCUMULATED CHANGE SET
<exact artifacts/files and observable state>

INTERFACES AND CONSTRAINTS
<requirements that must hold>

VERIFICATION EVIDENCE
<parent-observed checks>

SOL REVIEW
VERDICT: ship | fix-first | rethink
REASON: <decisive evidence>
FINDINGS: <precise findings or none>
RESIDUAL RISK: <remaining risk or none>
~~~

A fix invalidates the prior verdict.

## Parallel read workers

Parallel read workers must have disjoint questions and no mutation objective. Give each
a narrow question and require concise evidence-backed output. The parent synthesizes,
resolves conflicts, and owns final decisions.
