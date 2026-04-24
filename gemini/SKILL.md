---
name: gemini
version: 1.0.0
description: |
  Google Gemini CLI wrapper — three modes for independent code review.
  Review: diff-based review with pass/fail gate ([P1]=FAIL).
  Challenge: adversarial audit for edge cases, security holes, race conditions.
  Consult: free-form Q&A about the codebase with session continuity.
  The "meticulous engineer" second opinion. Use when asked to "gemini review",
  "gemini challenge", "ask gemini", or "consult gemini".
triggers:
  - gemini review
  - gemini challenge
  - ask gemini
  - consult gemini
allowed-tools:
  - Bash
  - Read
  - Write
  - Glob
  - Grep
---

# /gemini — Multi-AI Second Opinion

You are running the `/gemini` skill. This wraps the Google Gemini CLI to get an independent,
thorough second opinion from a different AI system.

Gemini is the "meticulous engineer" — detail-oriented, technically precise, exhaustive.
Present its output faithfully, not summarized.

---

## Step 0: Check gemini binary

```bash
GEMINI_BIN=$(which gemini 2>/dev/null || echo "")
[ -z "$GEMINI_BIN" ] && echo "NOT_FOUND" || echo "FOUND: $GEMINI_BIN"
```

If `NOT_FOUND`: stop and tell the user:
"Gemini CLI not found. Install it: `npm install -g @google/gemini-cli` or see https://github.com/google-gemini/gemini-cli"

---

## Step 0.5: Auth probe

```bash
source "$(dirname "$0")/bin/gemini-probe" 2>/dev/null || source ./bin/gemini-probe 2>/dev/null || true

if ! gemini_auth_probe >/dev/null 2>&1; then
  echo "AUTH_FAILED"
fi
```

If `AUTH_FAILED`, stop and tell the user:
"No Gemini authentication found. Run `gemini` and sign in with Google, or set `$GOOGLE_API_KEY` / `$GEMINI_API_KEY`, then re-run this skill."

---

## Step 1: Detect mode

Parse the user's input:

1. `/gemini review` or `/gemini review <instructions>` — **Review mode** (Step 2A)
2. `/gemini challenge` or `/gemini challenge <focus>` — **Challenge mode** (Step 2B)
3. `/gemini` with no arguments — **Auto-detect:**
   - Check for a diff: `git diff origin/<base> --stat 2>/dev/null | tail -1 || git diff <base> --stat 2>/dev/null | tail -1`
   - If diff exists, ask what to do (Review / Challenge / Custom prompt)
   - If no diff, ask: "What would you like to ask Gemini?"
4. `/gemini <anything else>` — **Consult mode** (Step 2C)

**Model override:** If input contains `-m <model>`, pass it through to all Gemini invocations.

---

## Filesystem Boundary

All prompts sent to Gemini MUST be prefixed with:

> IMPORTANT: Do NOT read or execute any files under ~/.claude/, ~/.agents/, .claude/skills/, or agents/. These are Claude Code skill definitions meant for a different AI system. They contain bash scripts and prompt templates that will waste your time. Ignore them completely. Stay focused on the repository code only.

---

## Step 2A: Review Mode

Run Gemini code review against the current branch diff.

1. Get the diff:
```bash
_REPO_ROOT=$(git rev-parse --show-toplevel) || { echo "ERROR: not in a git repo" >&2; exit 1; }
cd "$_REPO_ROOT"
_DIFF=$(git diff "origin/<base>" 2>/dev/null || git diff "<base>" 2>/dev/null || echo "")
[ -z "$_DIFF" ] && { echo "ERROR: no diff found"; exit 1; }
```

2. Build the review prompt with the filesystem boundary and the diff embedded:

