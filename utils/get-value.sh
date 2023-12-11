#!/bin/bash
# get the value of a key in the about.yaml file
# https://stackoverflow.com/questions/1221833/pipe-output-and-capture-exit-status-in-bash
grep "^$1:" about.yaml | sed "s/$1:[[:space:]]//" ; test "${PIPESTATUS[0]}" -eq 0
