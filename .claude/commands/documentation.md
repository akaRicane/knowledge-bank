---
description: Generate or update an HTML documentation page following knowledge_bank conventions
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash(find:*)
  - Bash(ls:*)
---

You are writing documentation for the `knowledge_bank` repository — a project-agnostic reference library served as plain HTML files.

## Rules (non-negotiable)

1. **Project-agnostic**: Never write Zuno-specific values (model names, email addresses, hostnames, DB names). Use placeholders: `app_db`, `app@example.com`, `mail.example.com`, `MyModel`, `PostFactory`.
2. **No build step**: Pure HTML + shared CSS. No frameworks, no npm, no external CDN.
3. **CSS path**: Use `../_shared/styles.css` from inside a theme folder (e.g. `adonis/common/`) or `_shared/styles.css` from a theme index.
4. **Breadcrumb**: Always a sticky `<nav class="breadcrumb">` as the first element inside `<body>`. Match depth: `Knowledge Bank → Theme → Page`.
5. **TOC**: A `<aside class="toc">` with anchor links to every `<h2>` on the page.
6. **Section IDs**: Every `<h2>` must have a matching `id` attribute used in the TOC.
7. **Version badges**: Use `<div class="version v6">` or `<div class="version v7">` wrappers when content is version-specific. Add a `<p class="version-date">Last verified: YYYY-MM-DD</p>` at the bottom.
8. **Code blocks**: `<pre data-lang="ts"><code>` — always specify `data-lang`.
9. **Callouts**: `<div class="callout callout--warning">` / `callout--info` / `callout--tip`.

## Process

1. Read `_shared/styles.css` and an existing page in the same theme directory (or `adonis/common/auth.html` as a reference) to match structure exactly.
2. Determine the correct relative path to `_shared/styles.css` based on the target file's depth.
3. Write the full HTML file using the standard template below.
4. If updating an existing file: read it first, then make targeted edits — do not rewrite sections that aren't changing.

## Standard HTML template

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PAGE TITLE — Knowledge Bank</title>
  <link rel="stylesheet" href="PATH_TO_shared/styles.css">
</head>
<body>

<nav class="breadcrumb">
  <a href="PATH_TO_ROOT/index.html">Knowledge Bank</a>
  <span>Theme</span>
  <span>Page Title</span>
</nav>

<div class="page-layout">
  <aside class="toc">
    <h3>On this page</h3>
    <ul>
      <li><a href="#section-one">Section One</a></li>
    </ul>
  </aside>

  <main>
    <header class="page-header">
      <h1>Page Title</h1>
      <p class="page-subtitle">One-sentence description.</p>
    </header>

    <section id="section-one">
      <h2>Section One</h2>
      <p>Content here.</p>
    </section>

    <p class="version-date">Last verified: YYYY-MM-DD</p>
  </main>
</div>

</body>
</html>
```

After writing the file, confirm which file was created/updated and what sections it contains.
