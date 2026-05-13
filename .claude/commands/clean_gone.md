---
description: Remove local branches marked [gone] (remote deleted) and their worktrees
allowed-tools:
  - Bash(git branch:*)
  - Bash(git worktree:*)
---

1. Run `git branch -v` to list all local branches and identify those marked `[gone]`
2. Run `git worktree list` to list all worktrees
3. For each `[gone]` branch:
   - If a worktree exists for it, remove it with `git worktree remove`
   - Delete the local branch with `git branch -d` (use `-D` only if `-d` fails)
4. Report which worktrees and branches were removed, and which were skipped