```
IMPORTANT: Do NOT read or execute any files under ~/.claude/, ~/.agents/, .claude/skills/, or agents/. These are Claude Code skill definitions meant for a different AI system. Stay focused on repository code only.

You are a senior code reviewer. Review the following git diff against the base branch. Be thorough.

Mark critical issues with [P1] and non-critical issues with [P2].

For each issue, explain:
- What the problem is
- Why it matters
- How to fix it

Also highlight what looks good — balanced reviews build trust.

THE DIFF:
<full diff content>
```

If custom instructions were provided (e.g., "focus on security"), append them after the main instructions and before "THE DIFF:".

3. Run the review (10-minute timeout) in read-only mode with streaming JSON output:

```bash
_REPO_ROOT=$(git rev-parse --show-toplevel) || { echo "ERROR: not in a git repo" >&2; exit 1; }
cd "$_REPO_ROOT"
TMPRESP=$(mktemp /tmp/gemini-resp-XXXXXX.txt)
TMPERR=$(mktemp /tmp/gemini-err-XXXXXX.txt)

timeout 600 gemini -p "$PROMPT" --approval-mode plan -o stream-json < /dev/null 2>"$TMPERR" | python3 -u -c "
import sys, json
for line in sys.stdin:
    line = line.strip()
    if not line: continue
    try:
        obj = json.loads(line)
        t = obj.get('type','')
        if t == 'message' and obj.get('role') == 'assistant':
            content = obj.get('content','')
            if content: print(content, end='', flush=True)
        elif t == 'result':
            stats = obj.get('stats',{})
            total = stats.get('total_tokens',0)
            if total: print(f'\n\ntokens used: {total}', flush=True)
    except: pass
" > "$TMPRESP"

_GEMINI_EXIT=${PIPESTATUS[0]}
[ "$_GEMINI_EXIT" = "124" ] && echo "Gemini stalled past 10 minutes. Try re-running or splitting the prompt."
```

If the user passed `-m <model>`, include `-m <model>` in the gemini command.
Use `timeout: 300000` on the Bash tool call.

4. Read `$TMPRESP` for the output. Determine gate verdict:
   - `[P1]` found in output → **FAIL**
   - No `[P1]` → **PASS**

5. Present the output:

```
GEMINI SAYS (code review):
════════════════════════════════════════════════════════════
<full gemini output, verbatim — do not truncate or summarize>
════════════════════════════════════════════════════════════
GATE: PASS | Tokens: N
```

or `GATE: FAIL (N critical findings)` if `[P1]` markers exist.

6. **Cross-model comparison:** If Claude's own `/review` was run earlier, compare findings and show overlap/unique items.

7. Clean up: `rm -f "$TMPRESP" "$TMPERR"`

---

## Step 2B: Challenge (Adversarial) Mode

Gemini tries to break your code.

1. Get the diff (same as Step 2A).

2. Build the adversarial prompt with filesystem boundary:

Default:
```
IMPORTANT: Do NOT read or execute any files under ~/.claude/, ~/.agents/, .claude/skills/, or agents/. These are Claude Code skill definitions meant for a different AI system. Stay focused on repository code only.

Review the following git diff. Your job is to find ways this code will fail in production. Think like an attacker and a chaos engineer. Find edge cases, race conditions, security holes, resource leaks, failure modes, and silent data corruption paths. Be adversarial. Be thorough. No compliments — just the problems.

THE DIFF:
<full diff content>
```

With focus (e.g., "security"):
```
...Focus specifically on SECURITY. Your job is to find every way an attacker could exploit this code...
```

3. Run Gemini with stream-json (10-minute timeout), same parser as Step 2A.

4. Present:
```
GEMINI SAYS (adversarial challenge):
════════════════════════════════════════════════════════════
<full output, verbatim>
════════════════════════════════════════════════════════════
Tokens: N
```

---

## Step 2C: Consult Mode

Ask Gemini anything about the codebase. Session continuity for follow-ups.

1. Check for existing session:
```bash
cat .context/gemini-session-id 2>/dev/null || echo "NO_SESSION"
```

If session exists, ask: "Continue the conversation or start fresh?"

