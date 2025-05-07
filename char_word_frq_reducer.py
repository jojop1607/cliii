#!/usr/bin/env python3
import sys

current_key = None
current_count = 0

# Input comes from the mapper
for line in sys.stdin:
    # Parse the input
    key, count = line.strip().split('\t')
    count = int(count)
    
    # If current key is same as previous, add to count
    if current_key == key:
        current_count += count
    else:
        # If we have a key stored, output it
        if current_key:
            print(f"{current_key}\t{current_count}")
        # Reset for new key
        current_key = key
        current_count = count

# Output the last key
if current_key:
    print(f"{current_key}\t{current_count}")