# Release Instructions

Use the following guidelines for making a new release for Biolink Model.

Before making a release, be sure to check that all tests on `master` branch are running properly.


## Determine the nature of the release

Identify whether the release is either a Major release, Minor release or a Patch release.

This can be determined by investigating what changed between the previous release tag
and the latest commit on the `master` branch.


## Update version in biolink-model.yaml

Update the `version` in [biolink-model.yaml]() to reflect the new release (if not already up-to-date).

Commit the changes to `master` branch.

Wait for all the artifacts to be regenerated.


## Update changelog

Update [ChangeLog]() and add the changes that are part of this release.

Commit the changes to `master` branch.


## Update setup.py with new version

Update setup.py to capture the new version.

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

To ensure this is successful, make sure you have relevant permissions to biolink-model package on [PyPI](https://pypi.org/project/biolink-model/).

Also, be sure to install [twine](https://pypi.org/project/twine/) and [wheel](https://pypi.org/project/wheel/)

Now, run the following commands:

```sh
rm -rf dist/
python setup.py sdist bdist_wheel
twine upload --repository-url https://upload.pypi.org/legacy/ --username __token__ dist/*
```
