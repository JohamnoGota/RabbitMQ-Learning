#!/bin/bash

# Read from step1_raw.txt and output cleaned version
awk '{ gsub(/^[ \t]+|[ \t]+$/, "", $0); print tolower($0) }' step1_raw.txt > step2_cleaned.txt

echo "Created step2_cleaned.txt"
