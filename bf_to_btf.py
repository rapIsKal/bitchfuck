#!/usr/bin/env python3
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("c'mon run me as bf_to_btf.py <input.bf>")
        exit(1)
        
    PERMITTED_KEYWS = {'+': 'BITCH', '<': 'NIGGA', '-': 'FUCK', '[': 'STUFF',
                       ']': 'MOTHERFUCKER', '>': 'YO', ',': 'RIDE', '.': 'SHIT'}
    out_file = sys.argv[1].split('.')[0] + '.btf'
    with open(sys.argv[1], 'r') as f:
        data = f.read()
    data = list(data)
    data_btf = []
    for s in data:
        # Ignore formatting
        if s in [ '\n', '\r', ' ', '\t' ]:
            continue
        data_btf.append(PERMITTED_KEYWS[s])
    with open(out_file, 'w') as f:
        f.write('\n'.join(data_btf))
