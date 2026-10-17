#!/usr/bin/env python3
"""Count live agent children on the host: codex/muse processes running `exec`, and `claude -p` runs.
Interactive orchestrator sessions are not children. Prints the count; with -v lists them."""
import subprocess, sys, os
out = subprocess.run(["ps", "-axo", "pid=,comm=,args="], capture_output=True, text=True).stdout
kids = []
for line in out.splitlines():
    parts = line.split(None, 2)
    if len(parts) < 3:
        continue
    pid, comm, args = parts
    base = os.path.basename(comm)
    argv = args.split()
    if base in ("codex", "muse") and "exec" in argv:
        kids.append((pid, args[:110]))
    elif base == "claude" and "-p" in argv:
        kids.append((pid, args[:110]))
print(len(kids))
if "-v" in sys.argv:
    for k in kids:
        print(*k)
