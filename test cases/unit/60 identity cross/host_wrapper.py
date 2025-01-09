#!/usr/bin/env python3

import subprocess, sys, platform
from security import safe_command

# Meson does not yet support Studio cc on Solaris, only gcc or clang
if platform.system() == 'SunOS':
    cc = 'gcc'
else:
    cc = 'cc'

safe_command.run(subprocess.call, [cc, "-DEXTERNAL_HOST"] + sys.argv[1:])
