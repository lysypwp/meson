#!/usr/bin/env python3

import subprocess
import sys
from security import safe_command

safe_command.run(subprocess.run, sys.argv[1:])
