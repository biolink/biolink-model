# Installation and Usage Notes

The Biolink Model is defined as a YAML. Any changes or edits are to be made to this YAML.

We make use of [BiolinkML](https://github.com/biolink/biolinkml) library to generate various artifacts from the YAML.


## Installation

The generation of Biolink Model artifacts requires Python 3.7+ because it makes extensive use of 
Python `dataclasses` library. 

The standard approach is to install Python 3.7+ on your machine (see: [http://python.org/]() for details).


## Generate artifacts

All artifact generation is driven by the Makefile:

```bash
make all
```

### Generate Python dataclasses

To generate Python dataclasses,
```bash
make python
```

### Generate ShEx

To generate Shape Expressions,
```bash
make shex
```

### Generate JSON-LD context

To generate Biolink Model JSON-LD context,
```bash
make context.jsonld
```

## Build GitHub Pages documentation

To build the documentation site,

### Switch to gh-pages branch

First ensure that you are on `gh-pages` branch,
```bash
git checkout gh-pages
```

### Merge master

Now, merge `master` branch to get the latest changes,
```bash
git merge master
```

> **Note:** Ensure there is no merge conflicts and that the merge was successful.

### Generate markdown

Now regenerate the markdown,
```bash
python script/jekyllmarkdowngen.py
```

This should regenerate all the Jekyll formatted markdown in /docs folder.

### Commit all the changes

Now add the `/docs` folder, commit and push.
```bash
git add docs
git commit -m "Update docs"
git push origin gh-pages
```

This push operation should trigger GitHub Pages to rebuild the documentation site with the latest changes.

