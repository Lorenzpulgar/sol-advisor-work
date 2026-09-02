# PLUS-ONLY WORK PROOF

This contract verifies the strongest claims available from ChatGPT Work on a normal ChatGPT Plus allowance without external billing or infrastructure.

## Hard boundary

- No OpenAI API.
- No external MCP server.
- No Platform API key, tunnel, external telemetry service, or separate paid runtime.
- Use only the active ChatGPT Work session, native agent controls, observable agent/workstream UI, repository tools already available to the session, and parent verification.
- requested != accepted != attested. A requested or accepted model/reasoning setting is not backend execution attestation.
- Tier B is a valid passing runtime outcome when Work creates the expected distinct workstreams and accepts routing controls but hides effective-model metadata.
- If the host exposes no effective model metadata, the effective backend model remains unverified.

## Purpose

Keep three dimensions independent:

1. functional proof — did Work follow the Advisor protocol?
2. capability tier — what does the host expose and attest?
3. backend model attestation — did the host prove the effective worker model?

A quality defect does not change capability tier. Tier B may receive a functional pass.

## Nonce-bound native smoke test

Create one short random-looking `PROOF_NONCE` in the parent and use it unchanged in every lane.

Use the smallest representative lanes:

```text
mechanical: request Luna / low
medium: request Terra / medium
complex: request Sol / high
review: request Sol / high in a separate review workstream
```

Each workstream receives the same nonce, an exact lane name, a tiny deterministic objective, and an exact return contract. The parent verifies nonce, lane, output correctness, request acceptance, and observable workstream separation.

## Canonical proof tokens

Critical proof fields are protocol tokens, not prose. Do not paraphrase canonical proof tokens.

For a Tier B smoke-test lane that asks the worker to identify the expected capability classification, return exactly:

```text
PROOF_CAPABILITY_TIER=B
```

Do not return `Tier B`, `Tier 2`, `B`, or any synonym in place of that token.

The final functional grade must be exactly one of:

```text
FUNCTIONAL_GRADE=PASS-PLUS
FUNCTIONAL_GRADE=PARTIAL-PLUS
FUNCTIONAL_GRADE=FAIL-PLUS
```

The backend-model field must be exactly one of:

```text
BACKEND_MODEL_ATTESTATION=VERIFIED
BACKEND_MODEL_ATTESTATION=UNVERIFIED
```

Use `BACKEND_MODEL_ATTESTATION=VERIFIED` only when host-provided execution metadata attests the effective model. Accepted model controls, worker prose, task quality, and UI agent count are insufficient.

## Functional grading

`FUNCTIONAL_GRADE=PASS-PLUS` requires the required native workstreams to complete, nonce/lane/output checks to pass, requested controls to be accepted where supported, parent verification to pass, and separate review to occur when requested, with no false backend claims.

`FUNCTIONAL_GRADE=PARTIAL-PLUS` means the Advisor followed its capability/fallback contract but one or more native Work capabilities or deterministic proof assertions were unavailable, ambiguous, or incorrect.

`FUNCTIONAL_GRADE=FAIL-PLUS` means the Advisor violated the contract, fabricated evidence, mixed nonces/lanes, failed required parent verification, or could not execute its required fallback.

A functional pass does not imply Tier A. Tier B can receive `FUNCTIONAL_GRADE=PASS-PLUS`.

## Canonical evidence report

```text
PLUS-ONLY WORK PROOF
PROOF_NONCE=<value>
FUNCTIONAL_GRADE=PASS-PLUS | PARTIAL-PLUS | FAIL-PLUS
PROOF_CAPABILITY_TIER=A | B | C
BACKEND_MODEL_ATTESTATION=VERIFIED | UNVERIFIED
MULTI_AGENT_OBSERVED=yes | no
SEPARATE_WORKSTREAMS_OBSERVED=<count>

MECHANICAL: requested=<...>; accepted=<yes/no/unknown>; nonce_verified=<yes/no>; output_verified=<yes/no>; runtime_attested=<yes/no>
MEDIUM: requested=<...>; accepted=<...>; nonce_verified=<...>; output_verified=<...>; runtime_attested=<...>
COMPLEX: requested=<...>; accepted=<...>; nonce_verified=<...>; output_verified=<...>; runtime_attested=<...>
REVIEW: requested=<...>; accepted=<...>; nonce_verified=<...>; output_verified=<...>; runtime_attested=<...>

QUALITY_VERDICT=ship | fix-first | rethink
EFFICIENCY_VERDICT=verified | plausible | unverified | inefficient
```

Canonical keys and enum values must be returned exactly. Explanatory prose may follow only where requested, and must not replace these fields.

## Claim rules

Functional evidence may prove that Work created distinct workstreams, delivered the intended lane packet, accepted requested controls, returned nonce-bound results, and passed parent/reviewer checks.

Do not use worker self-identification, model names in prompts, accepted parameters, UI labels without host execution metadata, or successful task quality as proof of the effective backend model.

Efficiency may be `plausible` when cheaper-model requests were accepted, delegation was justified, and unnecessary delegations were zero, but model-specific usage is hidden. Call efficiency `verified` only when host-provided attributable usage telemetry exists.

## Production implication

A successful Plus-only proof is sufficient to use the Advisor as a functional Work orchestrator under honest Tier B semantics. It is not sufficient to guarantee hidden Luna/Terra/Sol execution or exact savings.
