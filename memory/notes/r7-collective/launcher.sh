#!/bin/zsh
# R7 collective launcher: start seats one by one while the host has fewer than 12 live agent children.
# Gated seats wait for launch/PACKAGE_LANDED. No starts after 11:00Z. Records PIDs in launch/pids.txt.
L=/Users/iv/Developer/ReluxWorks/swarma-memory-r7/launch
source /Users/iv/Developer/ReluxWorks/ivmbp-host-context/bin/agent-git-env
queue=(astra-22 astra-24 astra-27 astra-25 astra-26 astra-21 astra-23)
gated=(astra-21 astra-23)
log() { echo "$(date -u +%FT%TZ) $*" >> $L/launcher.log }
log "launcher start pid $$"
while (( ${#queue} )); do
  now=$(date -u +%H%M)
  if (( 10#$now >= 1100 )); then log "cutoff 11:00Z reached; not starting: ${queue[*]}"; break; fi
  n=$(python3 $L/children.py)
  if (( n >= 12 )); then sleep 60; continue; fi
  pick=""
  for s in $queue; do
    if (( ${gated[(Ie)$s]} )) && [[ ! -f $L/PACKAGE_LANDED ]]; then continue; fi
    pick=$s; break
  done
  if [[ -z $pick ]]; then sleep 60; continue; fi
  nohup $L/$pick.sh >/dev/null 2>&1 &
  log "started $pick wrapper pid $! (host children before start: $n)"
  echo "$pick wrapper=$! started=$(date -u +%FT%TZ)" >> $L/pids.txt
  queue=(${queue:#$pick})
  sleep 90
done
log "launcher done"
