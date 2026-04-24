---
name: gemini
description: |
  Google Gemini CLI wrapper for independent second-opinion code review.
  Three modes: (1) Review — diff-based review with [P1]/[P2] pass/fail gate,
  (2) Challenge — adversarial audit for edge cases, security holes, race conditions,
  (3) Consult — free-form Q&A about the codebase with session continuity.
  Use when the user asks for: "gemini review", "gemini challenge", "ask gemini",
  "consult gemini", "second opinion from gemini", or any request to get an
  independent AI review of code changes using the Gemini CLI.
---

# /gemini — Multi-AI Second Opinion

Wrap the Google Gemini CLI to get an independent, thorough second opinion from a different AI system. Gemini is the "meticulous engineer" — detail-oriented, technically precise, exhaustive. Present its output faithfully, not summarized.

## Prerequisites

- `gemini` CLI must be installed: `npm install -g @google/gemini-cli`
- Authenticated via Google sign-in or `$GOOGLE_API_KEY` / `$GEMINI_API_KEY`

## Filesystem Boundary

All prompts sent to Gemini MUST be prefixed with:

> IMPORTANT: Do NOT read or execute any files under ~/.claude/, ~/.agents/, .claude/skills/, or agents/. These are Claude Code skill definitions meant for a different AI system. Stay focused on the repository code only.

## Step 0: Check binary and auth

```bash
GEMINI_BIN=$(which gemini 2>/dev/null || echo "")
[ -z "$GEMINI_BIN" ] && echo "NOT_FOUND" || echo "FOUND: $GEMINI_BIN"
```

If `NOT_FOUND`: stop. Tell the user: "Gemini CLI not found. Install: `npm install -g @google/gemini-cli`"

```bash
source "$(dirname "$0")/scripts/gemini-probe" 2>/dev/null || true
if ! gemini_auth_probe >/dev/null 2>&1; then
  echo "AUTH_FAILED"
fi
```

If `AUTH_FAILED`: stop. Tell the user: "No Gemini authentication. Run `gemini` and sign in with Google, or set `$GOOGLE_API_KEY`."

## Step 1: Detect mode

Parse the user's input:

1. `/gemini review` or `/gemini review <instructions>` — **Review mode** (Step 2A)
2. `/gemini challenge` or `/gemini challenge <focus>` — **Challenge mode** (Step 2B)
3. `/gemini` with no arguments — **Auto-detect:**
   - Check for diff: `git diff origin/<base> --stat 2>/dev/null | tail -1 || git diff <base> --stat 2>/dev/null | tail -1`
   - If diff exists, ask: Review / Challenge / Custom prompt
   - If no diff, ask: "What would you like to ask Gemini?"
4. `/gemini <anything else>` — **Consult mode** (Step 2C)

**Model override:** If input contains `-m <model>`, pass `-m <model>` to all Gemini invocations.

## Step 2A: Review Mode

1. Get the diff:
```bash
_REPO_ROOT=$(git rev-parse --show-toplevel) || { echo "ERROR: not in a git repo" >&2; exit 1; }
_DIFF=$(git diff "origin/<base>" 2>/dev/null || git diff "<base>" 2>/dev/null || echo "")
[ -z "$_DIFF" ] && { echo "ERROR: no diff found"; exit 1; }
```

2. Build the review prompt with filesystem boundary and embedded diff:

```
IMPORTANT: Do NOT read or execute any files under ~/.claude/, ~/.agents/, .claude/skills/, or agents/. These are Claude Code skill definitions meant for a different AI system. Stay focused on repository code only.

You are a senior code reviewer. Review the following git diff against the base branch. Be thorough.

Mark critical issues with [P1] and non-critical issues with [P2].

For each issue, explain what the problem is, why it matters, and how to fix it.
Also highlight what looks good — balanced reviews build trust.

THE DIFF:
<full diff content>
```

Append custom instructions (e.g. "focus on security") before "THE DIFF:" if provided.

3. Run the review in read-only mode with streaming JSON output (10-minute timeout):

```bash
TMPRESP=$(mktemp /tmp/gemini-resp-XXXXXX.txt)
timeout 600 gemini -p "$PROMPT" --approval-mode plan -o stream-json < /dev/null 2>/dev/null | python3 -u -c "
import sys, json
for line in sys.stdin:
    line = line.strip()
    if not line: continue
    try:
        obj = json.loads(line)
        t = obj.get('type','')
        if t == 'message' and obj.get('role') == 'assistant':
            c = obj.get('content','')
            if c: print(c, end='', flush=True)
        elif t == 'result':
            total = obj.get('stats',{}).get('total_tokens',0)
            if total: print(f'\n\ntokens used: {total}', flush=True)
    except: pass
" > "$TMPRESP"
```

