# Entity Matrix Scripts

Scripts for generating the biolink entity matrix spreadsheet and coverage heatmap.

## Overview

These scripts analyze all Translator ingest data sources to determine which ingests provide edges for each combination of biolink subject and object entity classes. The biolink class hierarchy (both `is_a` and mixin ancestry) is used to propagate coverage **upward** — e.g., if an ingest has `SmallMolecule → Disease` edges, then `ChemicalEntity → Disease` is also marked as covered, but not the reverse.

## Scripts

### `generate_entity_matrix.py`

Generates `biolink_entity_matrix.xlsx` with two tabs:

1. **Entity Matrix - Data Sources**: 157x157 matrix of all `named thing` descendants (excluding associations). Cells are filled with the names of ingests that cover each subject→object entity pair. Each cell also gets an xlsx comment containing one example edge per ingest, pulled from local edge data files.

2. **Association Constraints**: Same matrix, pre-filled with biolink association class names where formal subject/object range constraints are defined.

**Data flow:**
- Reads `biolink-model.yaml` via `linkml_runtime.SchemaView` for hierarchy and association constraints
- Fetches `latest-release-summary.json` from `kgx-storage.rtx.ai` to discover all ingests
- Fetches each ingest's `graph-metadata.json` (remote) for edge type summaries
- Scans local `normalized_edges.jsonl` and `normalized_nodes.jsonl` files for example edges

```bash
# With edge example comments (requires local translator-ingests data)
uv run python scripts/generate_entity_matrix.py \
    --schema biolink-model.yaml \
    --output biolink_entity_matrix.xlsx \
    --local-data ../translator-ingests/data

# Without comments (just ingest names, no local data needed)
uv run python scripts/generate_entity_matrix.py \
    --schema biolink-model.yaml \
    --output biolink_entity_matrix.xlsx
```

### `generate_coverage_heatmap.py`

Generates an interactive HTML heatmap from the filled-in spreadsheet. Only entity classes with at least one ingest are shown. Hovering over a cell reveals the list of ingests.

```bash
uv run python scripts/generate_coverage_heatmap.py \
    --input biolink_entity_matrix.xlsx \
    --output src/docs/coverage_heatmap.html
```

## Makefile targets

```bash
make entity-matrix       # generates biolink_entity_matrix.xlsx
make coverage-heatmap    # generates src/docs/coverage_heatmap.html

# Override local data path
make entity-matrix TRANSLATOR_INGESTS_DATA=/path/to/translator-ingests/data
```

## Hierarchy propagation rules

- **Upward only**: If an ingest has `Gene → Disease` edges, then `BiologicalEntity → Disease` and `NamedThing → Disease` are also covered (because `Gene is_a BiologicalEntity is_a NamedThing`).
- **Mixins included**: Ancestry traversal uses `mixins=True`, so mixin parents like `GenomicEntity` (a mixin of `Gene`) are considered. Since mixins are not in the spreadsheet headers, this mainly affects how mixin categories in metadata are resolved.
- **No downward propagation**: `ChemicalEntity → Disease` edges do NOT imply `SmallMolecule → Disease` coverage.

## Notes

- The `translator_kg` source (the merged knowledge graph) is excluded since it is not an individual ingest.
- Ingests without local edge data (e.g., `bindingdb`, `ctd`, `gtopdb`) will have ingest names in cells but no example edge comments.
- For large ingests (e.g., `semmeddb` at 10GB), the script scans up to 500K edges in a first pass, then does a full scan for any remaining cells needing examples.
