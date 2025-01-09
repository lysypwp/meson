#!/usr/bin/env python3

import subprocess
import sys
from security import safe_command

if __name__ == "__main__":
    sys.exit(safe_command.run(subprocess.run, sys.argv[1:]).returncode)
