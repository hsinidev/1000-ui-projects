---
name: Obsidian Fleet Logic
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#c8c5ce'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#918f98'
  outline-variant: '#47464e'
  surface-tint: '#c3c3ec'
  primary: '#c3c3ec'
  on-primary: '#2c2d4e'
  primary-container: '#1a1b3b'
  on-primary-container: '#8283a9'
  inverse-primary: '#5a5b7f'
  secondary: '#ffffff'
  on-secondary: '#003828'
  secondary-container: '#36ffc4'
  on-secondary-container: '#007255'
  tertiary: '#c3c0ff'
  on-tertiary: '#1d00a5'
  tertiary-container: '#110072'
  on-tertiary-container: '#7975ff'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e1e0ff'
  primary-fixed-dim: '#c3c3ec'
  on-primary-fixed: '#171838'
  on-primary-fixed-variant: '#434466'
  secondary-fixed: '#36ffc4'
  secondary-fixed-dim: '#00e1ab'
  on-secondary-fixed: '#002116'
  on-secondary-fixed-variant: '#00513c'
  tertiary-fixed: '#e2dfff'
  tertiary-fixed-dim: '#c3c0ff'
  on-tertiary-fixed: '#0f0069'
  on-tertiary-fixed-variant: '#3323cc'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 40px
    fontWeight: '700'
    lineHeight: 48px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
    letterSpacing: 0em
  body-sm:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 18px
    letterSpacing: 0.01em
  data-mono:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 11px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 16px
  margin: 24px
  container-max: 100%
  density-compact: 4px
  density-comfortable: 12px
---

## Brand & Style

This design system is engineered for the high-stakes environment of luxury logistics and aerospace fleet management. The personality is authoritative, precise, and sophisticated. It targets high-level operators who require split-second decision-making capabilities within data-saturated environments.

The aesthetic direction is **Futuristic Minimalism** with a **Tactile** digital edge. It utilizes a deep, monochromatic base to allow technical data to command attention. The interface avoids unnecessary decorative elements, instead using light-pipe effects and high-precision lines to create a "glass cockpit" feel. The emotional response is one of total control and premium reliability.

## Colors

The palette is optimized for low-light command centers. 
- **Matte Black (#050505)** serves as the infinite canvas, reducing eye strain and maximizing the perceived contrast of data points.
- **Deep Indigo (#1A1B3B)** acts as the primary structural color, used for sidebars and header backgrounds to provide depth without breaking the dark-mode immersion.
- **Neon Mint (#00FFC2)** is the primary "active" and "success" color. It is used sparingly for critical status indicators, primary buttons, and real-time telemetry updates.
- **Electric Indigo (#4F46E5)** is utilized for secondary interactive elements and data categorization to differentiate from the primary brand indigo.

## Typography

This design system employs a dual-font strategy to balance character with utility. **Space Grotesk** is used for headlines, labels, and technical readouts to provide a futuristic, geometric precision. **Inter** is used for body copy and dense data tables to ensure maximum legibility at small scales.

For high-density views, use `body-sm` and `label-caps` extensively. All numeric data should utilize the `data-mono` style to ensure vertical alignment in tabular layouts, facilitating rapid comparison of fleet metrics.

## Layout & Spacing

The layout utilizes a **Fluid Grid** model with a 12-column structure, allowing the UI to scale across ultra-wide command monitors. A strict 4px baseline grid ensures alignment across high-density data widgets.

Margins and gutters are kept tight (16px/24px) to maximize screen real estate. The design system prioritizes "information density per square inch" over whitespace. Layouts should utilize "Master-Detail" patterns, where a sidebar or top-bar controls a large, multi-widget dashboard canvas.

## Elevation & Depth

Hierarchy is established through **Tonal Layering** and **Subtle Outlines** rather than traditional shadows. 
- **Level 0 (Background):** The darkest surface (#050505).
- **Level 1 (Card/Container):** Slightly lighter matte black (#0F0F12) with a 1px border (#24242B).
- **Level 2 (Active/Hover):** Surface color shifts to Deep Indigo with a faint inner glow.

To signify critical alerts, use a "Neon Bloom" effect: a subtle, 4px outer glow using the Neon Mint hex at 30% opacity. This creates a sense of the screen emitting light for urgent telemetry.

## Shapes

The shape language is "Technical-Soft." A consistent **0.25rem (4px)** radius is applied to all cards, buttons, and inputs. This provides a modern, engineered feel that is more sophisticated than sharp 0px corners, while maintaining a more professional, "hardware" appearance than highly rounded mobile-first systems.

Iconography should follow a linear 1.5pt stroke weight with open terminals to maintain clarity in high-density views.

## Components

### Buttons
Primary buttons use a solid Neon Mint background with Matte Black text for maximum contrast. Secondary buttons are "Ghost" style with a 1px Deep Indigo border and clear backgrounds. All buttons feature a 150ms transition on hover, shifting border-color to white.

### Cards & Widgets
Every data widget must have a defined "Header" area using the `label-caps` typography and a 1px bottom border. Content inside cards should follow the 4px grid.

### Data Visualizations
Charts should use "Glow-Lines"—thin 1.5pt strokes with a 2px blur drop-shadow in the same color. Use Neon Mint for "Optimal" states and a vibrant Magenta for "Critical" states to contrast against the Indigo/Black base.

### Status Indicators
Status chips are small, rectangular, and use a "Light-Pipe" metaphor: a dark grey background with a small, glowing 4px square of color (Mint, Amber, or Red) to the left of the label.

### Technical Inputs
Input fields are dark-filled with no top or side borders; only a 1px bottom border that glows Neon Mint upon focus. This mimics a command-line interface refined for luxury aesthetics.