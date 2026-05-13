---
name: frontend-design
description: Create distinctive, production-grade frontend interfaces with high design quality. Use when building web components, pages, or applications.
---

# Frontend Design Skill

## Core philosophy

Avoid generic "AI slop" aesthetics. Every interface should have a reason to look the way it does — tied to its purpose, audience, and tone. Generate creative, polished code that is context-specific and memorable.

## Design thinking (before writing any code)

Answer these four questions first:

1. **Purpose** — What problem does this interface solve? Who uses it?
2. **Tone** — Pick an extreme aesthetic and commit to it:
   brutally minimal · maximalist · retro-futuristic · organic · luxury · playful · editorial · brutalist · art deco · soft/pastel · industrial
3. **Constraints** — What are the technical requirements?
4. **Differentiation** — What makes this interface unforgettable?

## Implementation guidelines

### Typography
- Choose distinctive fonts — not generic ones (no Arial, Inter, Roboto, system-ui)
- Pair a distinctive display font with a refined body font
- Avoid overused choices (Space Grotesk, etc.)
- Use type scale tokens — never raw px/rem values in components

### Color & theme
- Commit to a cohesive aesthetic — always use CSS custom properties
- Dominant colors with sharp accents beat timid evenly-distributed palettes
- Avoid clichéd combos (purple gradient on white, blue CTA on grey hero)

### Motion
- CSS transitions for hover/focus; Motion library (or Framer Motion) for React sequences
- Focus on high-impact moments: page load staggered reveals, hover surprises
- Hover = color/opacity shift — never scale or size jumps
- Keep it responsive-feeling, not theatrical

### Spatial composition
- Unexpected layouts: asymmetry, overlap, diagonal flow, grid-breaking elements
- Generous negative space OR controlled density — pick one and commit
- Avoid predictable layouts (hero → features → CTA → footer)

### Backgrounds & visual details
- Atmosphere and depth — not flat solid colors
- Gradient meshes, noise, patterns, layered transparencies, dramatic shadows
- Grain overlays, decorative borders, custom cursors where appropriate

## Anti-patterns — never use

- Overused font families: Inter, Roboto, Arial, system fonts
- Clichéd color schemes: purple gradient on white, safe blue accents
- Predictable component patterns with no context-specific character
- Solid background colors with no depth or texture
- Animations that loop without user interaction

## Complexity matching

Match implementation complexity to vision:
- **Maximalist** designs need elaborate, layered code
- **Minimalist/refined** designs need restraint and precision — not less effort, different effort

Always ship working, production-quality code — not prototypes or stubs.
