---
description: Create a git commit from current changes
allowed-tools:
  - Bash(git add:*)
  - Bash(git status:*)
  - Bash(git diff:*)
  - Bash(git log:*)
  - Bash(git commit:*)
---

Show current `git status`, staged and unstaged changes via `git diff HEAD`, and the last 5 commits via `git log --oneline -5`. Based on these, stage relevant files and create a single commit with an appropriate message. Do everything in one message with no other text.

Commit message format:
- First line: imperative mood, max 72 chars (e.g. "Add auth documentation to adonis/common/")
- No body unless the change is non-obvious
- Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
