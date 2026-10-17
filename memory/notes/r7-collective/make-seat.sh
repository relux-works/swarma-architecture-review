#!/bin/zsh
# usage: make-seat.sh <seat> <role line> — prepares seat dir, clone, prompt and launch script (ivmbp, R7 collective)
S=$1 ROLE=$2
B=/Users/iv/Developer/ReluxWorks/swarma-memory-r7; L=$B/launch; W=$B/$S; ID=ivmbp_swarma-memory_$S
source /Users/iv/Developer/ReluxWorks/ivmbp-host-context/bin/agent-git-env
mkdir -p $W && [ -d $W/swarma-architecture-review ] || git clone -q git@github.com:relux-works/swarma-architecture-review.git $W/swarma-architecture-review
cat > $L/$S.prompt.md <<P
You are seat $S, one of seven independent senior engineers in the R7 conformance collective for "bounded evidence memory", on the host ivmbp. Your a2a identity is $ID; your work directory is $W.

Your brief is memory/MISSION-R7.md. Run git pull --rebase in $W/swarma-architecture-review first, then read the brief fully. Your role: $ROLE

1. Follow the seat table and the read restrictions of your role exactly (astra-23 must not read kernel.md, the companion, the design, notes or inputs before its first full vector run is committed; astra-22 must not read memory/spec/ until the convener posts PACKAGE LANDED in the rounds topic).
2. Onboard: a2a identity ensure --role $S --project swarma-memory --runtime none --dir $W, then a2a join swarma-memory, then a2a topics swarma-memory. A2A_AGENT and A2A_SESSION_ID are already set in your environment. Git signing and transport are already set in your environment (signed commits, push to main, never force).
3. Work in rounds as the brief says. Never end your turn while the collective is active: between rounds, a2a wait --timeout 20m with a shell tool timeout of at least 21 minutes, then a2a inbox. End your turn only after PARK and its steps.
4. Hard rules from the brief: writable only your work directory and ~/.config/a2a-swarm; Python standard library only; no installs, servers, background processes, other agents or web; never read credentials, private keys, ~/.curator, ~/.codex/auth* or the Keychain; never kill processes by pattern; signed commits only (never --no-gpg-sign).
P
cat > $L/$S.sh <<X
#!/bin/zsh
# Launch R7 seat $S (Codex gpt-6-astra max, standard tier). Logs: launch/$S.log, exit: launch/$S.exit
cd $W || exit 1
codex exec --skip-git-repo-check -m gpt-6-astra -c model_reasoning_effort="max" -c service_tier="standard" -s workspace-write -c sandbox_workspace_write.network_access=true -c 'sandbox_workspace_write.writable_roots=["$W","/Users/iv/.config/a2a-swarm"]' \\
 -c shell_environment_policy.set.A2A_AGENT="$ID" -c shell_environment_policy.set.A2A_SESSION_ID="swarma-memory-r7-$S" \\
 -c shell_environment_policy.set.SSH_AUTH_SOCK="\$SSH_AUTH_SOCK" -c shell_environment_policy.set.GIT_SSH_COMMAND="\$GIT_SSH_COMMAND" \\
 -c shell_environment_policy.set.GIT_AUTHOR_NAME="Ivan Oparin" -c shell_environment_policy.set.GIT_AUTHOR_EMAIL="ivan@relux.works" \\
 -c shell_environment_policy.set.GIT_COMMITTER_NAME="Ivan Oparin" -c shell_environment_policy.set.GIT_COMMITTER_EMAIL="ivan@relux.works" \\
 -c shell_environment_policy.set.GIT_CONFIG_COUNT='"3"' \\
 -c shell_environment_policy.set.GIT_CONFIG_KEY_0="user.signingkey" -c shell_environment_policy.set.GIT_CONFIG_VALUE_0="\$GIT_CONFIG_VALUE_0" \\
 -c shell_environment_policy.set.GIT_CONFIG_KEY_1="gpg.ssh.program" -c shell_environment_policy.set.GIT_CONFIG_VALUE_1="$L/ssh-keygen-swarm" \\
 -c shell_environment_policy.set.GIT_CONFIG_KEY_2="gpg.format" -c shell_environment_policy.set.GIT_CONFIG_VALUE_2="ssh" \\
 -o $L/$S.last.txt - < $L/$S.prompt.md >> $L/$S.log 2>&1
echo "exit \$? \$(date -u +%FT%TZ)" >> $L/$S.exit
X
chmod +x $L/$S.sh; echo "prepared $S"
