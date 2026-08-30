# Runtime evidence and budget contract

The repository cannot inspect hidden backend execution. The parent must record
only host-provided evidence and must fail closed when a requested control is not
observable.

## Capability probe

Run this before spawning or claiming a route:

```text
WORK CAPABILITY CHECK
multi_agent: unavailable | available
per_agent_model_control: unavailable | available
per_agent_reasoning_control: unavailable | available
observable_agent_identity: unavailable | available
usage_telemetry: unavailable | available
execution_id: <host value or unavailable>
capability_tier: A | B | C
```

Tier A requires multi-agent execution and host evidence of the effective model.
Tier B permits role-based delegation but not exact model claims. Tier C is
parent-only. `usage_telemetry=available` does not prove routing unless the
records are attributable to the execution ID and lane.

## Lane record

Every requested lane gets one record, even when it is not delegated:

```text
LANE
name: mechanical | routine | medium | complex | review
requested_model: <value or none>
requested_reasoning: <value or none>
request_accepted: yes | no | unknown
runtime_attested: yes | no
observed_model: <host value or unavailable>
usage_verified: yes | no | unavailable
input_tokens: <host value or unavailable>
output_tokens: <host value or unavailable>
cost: <host value or unavailable>
```

Worker prose, names, badges, and prompt parameters are never evidence of
`runtime_attested` or `usage_verified`.

## Budget and delegation gate

Before an optional delegation, estimate spawn, context-transfer, synthesis, and
verification cost. Keep the task in the parent when the expected value does not
exceed that overhead. Use at most one implementation writer. A minimal smoke
test may exercise lanes explicitly, but production work must not spawn one
worker per lane without a value justification.

If model controls, identity, or usage are hidden, preserve the semantic role,
mark exact routing as unverified, and continue only when the user did not
require a hard guarantee.

## Completion rule

Efficiency is `verified` only when attributable telemetry confirms the lane mix
and the delegation was justified. Otherwise use `plausible` only when the host
accepted the route and the allocation was sensible; use `unverified` when
acceptance or usage is unknown.
