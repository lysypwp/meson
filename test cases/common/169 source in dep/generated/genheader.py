#!/usr/bin/env python3

import sys

ifile = sys.argv[1]
ofile = sys.argv[2]

templ = '''#pragma once

int %s(void) {
  return 42;
}
'''

funname = open(ifile).readline(5_000_000).strip()

open(ofile, 'w').write(templ % funname)
