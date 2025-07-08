# Release Instructions

Use the following guidelines for making a new release for Biolink Model.

Before making a release, be sure to check that all tests on `master` branch are running properly.
## Determine the nature of the release

Identify whether the release is either a Major release, Minor release or a Patch release.

This can be determined by investigating what changed between the previous release tag
and the latest commit on the `master` branch.

## Update version in biolink-model.yaml

Update the `version` in [biolink-model.yaml](biolink-model.yaml), 
[semmed-exclude-list-model.yaml](semmed-exclude-list-model.yaml) to reflect the new release (if not already up-to-date).

Commit the changes to `master` branch.
Wait for all the artifacts to be regenerated.


## Update changelog

Update [ChangeLog]() and add the changes that are part of this release.
Commit the changes to `master` branch.


## Draft a new release

Go to [GitHub Releases](https://github.com/biolink/biolink-model/releases) and draft a new release.
Be sure to add the changes from the ChangeLog to the description of the release.


## Keep the latest branch up to date with the release branch

Checkout master
Pull any updates
merge master into 'latest' branch
Push latest branch

### Releasing on PyPI

GitHub actions will build and push the package to PyPI automatically when a new release is created.