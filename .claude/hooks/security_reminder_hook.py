#!/usr/bin/env python3
"""
Pre-tool-use hook: checks the tool input for security-sensitive patterns and
prints a one-time warning per session if any are found.

Exit code 0 = allow the tool call to proceed.
Exit code 2 = block the tool call (with explanation shown to the user).

This hook only warns (exit 0) — it does not block. Adjust patterns below and
change exit codes to 2 if you want hard blocks on specific patterns.
"""

import json
import os
import re
import sys
import tempfile

# --- Patterns that warrant a security reminder ---

PATTERNS = [
    # GitHub Actions expression injection
    (r'\$\{\{.*github\.event\..*\}\}', "GitHub Actions expression injection risk — user-controlled input in run: steps"),
    # Shell exec calls
    (r'\bexec\s*\(', "exec() call detected — verify input is not user-controlled"),
    # Python/JS eval
    (r'\beval\s*\(', "eval() call detected — avoid evaluating untrusted input"),
    # React dangerouslySetInnerHTML
    (r'dangerouslySetInnerHTML', "dangerouslySetInnerHTML detected — ensure content is sanitized"),
    # Raw SQL string interpolation
    (r'(SELECT|INSERT|UPDATE|DELETE).*\$\{', "Possible SQL injection — use parameterized queries"),
    # innerHTML assignment
    (r'\.innerHTML\s*=', "innerHTML assignment — ensure content is sanitized to prevent XSS"),
    # child_process with variable
    (r'child_process.*exec\(', "child_process.exec with possible variable input — use execFile or spawn"),
    # Pickle deserialization
    (r'\bpickle\.loads?\(', "pickle deserialization — never unpickle untrusted data"),
    # Hardcoded secrets pattern (rough heuristic)
    (r'(?i)(password|secret|api_key|token)\s*=\s*["\'][^"\']{8,}["\']', "Possible hardcoded secret — use environment variables instead"),
]

# --- Session deduplication ---
# We write warned pattern keys to a temp file scoped to this Claude session.
# Each warning fires at most once per session.

def _session_file() -> str:
    session_id = os.environ.get("CLAUDE_SESSION_ID", "default")
    return os.path.join(tempfile.gettempdir(), f"security_hook_{session_id}.json")

def _load_warned() -> set:
    path = _session_file()
    if os.path.exists(path):
        try:
            with open(path) as f:
                return set(json.load(f))
        except Exception:
            return set()
    return set()

def _save_warned(warned: set) -> None:
    with open(_session_file(), "w") as f:
        json.dump(list(warned), f)

# --- Main ---

def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0  # not JSON — pass through

    # Flatten all string values in the tool input for scanning
    tool_input = payload.get("tool_input", {})
    text = " ".join(str(v) for v in tool_input.values() if isinstance(v, str))

    warned = _load_warned()
    new_warnings = []

    for pattern, message in PATTERNS:
        key = pattern  # use the pattern string as the dedup key
        if key not in warned and re.search(pattern, text):
            new_warnings.append(message)
            warned.add(key)

    if new_warnings:
        _save_warned(warned)
        print("\n\033[33m[Security Reminder]\033[0m", file=sys.stderr)
        for w in new_warnings:
            print(f"  · {w}", file=sys.stderr)
        print("", file=sys.stderr)

    return 0  # always allow — this hook warns only

if __name__ == "__main__":
    sys.exit(main())
