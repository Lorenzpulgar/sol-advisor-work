# Sol Advisor Work

**A quality-first AI team for ChatGPT Work.**

Sol Advisor Work is a Work-native adaptation of the original [Sol Advisor](https://github.com/DannyMac180/sol-advisor). Instead of asking one AI model to do everything, it organizes several models like a small team and gives each one the kind of work it handles best.

The main idea is simple: **Sol leads, Luna handles lighter work, Terra handles substantial implementation, and a fresh Sol can review important results.**

## Why it exists

Not every task needs the most powerful model from beginning to end. Simple work can be handled faster by a lighter model, while difficult decisions deserve stronger reasoning.

Sol Advisor Work keeps **GPT-5.6 Sol** in charge of the overall task. Sol understands the request, chooses the approach, decides when to delegate, checks the result, and decides when the work is ready.

This makes Sol Advisor Work a **quality-first** orchestrator: it saves work where it makes sense, but keeps the strongest model responsible for the important decisions.

## Meet the AI team

- **Sol — Team lead and architect.** Understands the full problem, makes important decisions, coordinates the other models, verifies their work, and accepts the final result.
- **Luna — Fast specialist.** Handles simple, repetitive, mechanical, or clearly defined work.
- **Terra — Main implementer.** Handles medium-to-difficult execution that needs more judgment and context.
- **Fresh Sol — Independent reviewer.** For important or risky work, a new Sol session reviews the result without relying on the original conversation context.

## How it works

```text
                         USER
                           │
                           ▼
                    ┌─────────────┐
                    │     SOL     │
                    │  Team Lead  │
                    └──────┬──────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
          Simple work   Medium work   Hard decisions
              │            │            │
              ▼            ▼            ▼
            LUNA          TERRA          SOL
              │            │            │
              └────────────┴────────────┘
                           │
                           ▼
                    SOL verifies
                           │
                    High-risk task?
                      /         \
                    No           Yes
                    │             │
                   DONE      Fresh SOL review
```

In plain English:

1. **Sol looks at the whole task first.**
2. If the work is simple and well defined, Sol can give it to Luna.
3. If the work requires more judgment or substantial implementation, Sol can give it to Terra.
4. Sol keeps difficult architectural or strategic decisions for itself.
5. Sol checks the actual result before accepting it.
6. If the task is especially important or risky, a fresh Sol can perform an independent final review.

## Work modes

Sol Advisor Work can choose between a few simple ways of working:

- **Solo** — Sol handles the task itself.
- **Delegate** — Sol gives one clearly defined part of the work to Luna or Terra and then checks it.
- **Parallel Read** — several agents can investigate different sources or parts of a problem at the same time, while Sol combines the findings.
- **Audit** — Sol completes the work and a fresh Sol independently reviews it.
- **Full** — for broad or high-risk tasks: research may happen in parallel, one agent performs the main implementation, Sol verifies it, and a fresh Sol performs the final review.

## One writer, many researchers

Work is especially useful when several agents can explore a problem at the same time. Sol Advisor Work encourages parallel agents for things such as research, reading documentation, exploring files, comparing alternatives, or finding missing tests.

For actual changes, however, it normally prefers **one writer at a time**. This reduces the chance that two agents overwrite each other's work or create conflicting changes.

```text
Research:        Agent A ─┐
                 Agent B ─┼──► Sol combines findings
                 Agent C ─┘

Implementation:             ► One writer ► Sol verifies
```

## Why Sol stays in charge

The most expensive mistake in a multi-agent system is often not bad implementation. It is **solving the wrong problem**.

A worker can perfectly execute a bad plan. By keeping Sol responsible for understanding the request, choosing the architecture, dividing the work, and checking the result, Sol Advisor Work puts the strongest reasoning where an error would have the biggest effect.

## Designed for ChatGPT Work

The original Sol Advisor was designed around Codex-native custom agents. Sol Advisor Work keeps the same core philosophy but is designed for **ChatGPT Work hosted subagents**.

That means this project focuses on:

- model-aware delegation inside Work;
- parallel research and exploration;
- clear responsibilities between agents;
- one-writer coordination for shared work;
- parent verification instead of blindly trusting worker reports;
- fresh review for important outcomes.

It does **not** pretend that Work provides local per-agent sandbox guarantees when those guarantees are not visible to the orchestrator.

## When should I use Sol Advisor Work?

Choose Sol Advisor Work when **quality is the priority** and you want the strongest model continuously responsible for the task.

It is a good fit for complex projects, important decisions, software work, research, business analysis, multi-step workflows, and tasks where a mistake near the beginning could affect everything that follows.

If your main priority is reducing model cost while still escalating difficult work to Sol when necessary, see **Luna Advisor Work**.

## For technical users

The public README intentionally keeps the concept simple. The full routing rules, worker contracts, verification behavior, and Work-specific safeguards live in:

- `skills/orchestration/SKILL.md`
- `skills/orchestration/references/role-contracts.md`
- `skills/orchestration/references/operations.md`

## Attribution

Sol Advisor Work is derived conceptually and structurally from [DannyMac180/sol-advisor](https://github.com/DannyMac180/sol-advisor), created by Daniel McAteer and distributed under the MIT License. This Work-native adaptation is maintained separately.
