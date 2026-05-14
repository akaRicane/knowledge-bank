# knowledge_bank

A personal knowledge base for programming patterns and tooling, organized by theme. Documentation is written in plain HTML with a shared CSS file — no build step, no external dependencies, browser-servable as-is.

Designed to be used as a **git submodule** across projects.

## Usage

```bash
# Add to a project
git submodule add https://github.com/akaRicane/knowledge-bank knowledge_bank

# Update after upstream changes
git submodule update --remote knowledge_bank
```

Reference the knowledge bank from your project's `CLAUDE.md`:

```markdown
## Knowledge bank
Project-agnostic patterns are in `knowledge_bank/`. Start from `knowledge_bank/index.html`.
```

## Structure

```
index.html          ← global entry point
├── claude/         ← agents, commands, hooks, skills for Claude Code
├── http/           ← HTTP methods and status codes
├── adonis/         ← AdonisJS patterns (common + v6)
├── design/         ← project-specific design direction (placeholder)
└── infrastructure/ ← project-specific infra config (placeholder)
```

## Browsing

Open any `.html` file directly in a browser. No server needed.

## License

MIT — see [LICENSE](LICENSE).
