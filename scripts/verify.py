#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAME = "sol-advisor-work"
PKG = ROOT / "plugins" / NAME
PAIRS = [
    (ROOT / ".codex-plugin/plugin.json", PKG / ".codex-plugin/plugin.json"),
    (ROOT / "skills/orchestration/SKILL.md", PKG / "skills/orchestration/SKILL.md"),
    (ROOT / "skills/orchestration/agents/openai.yaml", PKG / "skills/orchestration/agents/openai.yaml"),
    (ROOT / "skills/orchestration/references/operations.md", PKG / "skills/orchestration/references/operations.md"),
    (ROOT / "skills/orchestration/references/role-contracts.md", PKG / "skills/orchestration/references/role-contracts.md"),
    (ROOT / "skills/orchestration/references/runtime-evidence.md", PKG / "skills/orchestration/references/runtime-evidence.md"),
    (ROOT / "skills/orchestration/references/plus-work-proof.md", PKG / "skills/orchestration/references/plus-work-proof.md"),
]
errors = []

for root_file, pkg_file in PAIRS:
    if not root_file.is_file():
        errors.append(f"missing root source: {root_file.relative_to(ROOT)}")
    if not pkg_file.is_file():
        errors.append(f"missing packaged source: {pkg_file.relative_to(ROOT)}")
    if root_file.is_file() and pkg_file.is_file() and root_file.read_bytes() != pkg_file.read_bytes():
        errors.append(f"package drift: {root_file.relative_to(ROOT)} != {pkg_file.relative_to(ROOT)}")

for rel in [".agents/plugins/marketplace.json", ".github/workflows/verify.yml", "README.md", "LICENSE"]:
    if not (ROOT / rel).is_file():
        errors.append(f"missing required file: {rel}")

try:
    manifest = json.loads((PKG / ".codex-plugin/plugin.json").read_text())
    if manifest.get("name") != NAME:
        errors.append("plugin manifest name mismatch")
    if manifest.get("skills") != "./skills/":
        errors.append("plugin manifest skills path must be ./skills/")
    version = tuple(map(int, manifest.get("version", "0.0.0").split(".")))
    if version < (0, 3, 0):
        errors.append("plugin version must be >=0.3.0 for Plus-only proof contract")
    prompts = manifest.get("interface", {}).get("defaultPrompt", [])
    if not prompts or len(prompts) > 3 or any(len(p) > 128 for p in prompts):
        errors.append("defaultPrompt must contain 1-3 entries of <=128 characters")
except Exception as exc:
    errors.append(f"invalid plugin manifest: {exc}")

try:
    marketplace = json.loads((ROOT / ".agents/plugins/marketplace.json").read_text())
    entry = next((p for p in marketplace.get("plugins", []) if p.get("name") == NAME), None)
    if not entry:
        errors.append("marketplace entry missing")
    else:
        source = entry.get("source", {})
        if source.get("source") != "local" or source.get("path") != f"./plugins/{NAME}":
            errors.append("marketplace source must use standard ./plugins/<name> path")
        policy = entry.get("policy", {})
        if policy.get("installation") != "AVAILABLE" or policy.get("authentication") not in {"ON_INSTALL", "ON_USE"}:
            errors.append("marketplace policy invalid")
except Exception as exc:
    errors.append(f"invalid marketplace manifest: {exc}")

skill = PKG / "skills/orchestration/SKILL.md"
if skill.is_file():
    text = skill.read_text()
    markers = [
        "name: orchestration",
        "WORK CAPABILITY CHECK",
        "Tier A", "Tier B", "Tier C",
        "ROUTING EVIDENCE",
        "DELEGATION VALUE CHECK",
        "QUALITY VERDICT",
        "EFFICIENCY EVIDENCE",
        "request_accepted", "runtime_attested", "usage_verified",
        "Acceptance",
        "Fail-closed routing and budget gate",
        "references/runtime-evidence.md",
        "execution_id", "input_tokens", "output_tokens",
        "PLUS-ONLY WORK PROOF",
        "references/plus-work-proof.md",
        "PASS-PLUS", "PARTIAL-PLUS", "FAIL-PLUS",
        "PROOF_NONCE",
        "No OpenAI API",
        "No external MCP server",
    ]
    for marker in markers:
        if marker not in text:
            errors.append(f"SKILL.md missing required marker: {marker}")

proof = PKG / "skills/orchestration/references/plus-work-proof.md"
if proof.is_file():
    text = proof.read_text()
    for marker in [
        "PLUS-ONLY WORK PROOF",
        "No OpenAI API",
        "No external MCP server",
        "requested != accepted != attested",
        "Tier B is a valid passing runtime outcome",
        "effective backend model remains unverified",
        "PASS-PLUS", "PARTIAL-PLUS", "FAIL-PLUS",
    ]:
        if marker not in text:
            errors.append(f"plus-work-proof.md missing required marker: {marker}")

yaml = PKG / "skills/orchestration/agents/openai.yaml"
if yaml.is_file():
    text = yaml.read_text()
    for marker in ["display_name:", "short_description:", "default_prompt:"]:
        if marker not in text:
            errors.append(f"openai.yaml missing {marker}")

if errors:
    print("VERIFY FAILED")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("VERIFY OK")
print(f"plugin={NAME}")
print(f"package=plugins/{NAME}")
print("capability_gate=A/B/C")
print("routing_evidence=requested/accepted/attested")
print("plus_only_proof=ok")
print("quality_separate=ok")
print("efficiency_evidence=ok")
print("delegation_value_check=ok")
print("root_package_sync=ok")
