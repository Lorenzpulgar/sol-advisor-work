import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PlusWorkProofContractTests(unittest.TestCase):
    def test_plus_work_proof_reference_exists(self):
        path = ROOT / "skills/orchestration/references/plus-work-proof.md"
        self.assertTrue(path.is_file(), "missing Plus-only Work proof contract")

    def test_plus_work_proof_is_packaged_identically(self):
        root = ROOT / "skills/orchestration/references/plus-work-proof.md"
        pkg = ROOT / "plugins/sol-advisor-work/skills/orchestration/references/plus-work-proof.md"
        self.assertTrue(pkg.is_file(), "packaged Plus-only proof contract missing")
        self.assertEqual(root.read_bytes(), pkg.read_bytes(), "Plus-only proof contract drift")

    def test_contract_forbids_api_and_fake_backend_attestation(self):
        text = (ROOT / "skills/orchestration/references/plus-work-proof.md").read_text()
        for marker in [
            "PLUS-ONLY WORK PROOF",
            "No OpenAI API",
            "No external MCP server",
            "requested != accepted != attested",
            "Tier B is a valid passing runtime outcome",
            "effective backend model remains unverified",
        ]:
            self.assertIn(marker, text)

    def test_contract_uses_canonical_non_paraphrasable_tokens(self):
        text = (ROOT / "skills/orchestration/references/plus-work-proof.md").read_text()
        for marker in [
            "PROOF_CAPABILITY_TIER=B",
            "FUNCTIONAL_GRADE=PASS-PLUS",
            "FUNCTIONAL_GRADE=PARTIAL-PLUS",
            "FUNCTIONAL_GRADE=FAIL-PLUS",
            "BACKEND_MODEL_ATTESTATION=UNVERIFIED",
            "Do not paraphrase canonical proof tokens",
        ]:
            self.assertIn(marker, text)

    def test_skill_requires_canonical_plus_only_proof_when_requested(self):
        text = (ROOT / "skills/orchestration/SKILL.md").read_text()
        for marker in [
            "PLUS-ONLY WORK PROOF",
            "plus-work-proof.md",
            "PROOF_CAPABILITY_TIER=",
            "FUNCTIONAL_GRADE=",
            "BACKEND_MODEL_ATTESTATION=",
        ]:
            self.assertIn(marker, text)

    def test_manifest_version_bumped_for_canonical_contract_change(self):
        manifest = json.loads((ROOT / ".codex-plugin/plugin.json").read_text())
        self.assertGreaterEqual(tuple(map(int, manifest["version"].split("."))), (0, 3, 1))


if __name__ == "__main__":
    unittest.main()
