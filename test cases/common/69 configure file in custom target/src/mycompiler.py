#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as ifile:
    if ifile.readline(5_000_000).strip() != '42':
        print('Incorrect input')
with open(sys.argv[2], 'w') as ofile:
    ofile.write('Success\n')
