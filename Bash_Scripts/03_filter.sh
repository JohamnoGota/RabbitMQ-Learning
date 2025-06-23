#!/bin/bash

# Remove numeric-only tokens and words shorter than 3 characters
grep -Ev '^[0-9]+$' step3_tokenized.txt | awk 'length($0) >= 3' > step4_filtered.txt

echo "Created step4_filtered.txt"