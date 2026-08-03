# AGENTS.md for biolink-model

A LinkML schema repository: the Biolink data model (entities, associations, predicates) plus all derived artifacts (Python, JSON-Schema, OWL, SHACL, ShEx, Protobuf, JSON-LD, prefix map).

## Toolchain

- Uses `uv` (never `pip`). `uv sync` installs; `uv run <cmd>` runs things. `Makefile` targets wrap `uv run` for you.
- `linkml` and `linkml-runtime` are pinned to **`==1.10.0`** in `pyproject.toml`. Do not bump casually — generation output depends on the exact version.
- Python `>=3.10` (CI matrix: 3.10–3.13). Default branch is `master`.

## Source of truth vs. derived files (critical)

- **Edit the root files:** `biolink-model.yaml` (hyphenated) and `attributes.yaml`. The schema does `imports: [linkml:types, attributes]`, so `attributes.yaml` must sit next to it.
- **Never edit** the copies at `src/biolink_model/schema/biolink_model.yaml` + `src/biolink_model/schema/attributes.yaml`. The build regenerates them by copying the root files in (note the hyphen→underscore rename).
- **Never edit** anything under `project/`, `docs/`, or `src/biolink_model/datamodel/` (e.g. `model.py`) — all derived. The `push-main-regenerate-artifacts` workflow re-derives `project/*` and `src/*` on push to `master`.

The build copies the root schema because `about.yaml` → `source_schema_path` is `src/biolink_model/schema/biolink_model.yaml` (read via `utils/get-value.sh`), so every generate/test/lint target first does that `cp`.

## Common commands

```
make help            # list targets
make test            # full local check = gen-project + pytest + linkml-lint + codespell
make gen-project     # regenerate all project/ artifacts + Python datamodel
make lint            # linkml-lint only (auto-copies schema first)
make test-python     # pytest only (auto-copies schema first)
make testdoc         # build docs + local mkdocs server
```

- Running `pytest` directly will test a **stale** schema unless you first copy the root yaml in. Prefer `make test-python` / `make lint` / `make test` — they copy automatically.
- `make tests` (plural) and `tox.ini` are stale/broken (typo `biolink_model.yamlO`; tox targets py38/39). Ignore them; use `make test`.
- yamllint is **not** part of `make test`. CI runs it separately:
  `uv run yamllint -c .yamllint-config biolink-model.yaml` (line-length max 200, enforced on PRs).
- A single test: `uv run pytest tests/test_data.py` (after `cp biolink-model.yaml src/biolink_model/schema/biolink_model.yaml`). Main schema class for examples is `Entity`.

## CI verification (mirrors these locally)

PRs run (`pr-verify-pull-request`, `pr-codespell`, `pr-validate-biolink-yaml`, `pr-check-dependencies`):
`make test` + `codespell` + `yamllint biolink-model.yaml`. The dependency check rebuilds `uv.lock` from scratch, so keep version ranges sane in `pyproject.toml`.

## Schema-editing conventions

- Add meaningful `description:` to every class/slot/enum/type.
- For polymorphic classes, mark the discriminator slot `type_designator: true`.
- Map to existing standards where appropriate (e.g. `dcterms`, OBO ontologies).
- **Never guess OBO/ontology term IDs.** Look them up via the OLS API first.
- linkml-lint runs with `.linkmllint.yaml` which disables `standard_naming`, `canonical_prefixes`, and `recommended` — so those won't block, but don't rely on them catching issues.

## Note

`CLAUDE.md` and `.github/copilot-instructions.md` are stale duplicates of an earlier `AGENTS.md` (wrong filename, "justfile" typo). This file is the current source of truth.
