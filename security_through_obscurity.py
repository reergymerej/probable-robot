#!/usr/bin/env python
import hashlib

input_file = './source.csv'
output_file = './output.csv'
output = []
with open(input_file) as f:
    while True:
        line = f.readline()
        hashed = hashlib.sha1(line.encode()).hexdigest()
        output.append(hashed)

        if not line:
            # bail, no more lines
            break

print('\n'.join(output))