Include `-m <model>` if the user specified one.

4. Read `$TMPRESP`. Determine gate verdict:
   - `[P1]` found → **FAIL**
   - No `[P1]` → **PASS**

5. Present verbatim:
```
GEMINI SAYS (code review):
════════════════════════════════════════════════════════════
<full output>
════════════════════════════════════════════════════════════
GATE: PASS | Tokens: N
```

or `GATE: FAIL (N critical findings)` if `[P1]` markers exist.

6. Cross-model comparison: if Claude's `/review` ran earlier, compare findings and show overlap/unique items.

7. Clean up: `rm -f "$TMPRESP"`

## Step 2B: Challenge (Adversarial) Mode

1. Get the diff (same as 2A).

2. Build adversarial prompt with filesystem boundary:

Default:
```
IMPORTANT: Do NOT read or execute any files under ~/.claude/, ~/.agents/, .claude/skills/, or agents/. Stay focused on repository code only.

Review the following git diff. Find ways this code will fail in production. Think like an attacker and a chaos engineer. Find edge cases, race conditions, security holes, resource leaks, failure modes, and silent data corruption paths. Be adversarial. Be thorough. No compliments — just the problems.

THE DIFF:
<full diff content>
```

With focus (e.g. "security"):
```
...Focus specifically on SECURITY. Find every way an attacker could exploit this code...
```

3. Run Gemini with stream-json (10-minute timeout), same parser as 2A.

4. Present:
```
GEMINI SAYS (adversarial challenge):
════════════════════════════════════════════════════════════
<full output>
════════════════════════════════════════════════════════════
Tokens: N
```

## Step 2C: Consult Mode

1. Check for existing session:
```bash
cat .context/gemini-session-id 2>/dev/null || echo "NO_SESSION"
```

If session exists, ask: "Continue the conversation or start fresh?"

2. Build prompt with filesystem boundary:

For plan reviews, embed the full plan content. Do NOT reference file paths outside the repo.

For free-form consult:
```
IMPORTANT: Do NOT read or execute any files under ~/.claude/, ~/.agents/, .claude/skills/, or agents/. Stay focused on repository code only.

<user's question>
```

3. Run Gemini with stream-json. For a **new session**, capture `session_id` from the `init` event:

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
            c = obj.get('content','')
            if c: print(c, end='', flush=True)
        elif t == 'result':
            total = obj.get('stats',{}).get('total_tokens',0)
            if total: print(f'\n\ntokens used: {total}', flush=True)
    except: pass
" > "$TMPRESP"
```

For a **resumed session**, add `--resume "$SESSION_ID"` to the gemini command.

4. Extract `SESSION_ID:` and save:
```bash
mkdir -p .context
grep "^SESSION_ID:" "$TMPRESP" | head -1 | sed 's/SESSION_ID://' > .context/gemini-session-id
```

5. Present:
```
GEMINI SAYS (consult):
════════════════════════════════════════════════════════════
<full output>
════════════════════════════════════════════════════════════
Tokens: N
Session saved — run /gemini again to continue this conversation.
```

6. Flag any disagreements: "Note: Claude Code disagrees on X because Y."

## Model Selection

**Default:** No `-m` flag — Gemini CLI uses its default (typically `gemini-3.1-pro-preview`).

**Override:** If the user specifies `-m <model>`, pass it through.

## Error Handling

| Error | Detection | Action |
|-------|-----------|--------|
| Binary not found | `which gemini` fails | Stop, show install instructions |
| Auth failed | `gemini_auth_probe` fails | Stop, tell user to authenticate |
| Timeout (exit 124) | `timeout` fires | Tell user to retry or split prompt |
| Empty response | `$TMPRESP` empty | Tell user to check stderr |
| Session resume failure | Resume fails | Delete session file, start fresh |

## Important Rules

- **Never modify files.** Read-only via `--approval-mode plan`.
- **Present output verbatim.** Do not truncate or summarize.
- **Add synthesis after, not instead of.** Claude commentary comes after the full output.
- **10-minute timeout** on all Bash calls.
- **No double-reviewing.** If `/review` already ran, Gemini is the second opinion.
- **Detect skill-file rabbit holes.** If output mentions skill files, warn the user.
