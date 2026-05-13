# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

This is a standalone knowledge bank for programming patterns and documentation. It is used as a **git submodule** across projects. Documentation is written in plain HTML with a shared CSS file — no build step, no external dependencies. Every file can be opened directly in a browser.

## Navigation

Start from [`index.html`](index.html) — it lists all themes as cards. Each theme has its own `index.html` that lists its documents. Follow links to find relevant content.

```
index.html          ← global entry point
├── claude/
│   ├── index.html              ← setup guide + .claude/ wiring
│   ├── agents.html             ← all agents (code-architect, code-explorer, etc.)
│   ├── commands.html           ← all commands (feature-dev, review-pr, commit, etc.)
│   ├── hooks.html              ← security reminder hook, custom hook patterns
│   └── skills.html             ← frontend-design skill
├── adonis/
│   ├── index.html              ← AdonisJS theme index
│   ├── common/                 ← patterns common to all versions
│   │   ├── auth.html
│   │   ├── models.html
│   │   ├── services.html
│   │   ├── mailer.html
│   │   ├── validation.html
│   │   └── testing.html
│   └── v6/
│       └── index.html          ← v6-specific: packages, adonisrc, path aliases
├── design/
│   └── index.html              ← artistic direction, CSS tokens, viewer layouts
└── infrastructure/
    └── index.html              ← env vars, config files, database, CORS, security
```

CSS: `_shared/styles.css` — linked from every HTML file with a relative path.

## Authoring rules

Follow these rules strictly when creating or editing any HTML file:

1. **Project-agnostic.** Never include project-specific values — model names, email addresses, hostnames, database connection names, or company-specific service names. Use generic placeholders: `app_db`, `app@example.com`, `mail.example.com`, `MyModel`, `PostFactory`. Zuno-specific content belongs in Zuno's repository, not here.

3. **One file per concern.** Never cram unrelated topics into one file.

4. **Common vs version-specific split.** Patterns that apply across versions go in `common/`. Behaviour locked to a specific version goes in `v6/`, `v7/`, etc.

5. **CSS link path is always relative.** Count directory depth from the file to `_shared/styles.css`:
   - Root (`index.html`) → `_shared/styles.css`
   - First level (`adonis/index.html`) → `../_shared/styles.css`
   - Second level (`adonis/common/auth.html`) → `../../_shared/styles.css`

6. **No external dependencies.** No CDN links, no JS frameworks. The repo must work offline and as a static submodule.

7. **Every `<section>` must have an `id`** for deep-linking (e.g. `<section id="configuration">`).

8. **Update the `version-badge` date** when creating or significantly editing a file.

9. **New themes:** create a new theme folder only when content does not fit any existing theme. Immediately add a card for it in the root `index.html`.

10. **Always update docs** when a pattern changes in a project that references this knowledge bank. If a config, service, or convention is updated in a project, flag which HTML file in this repo needs updating.

## HTML document template

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Topic] — [Theme] — Knowledge Bank</title>
  <link rel="stylesheet" href="../../_shared/styles.css">
</head>
<body>
  <div class="page-layout">
    <nav class="breadcrumb">
      <a href="../../index.html">Knowledge Bank</a>
      <span class="breadcrumb__sep">/</span>
      <a href="../index.html">[Theme]</a>
      <span class="breadcrumb__sep">/</span>
      <span class="breadcrumb__current">[Topic]</span>
    </nav>

    <nav class="toc">
      <div class="toc__title">On this page</div>
      <ul class="toc__list">
        <li class="toc__item"><a href="#section-id">Section name</a></li>
      </ul>
    </nav>

    <main>
      <header class="page-header">
        <h1>[Topic]</h1>
        <p class="subtitle">One-line description.</p>
        <div class="meta">
          <span class="tag">[theme]</span>
          <span class="version-badge">Last updated: YYYY-MM-DD</span>
        </div>
      </header>

      <section id="first-section">
        <h2>First section</h2>
        <p>Content here.</p>
      </section>
    </main>
  </div>
</body>
</html>
```

## Version-specific content

When common and version-specific content must coexist in one file, wrap the version block:

```html
<div class="version v6" data-version="v6">
  <!-- v6-specific content here -->
</div>

<div class="version v7" data-version="v7">
  <!-- v7-specific content here -->
</div>
```

CSS classes available: `.version.v6` (blue border), `.version.v7` (green border), `.version.v8` (orange border).

## Available CSS components

- `.page-layout` / `.page-layout--full` — grid wrapper (with/without sidebar)
- `.breadcrumb` — top navigation trail
- `.toc` — sticky sidebar table of contents
- `.page-header` — title + subtitle + meta block
- `.tag` — small label chip
- `.version-badge` — monospace date/version chip
- `.version.v6/.v7/.v8` — coloured left-border version block
- `.callout.callout--note/.callout--warn/.callout--tip` — inline callout box
- `.card-grid` + `.card` — responsive card grid (for index pages)
- `.doc-list` + `.doc-list__item` — linked document list (for theme indexes)
- `.table-wrap` + `table` — responsive table wrapper
- `pre[data-lang]` — code block with language label