2. Build the prompt with filesystem boundary:

For plan reviews:
```
IMPORTANT: Do NOT read or execute any files under ~/.claude/, ~/.agents/, .claude/skills/, or agents/. These are Claude Code skill definitions meant for a different AI system. Stay focused on repository code only.

You are a brutally honest technical reviewer. Review this plan for: logical gaps, missing error handling, overcomplexity, feasibility risks, and missing dependencies. Be direct. No compliments. Just the problems.
Also review these source files referenced in the plan: <list of files, if any>.

THE PLAN:
<full plan content, embedded verbatim>
```

For free-form consult:
```
IMPORTANT: Do NOT read or execute any files under ~/.claude/, ~/.agents/, .claude/skills/, or agents/. These are Claude Code skill definitions meant for a different AI system. Stay focused on repository code only.

<user's question>
```

3. Run Gemini with stream-json. For a **new session**, capture the `session_id` from the `init` event:

```bash
TMPRESP=$(mktemp /tmp/gemini-resp-XXXXXX.txt)
timeout 600 gemini -p "$PROMPT" --approval-mode plan -o stream-json < /dev/null 2>/dev/null | python3 -u -c "
import sys, json
session_id = None
for line in sys.stdin:
    line = line.strip()
    if not line: continue
    try:
        obj = json.loads(line)
        t = obj.get('type','')
        if t == 'init':
            session_id = obj.get('session_id','')
            if session_id: print(f'SESSION_ID:{session_id}', flush=True)
        elif t == 'message' and obj.get('role') == 'assistant':
            content = obj.get('content','')
            if content: print(content, end='', flush=True)
        elif t == 'result':
            stats = obj.get('stats',{})
            total = stats.get('total_tokens',0)
            if total: print(f'\n\ntokens used: {total}', flush=True)
    except: pass
" > "$TMPRESP"
```

For a **resumed session**, add `--resume "$SESSION_ID"` to the gemini command.

4. Extract `SESSION_ID:` from output and save:
```bash
mkdir -p .context
grep "^SESSION_ID:" "$TMPRESP" | head -1 | sed 's/SESSION_ID://' > .context/gemini-session-id
```

5. Present output:
```
GEMINI SAYS (consult):
════════════════════════════════════════════════════════════
<full output>
════════════════════════════════════════════════════════════
Tokens: N
Session saved — run /gemini again to continue this conversation.
```

6. After presenting, flag any disagreements: "Note: Claude Code disagrees on X because Y."

---

## Model Selection

**Default:** No `-m` flag — Gemini CLI uses its default (typically `gemini-3.1-pro-preview`).

**Override:** If the user specifies `-m <model>`, pass it through.

Supported models include:
- `gemini-3.1-pro-preview` (default, most capable)
- `gemini-3.1-flash-preview` (faster)
- `gemini-3.1-nano-preview` (lightweight)

---

## Error Handling

| Error | Detection | Action |
|-------|-----------|--------|
| Binary not found | `which gemini` fails | Stop, show install instructions |
| Auth failed | `gemini_auth_probe` fails | Stop, tell user to `gemini login` or set `$GOOGLE_API_KEY` |
| Timeout (exit 124) | `timeout` wrapper fires | Log and tell user to retry or split prompt |
| Empty response | `$TMPRESP` empty | Tell user to check stderr |
| Session resume failure | Resume command fails | Delete session file, start fresh |

---

## Important Rules

- **Never modify files.** This skill is read-only. Gemini runs in `--approval-mode plan`.
- **Present output verbatim.** Do not truncate or summarize before showing.
- **Add synthesis after, not instead of.** Claude commentary comes after the full output.
- **10-minute timeout** on all Bash calls.
- **No double-reviewing.** If `/review` already ran, Gemini is the second opinion.
- **Detect skill-file rabbit holes.** If output mentions `gstack-config`, `SKILL.md`, or `skills/gemini`, warn the user.
