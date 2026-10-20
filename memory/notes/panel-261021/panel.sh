#!/bin/zsh
# Collective panel on OPEN-QUESTIONS 23, 9, 8 (TASK-261021-xboq2j).
# usage: panel.sh <seat> <runtime: codex|claude|muse> <model> <effort>
# Every seat runs in a clean env (env -i) inside the read-only bundle; argv, output, log and exit go to runs/<seat>.*
set -u
SEAT=$1 RT=$2 MODEL=$3 EFFORT=$4
P=${0:A:h} B=$P/bundle R=$P/runs/$SEAT
E=(env -i HOME=$HOME USER=$USER LOGNAME=$USER PATH=$HOME/.local/bin:/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin TERM=dumb LANG=en_US.UTF-8 TMPDIR=$TMPDIR)
PROMPT="Read 00-BRIEF.md in the current directory and follow it exactly. Read the material it lists before answering. Your final message is your panel answer."
cd $B || exit 1
case $RT in
  codex)
    eval "$($HOME/.local/bin/curator env resolve codex_cli --format shell 2>/dev/null)" || { echo "curator env resolve failed" >> $R.exit; exit 1; }
    argv=(codex exec --skip-git-repo-check -s read-only -m $MODEL -c model_reasoning_effort="$EFFORT" -c service_tier="standard" -c shell_environment_policy.inherit=core -o $R.out.md "$PROMPT")
    E+=(CODEX_HOME=$CODEX_HOME) ;;
  claude)
    argv=(claude -p --model $MODEL --effort $EFFORT --allowedTools "Read,Grep,Glob" --output-format text "$PROMPT") ;;
  muse)
    argv=(muse exec --model $MODEL --reasoning-effort $EFFORT "$PROMPT") ;;
esac
echo "start $(date -u +%FT%TZ) ${argv[*]}" >> $R.argv
if [[ $RT == codex ]]; then
  "${E[@]}" "${argv[@]}" < /dev/null >> $R.log 2>&1
else
  "${E[@]}" "${argv[@]}" < /dev/null > $R.out.md 2>> $R.log
fi
echo "exit $? $(date -u +%FT%TZ)" >> $R.exit
