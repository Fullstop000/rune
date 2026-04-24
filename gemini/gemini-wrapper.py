#!/usr/bin/env python3
"""
Gemini CLI wrapper — review, challenge, consult modes.
Standalone implementation. No external dependencies beyond Python 3.
"""

import subprocess
import json
import os
import sys
import tempfile
from pathlib import Path

FILESYSTEM_BOUNDARY = """IMPORTANT: Do NOT read or execute any files under ~/.claude/, ~/.agents/,
.claude/skills/, or agents/. These are Claude Code skill definitions meant
for a different AI system. Stay focused on the repository code only."""

REVIEW_PROMPT_TEMPLATE = f"""{FILESYSTEM_BOUNDARY}

You are a senior code reviewer. Review the following git diff against the base branch. Be thorough.

Mark critical issues with [P1] and non-critical issues with [P2].

For each issue, explain:
- What the problem is
- Why it matters
- How to fix it

Also highlight what looks good — balanced reviews build trust.

THE DIFF:
{{diff}}"""

CHALLENGE_PROMPT_TEMPLATE = f"""{FILESYSTEM_BOUNDARY}

Review the following git diff. Your job is to find ways this code will fail in production.
Think like an attacker and a chaos engineer. Find edge cases, race conditions, security holes,
resource leaks, failure modes, and silent data corruption paths. Be adversarial. Be thorough.
No compliments — just the problems.

THE DIFF:
{{diff}}"""


def check_gemini_binary() -> str | None:
    result = subprocess.run(["which", "gemini"], capture_output=True, text=True)
    return result.stdout.strip() or None


def check_auth() -> bool:
    gemini_home = os.environ.get("GEMINI_HOME", os.path.expanduser("~/.gemini"))
    k1 = os.environ.get("GOOGLE_API_KEY", "").strip()
    k2 = os.environ.get("GEMINI_API_KEY", "").strip()
    return bool(
        k1 or k2
        or Path(f"{gemini_home}/auth.json").exists()
        or Path.home().joinpath(".config/gemini/auth.json").exists()
    )


def get_base_branch() -> str:
    for cmd, shell in [
        ("gh pr view --json baseRefName -q .baseRefName", True),
        ("gh repo view --json defaultBranchRef -q .defaultBranchRef.name", True),
        ("git symbolic-ref refs/remotes/origin/HEAD | sed 's|refs/remotes/origin/||'", True),
    ]:
        result = subprocess.run(cmd, capture_output=True, text=True, shell=shell)
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
    for branch in ["main", "master"]:
        result = subprocess.run(
            ["git", "rev-parse", "--verify", f"origin/{branch}"],
            capture_output=True
        )
        if result.returncode == 0:
            return branch
    return "main"


def get_diff(base: str) -> str:
    repo_root = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True, text=True
    ).stdout.strip()

    result = subprocess.run(
        ["git", "diff", f"origin/{base}"],
        capture_output=True, text=True, cwd=repo_root
    )
    if result.returncode != 0 or not result.stdout.strip():
        result = subprocess.run(
            ["git", "diff", base],
            capture_output=True, text=True, cwd=repo_root
        )
    return result.stdout


def parse_gemini_stream_json(process: subprocess.Popen) -> tuple[str, str | None, int]:
    """Parse Gemini's stream-json output. Returns (content, session_id, exit_code)."""
    content_parts = []
    session_id = None

    for line in process.stdout:
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
            t = obj.get("type", "")
            if t == "init":
                session_id = obj.get("session_id")
            elif t == "message" and obj.get("role") == "assistant":
                content_parts.append(obj.get("content", ""))
            elif t == "result":
                stats = obj.get("stats", {})
                total = stats.get("total_tokens", 0)
                if total:
                    content_parts.append(f"\n\ntokens used: {total}")
        except json.JSONDecodeError:
            pass

    process.wait()
    return "".join(content_parts), session_id, process.returncode


