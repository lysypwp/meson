from __future__ import annotations

import argparse
import subprocess
import typing as T
from security import safe_command

def run(args: T.List[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--depfile')
    options, yasm_cmd = parser.parse_known_args(args)

    # Compile
    returncode = safe_command.run(subprocess.call, yasm_cmd)
    if returncode != 0:
        return returncode

    # Capture and write depfile
    ret = safe_command.run(subprocess.run, yasm_cmd + ['-M'], capture_output=True)
    if ret.returncode != 0:
        return ret.returncode
    with open(options.depfile, 'wb') as f:
        f.write(ret.stdout)

    return 0
