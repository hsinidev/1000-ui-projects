---
name: Forge Protocol
colors:
  surface: '#131314'
  surface-dim: '#131314'
  surface-bright: '#3a393a'
  surface-container-lowest: '#0e0e0f'
  surface-container-low: '#1c1b1c'
  surface-container: '#201f20'
  surface-container-high: '#2a2a2b'
  surface-container-highest: '#353435'
  on-surface: '#e5e2e2'
  on-surface-variant: '#c6c6cc'
  inverse-surface: '#e5e2e2'
  inverse-on-surface: '#313031'
  outline: '#909096'
  outline-variant: '#45464b'
  surface-tint: '#c3c6d3'
  primary: '#c3c6d3'
  on-primary: '#2c303a'
  primary-container: '#0a0e17'
  on-primary-container: '#777b87'
  inverse-primary: '#5a5e69'
  secondary: '#c1c7d1'
  on-secondary: '#2b3139'
  secondary-container: '#414750'
  on-secondary-container: '#b0b5bf'
  tertiary: '#d8c3af'
  on-tertiary: '#3b2e20'
  tertiary-container: '#160c03'
  on-tertiary-container: '#8a7867'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dfe2ef'
  primary-fixed-dim: '#c3c6d3'
  on-primary-fixed: '#181b25'
  on-primary-fixed-variant: '#434751'
  secondary-fixed: '#dde3ed'
  secondary-fixed-dim: '#c1c7d1'
  on-secondary-fixed: '#161c23'
  on-secondary-fixed-variant: '#414750'
  tertiary-fixed: '#f5dfca'
  tertiary-fixed-dim: '#d8c3af'
  on-tertiary-fixed: '#25190d'
  on-tertiary-fixed-variant: '#534435'
  background: '#131314'
  on-background: '#e5e2e2'
  surface-variant: '#353435'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
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
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 48px
  container-max: 1280px
  gutter: 24px
---

## Brand & Style
The design system is engineered for high-performance developer environments, prioritizing cognitive efficiency and technical precision. The brand personality is "Expert-Grade," evoking the focused, low-distraction atmosphere of a high-end IDE. 

The visual style is a **Code-Editor Aesthetic** mixed with **Minimalism**. It avoids decorative fluff in favor of structural clarity. By utilizing a dark-first color strategy and syntax-highlighting logic for visual cues, the design system makes complex API documentation and technical workflows feel organized and native to a developer's existing toolchain. The emotional response is one of control, reliability, and speed.

## Colors
This design system utilizes a "Lights-Out" palette optimized for long-duration technical work. The primary background (Midnight Blue) provides a deep, low-glare canvas. 

Functional logic drives color application:
- **Neon Cyan** is reserved exclusively for primary actions and active states.
- **Graphite** serves as the structural scaffolding, defining containers and inactive boundaries.
- **Semantic Colors** (Electric Green, Vivid Orange/Red) are used sparingly for status indicators, mimicking the "problems" panel in a terminal.
- **Syntax Accents**: Use tertiary shades of purple and gold only within code blocks to provide visual rhythm without distracting from the main UI navigation.

## Typography
The typography system balances futuristic geometry with utilitarian readability. **Space Grotesk** is used for headlines to give the design system a modern, technical edge. **Inter** handles the heavy lifting for body copy, ensuring that long-form documentation remains legible.

**JetBrains Mono** is the core functional font. It must be used for all code snippets, API endpoints, terminal commands, and metadata labels. Line heights are generous in documentation sections to prevent "text-wall" fatigue, while labels use a tighter, uppercase treatment to denote UI hierarchy.

## Layout & Spacing
The design system employs a **12-column fluid grid** for desktop and a single-column stacked layout for mobile. A strict 4px base unit ensures mathematical precision across all components.

On mobile, the layout shifts to prioritize the "Search-First" workflow, with a persistent floating action button for search or a compact top-bar. Documentation pages utilize a "Reading Rail" approach—a fixed-width central column (max 800px) to maintain optimal line lengths, with secondary navigation tucked into a collapsible sidebar or "Drawer" on smaller screens.

## Elevation & Depth
Depth is communicated through **Tonal Layering** and **Subtle Outlines** rather than traditional drop shadows. In this design system, objects that are "higher" in the hierarchy are represented by lighter surface colors (e.g., moving from Midnight Blue to Graphite).

- **Level 0 (Background):** Midnight Blue (#0A0E17).
- **Level 1 (Cards/Sidebar):** Graphite (#2D333B) or a 5% lighter tint of Midnight Blue.
- **Level 2 (Popovers/Tooltips):** Solid background with a 1px Neon Cyan border.
- **Active State:** Elements gain a subtle 0 0 8px glow using the Accent color to simulate a "powered-on" hardware state.

## Shapes
The shape language is **Sharp**. Right angles are used for buttons, input fields, and containers to reinforce the "Terminal" and "Code Editor" aesthetic. This lack of roundedness signals a professional, no-nonsense tool. 

The only exception is for status dots or user avatars, which may be circular to provide a soft visual contrast to the rigid grid. Borders should be kept at a constant 1px width, creating a wireframe-like precision across the interface.

## Components
- **Buttons:** Primary buttons use a solid Neon Cyan background with Midnight Blue text. Secondary buttons are transparent with a 1px Graphite border and Cyan text on hover.
- **API Chips:** Small, monospaced badges for HTTP methods (GET: Green, POST: Cyan, DELETE: Red). Use a subtle background tint and high-contrast text.
- **Input Fields:** Dark backgrounds (#0A0E17) with 1px Graphite borders. On focus, the border transitions to Neon Cyan with a sharp, square caret.
- **Code Blocks:** Syntax highlighting is mandatory. Use a slightly darker "Deep Black" background for the block itself to separate it from the UI. Include a "Copy" icon in the top right that triggers a Cyan "Success" feedback loop.
- **Terminal Component:** A specialized container for CLI examples, featuring a header bar with "window controls" (red, yellow, green dots) and a monospaced prompt character (`$`).
- **Navigation:** A vertical, collapsible sidebar with "icon + label" pairing. Active links are marked with a 2px vertical Cyan line on the left edge.