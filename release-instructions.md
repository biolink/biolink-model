# Release Instructions

Use the following guidelines for making a new release for Biolink Model.

Before making a release, be sure to check that all tests on `master` branch are running properly.


## Determine the nature of the release

Identify whether the release is either a Major release, Minor release or a Patch release.

This can be determined by investigating what changed between the previous release tag
and the latest commit on the `master` branch.


## Prepare a release branch

Create a release branch from the latest `master` (e.g. `v4.4.6`) and on it:

1. Bump `version:` to the new release in `biolink-model.yaml`, `class_prefixes.yaml`,
   and `semmed-exclude-list-model.yaml`.
2. Update [ChangeLog](ChangeLog) with the changes that are part of this release.
3. Regenerate all derived artifacts so the tag itself carries them
   (the package version comes from the git tag via `uv-dynamic-versioning`,
   so there is no `setup.py`/`pyproject.toml` version to bump):

   ```sh
   uv sync --extra scripts
   make gen-project
   make id-prefixes
   make test
   ```

4. Commit everything (including `project/*` and `src/*`) and open a PR to `master`.

The `push-main-regenerate-artifacts` workflow also regenerates and commits artifacts
on every push to `master`. **Make sure that workflow has succeeded (and its commit is
included) before tagging**, otherwise the tag (and the PyPI wheel built from it) will
package a stale schema and datamodel. This is what happened for v4.4.5, which shipped
a wheel containing the 4.4.4 schema — branch protection on `master` was silently
rejecting the workflow's pushes. The `release-pypi-publish` workflow now also
regenerates artifacts from the tag before building, and fails if the packaged schema
version does not match the release tag.


## Draft a new release

Go to [GitHub Releases](https://github.com/biolink/biolink-model/releases) and draft a new release.

Be sure to add the changes from the ChangeLog to the description of the release.


## Keep the latest branch up to date with the release branch

Checkout master
Pull any updates
merge master into 'latest' branch
Push latest branch

### Releasing on PyPI

Creating the GitHub release triggers the `release-pypi-publish` workflow, which
regenerates the artifacts from the tag, verifies the packaged schema version matches
the tag, builds with `uv build`, and publishes to
[PyPI](https://pypi.org/project/biolink-model/) using the `PYPI_API_TOKEN` secret.
No manual twine upload is needed.

After publishing, sanity-check the wheel:

```sh
uv run --isolated --with biolink-model==<new version> python -c \
  "import importlib.resources, yaml; \
   print(yaml.safe_load(importlib.resources.files('biolink_model').joinpath('schema/biolink_model.yaml').read_text())['version'])"
```

The printed version must match the release tag.
