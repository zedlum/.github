# .github

Org-wide defaults for zedlum. Two jobs:

1. Provides `profile/README.md`, shown on the org's GitHub page.
2. Marked as a template repository. New component repos should be created
   from it (`gh repo create zedlum/<name> --template zedlum/.github`) to
   inherit conventional-commit enforcement and release automation from
   the start.

## What's in the template

- `Makefile` — build/install/test/freeze targets (Go + optional Python venv)
- `.pre-commit-config.yaml` / `.cz.toml` — commitizen commit-msg enforcement
  locally, plus a `make freeze` hook keeping `requirements.txt` in sync
- `.github/workflows/commitizen-check.yml` — same enforcement in CI
- `.github/workflows/release.yml` — semver bump + changelog on merge to main

Rename/adjust the Makefile's binary name and build steps per repo.
