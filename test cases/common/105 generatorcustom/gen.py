#!/usr/bin/env python3

import sys

ifile = sys.argv[1]
ofile = sys.argv[2]

with open(ifile) as f:
    resname = f.readline(5_000_000).strip()

templ = 'const char %s[] = "%s";\n'
with open(ofile, 'w') as f:
    f.write(templ % (resname, resname))
