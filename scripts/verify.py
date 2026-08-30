#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAME = "sol-advisor-work"
REQUIRED = [
    ".codex-plugin/plugin.json",
    ".agents/plugins/marketplace.json",
    "skills/orchestration/SKILL.md",
    "skills/orchestration/agents/openai.yaml",
    "skills/orchestration/references/operations.md",
    "skills/orchestration/references/role-contracts.md",
    "README.md",
    "LICENSE",
]

errors = []
for rel in REQUIRED:
    if not (ROOT / rel).is_file():
        errors.append(f"missing required file: {rel}")

try:
    manifest = json.loads((ROOT / ".codex-plugin/plugin.json").read_text())
    if manifest.get("name") != NAME:
        errors.append("plugin manifest name mismatch")
    if manifest.get("skills") != "./skills/":
        errors.append("plugin manifest skills path must be ./skills/")
    interface = manifest.get("interface", {})
    if not interface.get("displayName") or not interface.get("defaultPrompt"):
        errors.append("plugin interface requires displayName and defaultPrompt")
except Exception as exc:
    errors.append(f"invalid plugin manifest: {exc}")

try:
    marketplace = json.loads((ROOT / ".agents/plugins/marketplace.json").read_text())
    plugins = marketplace.get("plugins", [])
    entry = next((p for p in plugins if p.get("name") == NAME), None)
    if not entry:
        errors.append("marketplace entry missing")
    else:
        source = entry.get("source", {})
        if source.get("source") != "local" or source.get("path") != ".":
            errors.append("marketplace source must point to repository root")
except Exception as exc:
    errors.append(f"invalid marketplace manifest: {exc}")

try:
    skill = (ROOT / "skills/orchestration/SKILL.md").read_text()
    for marker in ["name: orchestration", "WORK CAPABILITY CHECK", "Tier A", "Tier B", "Tier C", "Acceptance"]:
        if marker not in skill:
            errors.append(f"SKILL.md missing required contract marker: {marker}")
except Exception as exc:
    errors.append(f"unable to read SKILL.md: {exc}")

try:
    yaml = (ROOT / "skills/orchestration/agents/openai.yaml").read_text()
    for marker in ["display_name:", "short_description:", "default_prompt:"]:
        if marker not in yaml:
            errors.append(f"openai.yaml missing {marker}")
except Exception as exc:
    errors.append(f"unable to read openai.yaml: {exc}")

if errors:
    print("VERIFY FAILED")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("VERIFY OK")
print(f"plugin={NAME}")
print("marketplace=root")
print("capability_gate=A/B/C")
