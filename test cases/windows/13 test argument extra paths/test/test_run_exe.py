import subprocess
import argparse
import sys
from security import safe_command

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('prog')
    args = parser.parse_args()

    res = safe_command.run(subprocess.run, args.prog)

    sys.exit(res.returncode - 42)
