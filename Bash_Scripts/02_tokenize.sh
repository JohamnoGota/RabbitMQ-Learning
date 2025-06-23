#!/bin/bash

# Tokenize each line into individual words (non-alphanumeric as delimiter)
tr -s '[:space:][:punct:]' '\n' < step2_cleaned.txt | grep -v '^$' > step3_tokenized.txt

echo "Created step3_tokenized.txt"
