---
name: CloudArchitect
colors:
  surface: '#0c141f'
  surface-dim: '#0c141f'
  surface-bright: '#323a46'
  surface-container-lowest: '#070f19'
  surface-container-low: '#141c27'
  surface-container: '#18202c'
  surface-container-high: '#222a36'
  surface-container-highest: '#2d3541'
  on-surface: '#dbe3f3'
  on-surface-variant: '#c7c6cc'
  inverse-surface: '#dbe3f3'
  inverse-on-surface: '#29313d'
  outline: '#909096'
  outline-variant: '#46464c'
  surface-tint: '#c3c6d7'
  primary: '#c3c6d7'
  on-primary: '#2c303d'
  primary-container: '#0a0e1a'
  on-primary-container: '#777b8a'
  inverse-primary: '#5a5e6d'
  secondary: '#d3fbff'
  on-secondary: '#00363a'
  secondary-container: '#00eefc'
  on-secondary-container: '#00686f'
  tertiary: '#c1c8ca'
  on-tertiary: '#2b3234'
  tertiary-container: '#091012'
  on-tertiary-container: '#767d7f'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dfe2f3'
  primary-fixed-dim: '#c3c6d7'
  on-primary-fixed: '#171b28'
  on-primary-fixed-variant: '#434654'
  secondary-fixed: '#7df4ff'
  secondary-fixed-dim: '#00dbe9'
  on-secondary-fixed: '#002022'
  on-secondary-fixed-variant: '#004f54'
  tertiary-fixed: '#dde4e6'
  tertiary-fixed-dim: '#c1c8ca'
  on-tertiary-fixed: '#161d1f'
  on-tertiary-fixed-variant: '#41484a'
  background: '#0c141f'
  on-background: '#dbe3f3'
  surface-variant: '#2d3541'
typography:
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 28px
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
    lineHeight: '1.6'
  code-sm:
    fontFamily: monospace
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.4'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  gutter: 24px
  margin: 32px
  container-max: 1440px
---

## Brand & Style

This design system is engineered for the high-stakes environment of cloud architecture and technical certification. The brand personality is authoritative, precise, and forward-leaning, evoking the feeling of a sophisticated command center rather than a standard educational tool. 

The aesthetic leverages a **High-Contrast / Technical** style. It prioritizes clarity through sharp geometry and a "dark mode" default that reduces eye strain during long study sessions. By combining a deep, immersive background with vibrant, neon functional accents, the UI establishes a clear hierarchy where action and progress are immediately visible against a complex data landscape.

## Colors

The palette is strictly functional, designed to mimic terminal environments while maintaining modern readability.

- **Midnight Blue (#0A0E1A):** The primary canvas. It provides deep contrast for neon elements and sets a professional, "tech-first" tone.
- **Neon Cyan (#00F0FF):** Reserved exclusively for interactive elements, progress indicators, and primary calls to action. It should be used sparingly to maintain its "high-energy" impact.
- **Graphite (#2D3436):** Used for structural boundaries, dividers, and component backgrounds. It separates content areas without breaking the dark-mode immersion.
- **Secondary Text (#9DA5B4):** A muted grey used for labels and metadata to ensure the primary information remains the focal point.

## Typography

This design system utilizes a dual-font approach to balance readability with technical flavor. 

**Space Grotesk** is used for headlines and navigational labels. Its geometric, slightly eccentric letterforms reinforce the futuristic, technical nature of cloud computing. All-caps styling should be applied to small labels to enhance the "interface" feel.

**Inter** serves as the primary body face, chosen for its exceptional legibility in dark environments. For data points, IP addresses, and code snippets, a standard **Monospace** stack is used to ensure character-level clarity, which is critical for technical certification content.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model to maintain a sense of structured engineering. Use a 12-column grid for primary dashboards and a single-column focused layout for examination modules.

Spacing is governed by a strict 4px baseline shift. Large containers should use 32px padding to maintain an airy, premium feel despite the dark palette. Use generous margins between distinct technical sections to prevent information density from becoming overwhelming. Content should be centered within a 1440px max-width container to ensure high-end monitor support.

## Elevation & Depth

In this design system, depth is conveyed through **Tonal Layering** and **Subtle Glows** rather than traditional shadows.

1.  **Base Layer:** Midnight Blue (#0A0E1A) for the global background.
2.  **Surface Layer:** Graphite (#2D3436) for cards, sidebars, and header areas, using sharp 1px borders in a slightly lighter grey to define edges.
3.  **Active State:** Elements in focus or active states utilize a "Neon Glow"—a subtle, outer box-shadow using Neon Cyan at 20-30% opacity. 

Avoid using soft, diffused shadows. Depth should feel "stacked" and architectural, with crisp lines separating different levels of the interface.

## Shapes

The shape language is **Sharp (0)**. To reflect the precision of architectural diagrams and cloud infrastructure, all buttons, cards, and input fields feature 90-degree corners. 

This lack of rounding creates a "brutalist-tech" aesthetic that emphasizes stability and accuracy. The only exception is for circular icons or specific status pips. All structural borders should be 1px wide, maintaining a clean, wireframe-like precision across the entire design system.

## Components

### Buttons
Primary buttons are solid Neon Cyan with black text for maximum contrast. Secondary buttons use a ghost style: a 1px Cyan border with Cyan text. All buttons have 0px corner radius and a subtle "Cyan Glow" on hover.

### Cards & Containers
Cards use the Graphite color for the background with a 1px border. For "Active" or "Selected" cards (e.g., a selected certification path), the border color switches to Neon Cyan.

### Input Fields
Inputs are dark-hued with a Graphite bottom border only (terminal style). On focus, the border becomes Neon Cyan with a faint vertical cursor block in the same color.

### Chips & Badges
Small, rectangular badges for "Exam Codes" or "Status" (e.g., `AWS-SAA-C03`). These use Monospace type and a subtle 1px border.

### Progress Indicators
Progress bars should be thin (4px height) and use a solid Neon Cyan fill against a Graphite track. For certification paths, use a "glow-pulse" animation on the leading edge of the progress fill.

### Technical Data Tables
Tables must feature Monospace text for all cell data. Row headers should be in all-caps Space Grotesk. Use alternating Graphite/Midnight row fills for readability in long data sets.