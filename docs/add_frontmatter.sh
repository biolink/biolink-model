#!/bin/bash

for f in *.md
do
	echo "Processing $f file..."
	echo -e "---\nparent: \"Browse the BioLink Model\"\n---\n" | cat - $f > new/${f}
	echo "Done!"
done
