# Sol Advisor Work

**A quality-first AI team for ChatGPT Work.**

Sol Advisor Work is a Work-native adaptation of the original [Sol Advisor](https://github.com/DannyMac180/sol-advisor). Instead of asking one AI model to do everything, it organizes the work like a small team.

The ideal architecture is simple: **Sol leads, Luna handles lighter work, Terra handles substantial implementation, and an independent reviewer checks important results.** Exact model assignment is used only when the current Work runtime exposes and verifies those controls.

## Why it exists

Not every task needs the most powerful model from beginning to end. Simple work can be handled faster by a lighter worker, while difficult decisions deserve stronger reasoning.

Sol Advisor Work is **quality-first**: the parent owns the overall problem, architecture, verification, and acceptance, while delegation is used only when the runtime can support it safely.

## Meet the AI team

When Work exposes exact model routing, the preferred roles are:

- **Sol — Team lead and architect.** Understands the full problem, makes important decisions, verifies work, and accepts the final result.
- **Luna — Fast specialist.** Handles simple, repetitive, mechanical, or clearly defined work.
- **Terra — Main implementer.** Handles medium-to-difficult execution that needs more judgment and context.
- **Fresh Sol — Independent reviewer.** Reviews important or risky work in a separate workstream when Work can provide it.

If Work does not expose exact model routing, the same workflow uses generic roles instead of pretending a hidden worker is Luna, Terra, or Sol.

## How it works

```text
                         USER
                           │
                           ▼
                    ┌─────────────┐
                    │   PARENT    │
                    │ Quality lead│
                    └──────┬──────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
          Simple work   Medium work   Hard decisions
              │            │            │
              ▼            ▼            ▼
       light worker   implementer   specialist
              │            │            │
              └────────────┴────────────┘
                           │
                           ▼
                    Parent verifies
                           │
                    High-risk task?
                      /         \
                    No           Yes
                    │             │
                   DONE      Independent review
```

When exact model control is available, those roles map to Luna, Terra, and Sol. Otherwise, the role contracts stay the same without unsupported model claims.

## Three Work capability levels

Every run begins with a capability check:

- **Tier A — Exact routing.** Work exposes multi-agent execution and enough evidence to select the intended worker model. Luna/Terra/Sol names may be used when verified.
- **Tier B — Work multi-agent.** Work can run parallel agents, but exact worker model identity is not guaranteed. The plugin uses role names such as `implementation-worker` or `complex-specialist`.
- **Tier C — Safe fallback.** The plugin cannot access multiple agents. The parent performs the same structured workflow directly and reports that delegation was unavailable.

This prevents the plugin from claiming a model, reasoning level, fresh context, or read-only sandbox that Work did not actually prove.

## Work modes

- **Solo** — the parent handles and verifies the task.
- **Delegate** — one clearly scoped worker performs implementation, then the parent checks it.
- **Parallel Read** — several workers investigate independent questions while the parent combines the evidence.
- **Audit** — the parent completes the work and a separate reviewer checks it when available.
- **Full** — for broad or high-risk tasks: parallel research may be used, exactly one writer performs shared-state changes, the parent verifies, and independent review is added when supported.

## One writer, many researchers

Parallel research is useful; competing writes are dangerous. Sol Advisor Work therefore prefers several read-only research lanes but **one writer at a time** for shared files or artifacts.

```text
Research:        Agent A ─┐
                 Agent B ─┼──► Parent combines findings
                 Agent C ─┘

Implementation:             ► One writer ► Parent verifies
```

## Why the strongest reasoning stays near the top

The most expensive mistake in a multi-agent system is often not bad implementation. It is **solving the wrong problem**. A worker can perfectly execute a bad plan.

The quality-first design therefore keeps architecture, escalation, verification, and final acceptance in the control plane rather than blindly trusting worker reports.

## Designed for ChatGPT Work

The original Sol Advisor was built around Codex-native custom agents. Sol Advisor Work instead targets Work's hosted execution model and deliberately avoids depending on Codex-only TOML agents, local rollout inspectors, or unproven per-agent sandbox guarantees.

## Technical reliability

The repository includes:

- the standard `.agents/plugins/marketplace.json` entry;
- an installable package under `plugins/sol-advisor-work/`;
- `.codex-plugin/plugin.json` and skill metadata following the OpenAI plugin layout;
- an explicit A/B/C runtime capability gate;
- scoped worker contracts and parent verification rules;
- serialized shared-state writers;
- GitHub Actions verification via `scripts/verify.py` to detect missing files, invalid JSON, package drift, bad marketplace paths, oversized starter prompts, and missing capability-contract markers.

Static packaging can be validated by CI. Exact multi-model routing remains a runtime capability of ChatGPT Work and is never falsely presented as a repository-level guarantee.

## Runtime evidence and efficiency guardrails

Each run must begin with a capability probe and record an execution ID when the
host provides one. Every lane separates the requested model/reasoning from
request acceptance, effective-model attestation, usage verification, tokens,
and cost. Hidden controls fail closed to semantic roles or parent-only work.

The delegation gate accounts for spawn, context-transfer, synthesis, and
verification overhead. Tiny deterministic work stays in the parent, delegated
implementation has one writer, and reviews are added only when risk or an
explicit audit justifies them. See `skills/orchestration/references/runtime-evidence.md`.

## When should I use Sol Advisor Work?

Choose Sol Advisor Work when **quality is the priority** and you want the strongest available reasoning continuously responsible for architecture and acceptance.

For a more cost-focused design that escalates difficult work only when needed, see **Luna Advisor Work**.

## For technical users

The complete routing and safety contracts live in:

- `skills/orchestration/SKILL.md`
- `skills/orchestration/references/role-contracts.md`
- `skills/orchestration/references/operations.md`

The installable copy is mirrored under `plugins/sol-advisor-work/`, and CI requires both copies to remain identical.

## Attribution

Sol Advisor Work is derived conceptually and structurally from [DannyMac180/sol-advisor](https://github.com/DannyMac180/sol-advisor), created by Daniel McAteer and distributed under the MIT License. This Work-native adaptation is maintained separately.
