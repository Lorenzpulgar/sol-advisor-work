# PLUS-ONLY WORK PROOF

This contract verifies the strongest claims available from ChatGPT Work on a normal ChatGPT Plus allowance without external billing or infrastructure.

## Hard boundary

- No OpenAI API.
- No external MCP server.
- No Platform API key, tunnel, external telemetry service, or separate paid runtime.
- Use only the active ChatGPT Work session, its native agent controls, observable agent/workstream UI, repository tools already available to the session, and parent verification.
- requested != accepted != attested. A requested or accepted model/reasoning setting is not backend execution attestation.
- Tier B is a valid passing runtime outcome when Work creates the expected distinct workstreams and accepts routing controls but hides effective-model metadata.
- If the host exposes no effective model metadata, the effective backend model remains unverified.

## Purpose

The proof answers two different questions and never merges them:

1. **Functional proof:** did this Advisor cause Work to follow the intended orchestration protocol?
2. **Backend proof:** did OpenAI attest the effective model/reasoning used by each worker?

The first can pass on Plus. The second passes only when the host itself exposes attributable metadata.

## Nonce-bound native smoke test

When the user explicitly requests a Plus-only proof, create a short random-looking run nonce in the parent, for example `ADVISOR_PROOF_7F3A9C`. Use that same nonce in every test lane. The nonce is not a security primitive; it prevents accidentally mixing outputs from different smoke tests.

Use the smallest representative lanes necessary:

```text
mechanical: request Luna / low
medium: request Terra / medium
complex: request Sol / high
review: request Sol / high in a separate review workstream
```

Each spawned workstream receives:

```text
PROOF_NONCE: <same nonce>
PROOF_LANE: <mechanical | medium | complex | review>
OBJECTIVE: <tiny deterministic representative task>
RETURN: nonce, lane, result, verification evidence only
```

The parent must verify that each returned nonce/lane matches the request and that the result is correct. Distinct workstreams may be counted only when the Work host exposes them as distinct agents/workstreams.

## Functional proof grade

Return one of:

- `PASS-PLUS`: Work exposed multi-agent execution; required representative workstreams completed; requested controls were accepted where available; parent verification passed; review was separate when requested; no false backend-model claims were made.
- `PARTIAL-PLUS`: the Advisor loaded and followed its capability/fallback rules, but one or more native Work capabilities needed for the multi-agent smoke test were unavailable or ambiguous.
- `FAIL-PLUS`: the Advisor violated its contract, fabricated unavailable evidence, failed parent verification, mixed lanes/nonces, or could not execute its required fallback.

A `PASS-PLUS` does **not** imply Tier A. Tier B can be `PASS-PLUS`.

## Evidence report

```text
PLUS-ONLY WORK PROOF
proof_nonce: <value>
functional_grade: PASS-PLUS | PARTIAL-PLUS | FAIL-PLUS
capability_tier: A | B | C
multi_agent_observed: yes | no
separate_workstreams_observed: <count>

LANES:
mechanical: requested=<...>; accepted=<yes/no/unknown>; nonce_verified=<yes/no>; output_verified=<yes/no>; runtime_attested=<yes/no>
medium: requested=<...>; accepted=<...>; nonce_verified=<...>; output_verified=<...>; runtime_attested=<...>
complex: requested=<...>; accepted=<...>; nonce_verified=<...>; output_verified=<...>; runtime_attested=<...>
review: requested=<...>; accepted=<...>; nonce_verified=<...>; output_verified=<...>; runtime_attested=<...>

QUALITY VERDICT: ship | fix-first | rethink
BACKEND MODEL VERDICT: verified | unverified
EFFICIENCY VERDICT: verified | plausible | unverified | inefficient
```

## Claim rules

Functional evidence may prove that Work created distinct workstreams, received the intended lane packet, accepted requested routing controls, returned lane-bound results, and passed parent/reviewer checks.

Do not use worker self-identification, model names in prompts, accepted parameters, UI labels without host execution metadata, or successful task quality as proof of the effective backend model.

Efficiency may be `plausible` when cheaper-model routing requests were accepted, delegation was justified, and unnecessary delegations were zero, but model-specific usage is hidden. Call efficiency `verified` only when host-provided attributable usage telemetry exists.

## Production implication

A successful Plus-only proof is sufficient to use the Advisor as a functional Work orchestrator under its honest Tier B semantics. It is not sufficient to guarantee hidden Luna/Terra/Sol execution or exact savings. Keep those claims unverified until OpenAI exposes backend attestation or attributable usage telemetry in the active host.
