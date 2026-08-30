# Sol Advisor Work

A ChatGPT Work-native adaptation of Sol Advisor, based on the original MIT-licensed project by Daniel McAteer.

## Goal

Keep GPT-5.6 Sol as the control plane for intent, architecture, routing, verification, and acceptance while delegating execution selectively:

- Luna for mechanical/light and tightly bounded work.
- Terra for medium or judgment-heavy implementation.
- Fresh Sol for independent review when risk justifies it.

Unlike the Codex-native original, this repository does not rely on local custom-agent TOML registration, local runtime inspection, or per-agent sandbox guarantees. It is designed around hosted Work subagents.

## Core policy

1. Declare a `WORK ROUTE` before substantial task work.
2. Use the least expensive model that preserves correctness.
3. Parallelize independent read-heavy tasks.
4. Serialize shared-state writes and prefer exactly one writer.
5. Treat worker reports as claims; parent verifies observable state.
6. Use fresh Sol review only for `audit` or `full` routes.
7. Never claim model pins, reasoning effort, or isolation that Work did not expose.

## Routes

- `solo`
- `delegate`
- `parallel-read`
- `audit`
- `full`

See `skills/orchestration/SKILL.md` for the complete workflow and `references/` for role contracts and operations.

## Attribution

This project is derived conceptually and structurally from [DannyMac180/sol-advisor](https://github.com/DannyMac180/sol-advisor), licensed under MIT. The Work-native adaptation is maintained separately.
