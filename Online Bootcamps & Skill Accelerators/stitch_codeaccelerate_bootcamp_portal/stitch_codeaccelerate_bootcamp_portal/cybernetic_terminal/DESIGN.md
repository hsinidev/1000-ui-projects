---
name: Cybernetic Terminal
colors:
  surface: '#08132a'
  surface-dim: '#08132a'
  surface-bright: '#2f3952'
  surface-container-lowest: '#030d25'
  surface-container-low: '#101b33'
  surface-container: '#151f37'
  surface-container-high: '#1f2942'
  surface-container-highest: '#2a344d'
  on-surface: '#d9e2ff'
  on-surface-variant: '#bacac3'
  inverse-surface: '#d9e2ff'
  inverse-on-surface: '#263049'
  outline: '#85948e'
  outline-variant: '#3c4a45'
  surface-tint: '#38debb'
  primary: '#ffffff'
  on-primary: '#00382d'
  primary-container: '#5ffbd6'
  on-primary-container: '#00725e'
  inverse-primary: '#006b58'
  secondary: '#b9c7e4'
  on-secondary: '#233148'
  secondary-container: '#3c4962'
  on-secondary-container: '#abb9d6'
  tertiary: '#ffffff'
  on-tertiary: '#1e304f'
  tertiary-container: '#d7e3ff'
  on-tertiary-container: '#536586'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#5ffbd6'
  primary-fixed-dim: '#38debb'
  on-primary-fixed: '#002019'
  on-primary-fixed-variant: '#005142'
  secondary-fixed: '#d6e3ff'
  secondary-fixed-dim: '#b9c7e4'
  on-secondary-fixed: '#0d1c32'
  on-secondary-fixed-variant: '#39475f'
  tertiary-fixed: '#d7e3ff'
  tertiary-fixed-dim: '#b5c7ed'
  on-tertiary-fixed: '#061b39'
  on-tertiary-fixed-variant: '#354767'
  background: '#08132a'
  on-background: '#d9e2ff'
  surface-variant: '#2a344d'
typography:
  h1:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  h3:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  code-sm:
    fontFamily: monospace
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  gutter: 24px
  margin: 40px
  container-max: 1280px
---

## Brand & Style

The design system is engineered to evoke the high-stakes, high-focus environment of an elite terminal. It targets ambitious developers who value precision, speed, and technical depth. The aesthetic merges **Modern Minimalism** with **Cyberpunk-inspired High-Contrast**, creating a "command line" atmosphere that feels both premium and functional.

The interface should feel like a sophisticated IDE. This is achieved through a strict dark mode foundation, razor-sharp lines, and intentional "glow" states that signal activity or success. The emotional response is one of "Deep Focus"—minimizing visual noise while using vibrant accents to direct cognitive energy toward the code and curriculum.

## Colors

The palette is anchored by **Midnight Blue (#0A192F)** for the primary canvas, providing a deep, low-fatigue background. **Graphite (#233554)** serves as the structural layer, used for cards, section headers, and nested containers to create subtle depth without breaking the dark-mode immersion.

The hero color is **Neon Mint (#64FFDA)**. It is used sparingly for primary actions, success states, and critical data points. To enhance the "technical" energy, use this color for text glows and subtle drop shadows on interactive elements. Text is rendered in high-contrast off-whites and cool greys to ensure legibility against the dark void.

## Typography

This design system utilizes a dual-typeface strategy. **Space Grotesk** is used for headlines and UI labels to provide a geometric, futuristic edge that feels technical and bold. **Inter** is the workhorse for body copy and long-form instructional content, chosen for its exceptional readability in dark mode at various scales.

Technical accents—such as line numbers, terminal prompts, and variable names—must use a monospace font. All uppercase labels should have increased letter spacing to mimic the look of hardware identification tags.

## Layout & Spacing

The layout philosophy follows a **Fixed-Fluid Hybrid** model. Content is contained within a 1280px max-width wrapper, utilizing a 12-column grid. Spacing is strictly based on a 4px baseline shift to ensure mathematical harmony.

Large-scale backgrounds should incorporate a subtle 32px square grid pattern in a low-opacity Graphite (#233554) to reinforce the "blueprint" or "editor" feel. Margins are generous between sections to prevent the dark interface from feeling claustrophobic, while internal component padding remains tight and efficient.

## Elevation & Depth

In this dark-mode ecosystem, depth is communicated through **Tonal Layering** and **Luminescent Accents** rather than traditional shadows. 

1.  **Base Layer:** Midnight Blue (#0A192F).
2.  **Surface Layer:** Graphite (#233554) with a 1px solid border of the same color but 10% lighter.
3.  **Active Layer:** Elements that are being hovered or focused should emit a "Neon Mint" glow (box-shadow: 0 0 15px rgba(100, 255, 218, 0.2)).

Avoid heavy blurs. Use crisp, 1px lines to separate code blocks from instructional text. Use semi-transparent overlays (20% opacity) for modal backdrops to maintain the visibility of the underlying "codebase."

## Shapes

The design system employs **Sharp (0px)** corners for all structural components, including buttons, cards, and input fields. This reinforces the "unrefined" brutalist edge and technical precision of a development environment. 

The only exception to the sharp-corner rule is for status indicators (dots) or specific "user" avatars, which remain circular. All other UI containers should feel like cut-glass or machined metal—precise and uncompromising.

## Components

-   **Buttons:** Primary buttons feature a solid Neon Mint background with Midnight Blue text. No rounded corners. The hover state adds a 4px offset "ghost" border. Secondary buttons are Ghost-style with a Neon Mint border and text.
-   **Inputs:** Fields are dark (Midnight Blue) with a 1px Graphite border. Upon focus, the border changes to Neon Mint and a "scanning" horizontal line animation briefly flashes across the top.
-   **Cards:** Use Graphite backgrounds with no shadow. Use a "Label-caps" typography style in the top left corner to categorize the content (e.g., "MODULE 01", "README.md").
-   **Chips/Tags:** Monospace font, 1px border, no background. Used for tech-stack identifiers (e.g., [ React ], [ TypeScript ]).
-   **Code Blocks:** Distinct containers with a slightly darker background than the base. Features a faux "window header" with three dots (red, yellow, green) to mimic a MacOS terminal window.
-   **Progress Bars:** Thin, 4px tall bars. The filled portion should have a "pulse" animation moving from left to right in Neon Mint.