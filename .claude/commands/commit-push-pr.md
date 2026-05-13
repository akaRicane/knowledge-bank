---
description: Commit, push, and open a pull request in one shot
allowed-tools:
  - Bash(git branch:*)
  - Bash(git checkout:*)
  - Bash(git add:*)
  - Bash(git status:*)
  - Bash(git diff:*)
  - Bash(git log:*)
  - Bash(git commit:*)
  - Bash(git push:*)
  - Bash(gh pr create:*)
---

1. Show `git status` and `git diff HEAD`
2. If on `main` or `master`, create a new branch with a short descriptive name
3. Stage relevant files and create a single commit with an appropriate message
4. Push the branch to origin with `-u`
5. Create a pull request with `gh pr create` — write a clear title and body summarizing what changed and why

Do all steps in a single message with no other text.

Commit message: imperative mood, max 72 chars.
Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