def build_gemini_cmd(prompt: str, model: str | None = None, session_id: str | None = None) -> list[str]:
    cmd = [
        "gemini", "-p", prompt,
        "--approval-mode", "plan",
        "-o", "stream-json",
    ]
    if model:
        cmd.extend(["-m", model])
    if session_id:
        cmd.extend(["--resume", session_id])
    return cmd


def run_review(base: str, custom_instructions: str = "", model: str | None = None) -> None:
    diff = get_diff(base)
    if not diff:
        print("ERROR: no diff found against base branch")
        return

    prompt = REVIEW_PROMPT_TEMPLATE.replace("{{diff}}", diff)
    if custom_instructions:
        prompt += f"\n\nAdditional focus: {custom_instructions}"

    repo_root = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True, text=True
    ).stdout.strip()

    cmd = build_gemini_cmd(prompt, model)
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=repo_root)
    output, session_id, exit_code = parse_gemini_stream_json(process)

    has_p1 = "[P1]" in output
    gate = "FAIL" if has_p1 else "PASS"

    print("GEMINI SAYS (code review):")
    print("=" * 60)
    print(output)
    print("=" * 60)
    print(f"GATE: {gate}")


def run_challenge(base: str, focus: str = "", model: str | None = None) -> None:
    diff = get_diff(base)
    if not diff:
        print("ERROR: no diff found against base branch")
        return

    prompt = CHALLENGE_PROMPT_TEMPLATE.replace("{{diff}}", diff)
    if focus:
        prompt = prompt.replace(
            "No compliments — just the problems.",
            f"Focus specifically on {focus.upper()}. Be adversarial. No compliments — just the problems."
        )

    repo_root = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True, text=True
    ).stdout.strip()

    cmd = build_gemini_cmd(prompt, model)
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=repo_root)
    output, session_id, exit_code = parse_gemini_stream_json(process)

    print("GEMINI SAYS (adversarial challenge):")
    print("=" * 60)
    print(output)
    print("=" * 60)


def run_consult(question: str, model: str | None = None, session_id: str | None = None) -> str | None:
    prompt = f"{FILESYSTEM_BOUNDARY}\n\n{question}"

    repo_root = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True, text=True
    ).stdout.strip()

    cmd = build_gemini_cmd(prompt, model, session_id)
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=repo_root)
    output, new_session_id, exit_code = parse_gemini_stream_json(process)

    print("GEMINI SAYS (consult):")
    print("=" * 60)
    print(output)
    print("=" * 60)

    if new_session_id:
        ctx_dir = Path(".context")
        ctx_dir.mkdir(exist_ok=True)
        (ctx_dir / "gemini-session-id").write_text(new_session_id)
        print(f"\nSession saved — run again to continue this conversation.")

    return new_session_id


def main():
    if not check_gemini_binary():
        print("Gemini CLI not found. Install: npm install -g @google/gemini-cli")
        sys.exit(1)

    if not check_auth():
        print("No Gemini authentication. Run `gemini` and sign in with Google, or set $GOOGLE_API_KEY")
        sys.exit(1)

    base = get_base_branch()
    args = sys.argv[1:]

    model = None
    if "-m" in args:
        idx = args.index("-m")
        if idx + 1 < len(args):
            model = args[idx + 1]
            args = args[:idx] + args[idx + 2:]

    if not args:
        result = subprocess.run(
            ["git", "diff", f"origin/{base}", "--stat"],
            capture_output=True, text=True
        )
        if result.returncode == 0 and result.stdout.strip():
            print(f"Diff detected against {base}. Use: review | challenge | consult")
        else:
            print("What would you like to ask Gemini?")

    elif args[0] == "review":
        instructions = " ".join(args[1:]) if len(args) > 1 else ""
        run_review(base, instructions, model)

    elif args[0] == "challenge":
        focus = " ".join(args[1:]) if len(args) > 1 else ""
        run_challenge(base, focus, model)

    else:
        question = " ".join(args)
        existing = None
        session_file = Path(".context/gemini-session-id")
        if session_file.exists():
            existing = session_file.read_text().strip()
        run_consult(question, model, existing)


if __name__ == "__main__":
    main()
