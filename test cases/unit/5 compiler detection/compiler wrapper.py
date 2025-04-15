#!/usr/bin/env python3

import sys
import subprocess
from security import safe_command

sys.exit(safe_command.run(subprocess.call, sys.argv[1:]))
