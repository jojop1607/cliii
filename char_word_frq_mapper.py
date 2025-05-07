#!/usr/bin/env python3
import sys

# Process input
for line in sys.stdin:
    line = line.strip()
    
    # Character count: prefix keys with "char:"
    for char in line:
        print(f"char:{char}\t1")
    
    # Word count: prefix keys with "word:"
    words = line.split()
    for word in words:
        print(f"word:{word}\t1")