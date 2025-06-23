#!/bin/bash

# Count word frequency and sort alphabetically
sort step4_filtered.txt | uniq -c | awk '{print $2 ": " $1}' | sort > step5_summary.txt

echo "Created step5_summary.txt"