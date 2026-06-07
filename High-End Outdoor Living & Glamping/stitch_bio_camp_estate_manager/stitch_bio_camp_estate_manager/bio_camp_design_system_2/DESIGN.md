---
name: Bio-Camp Design System
colors:
  surface: '#121414'
  surface-dim: '#121414'
  surface-bright: '#38393a'
  surface-container-lowest: '#0d0e0f'
  surface-container-low: '#1a1c1c'
  surface-container: '#1e2020'
  surface-container-high: '#282a2b'
  surface-container-highest: '#333535'
  on-surface: '#e2e2e2'
  on-surface-variant: '#e2bfb0'
  inverse-surface: '#e2e2e2'
  inverse-on-surface: '#2f3131'
  outline: '#a98a7d'
  outline-variant: '#5a4136'
  surface-tint: '#ffb693'
  primary: '#ffb693'
  on-primary: '#561f00'
  primary-container: '#ff6b00'
  on-primary-container: '#572000'
  inverse-primary: '#a04100'
  secondary: '#b9c7e4'
  on-secondary: '#233148'
  secondary-container: '#3c4962'
  on-secondary-container: '#abb9d6'
  tertiary: '#c1c8ca'
  on-tertiary: '#2b3234'
  tertiary-container: '#939a9c'
  on-tertiary-container: '#2b3234'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbcc'
  primary-fixed-dim: '#ffb693'
  on-primary-fixed: '#351000'
  on-primary-fixed-variant: '#7a3000'
  secondary-fixed: '#d6e3ff'
  secondary-fixed-dim: '#b9c7e4'
  on-secondary-fixed: '#0d1c32'
  on-secondary-fixed-variant: '#39475f'
  tertiary-fixed: '#dde4e6'
  tertiary-fixed-dim: '#c1c8ca'
  on-tertiary-fixed: '#161d1f'
  on-tertiary-fixed-variant: '#41484a'
  background: '#121414'
  on-background: '#e2e2e2'
  surface-variant: '#333535'
typography:
  display-xl:
    fontFamily: JetBrains Mono
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: JetBrains Mono
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: JetBrains Mono
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: JetBrains Mono
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  body-sm:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
  code-data:
    fontFamily: JetBrains Mono
    fontSize: 13px
    fontWeight: '500'
    lineHeight: '1.4'
spacing:
  unit: 4px
  gutter: 16px
  margin: 24px
  container-max: 1440px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style

This design system is engineered for mission-critical campsite management where security, utility, and environmental monitoring are paramount. The aesthetic blends **Industrial Brutalism** with **Modern Technical** interfaces to evoke a sense of "tactical reliability." It targets elite site administrators who require high-density data visualization and instant status recognition.

The UI should feel like a high-end command console—robust, uncompromising, and highly structured. We utilize heavy borders, monospaced typography, and a strict color hierarchy to ensure the interface remains legible under intense operational conditions. The emotional response is one of controlled authority and technical precision.

## Colors

The palette is anchored by the deep, atmospheric **Midnight Blue (#0A192F)** for all primary backgrounds to reduce eye strain during night operations. **Safety Orange (#FF6B00)** serves as the high-visibility tactical layer, used exclusively for primary actions, critical alerts, and active states.

**Graphite (#2D3436)** and secondary slate tones provide the structural scaffolding for containers and dividers. Alert states follow a high-contrast logic: "Safe" states use a terminal-style phosphor green, while "Critical" states utilize a pure red, often paired with an orange stroke to signify immediate attention required in the field.

## Typography

This design system uses **JetBrains Mono** exclusively to maintain a consistent technical and monospaced rhythm. This ensures that columns of numerical data (coordinates, timestamps, chemical levels) remain perfectly aligned for rapid scanning.

Headlines should be set with tight tracking to feel dense and impactful. Labels and metadata should utilize the `label-caps` style to differentiate administrative descriptions from user-generated content. All weights are utilized to create a clear information hierarchy without needing to change font families.

## Layout & Spacing

The layout follows a **Fixed-Fluid Hybrid Grid** optimized for 1080p and 1440p desktop displays. A 12-column system is used for primary dashboard layouts, with a strict 4px baseline grid to maintain the industrial feel.

Margins and gutters are kept relatively tight to maximize data density. Use "Technical Padding" (equal spacing on all four sides of a container) to reinforce the boxy, modular nature of the campsite management tools. Content should be grouped into logical "Modules" that can be rearranged within the grid system.

## Elevation & Depth

In this design system, depth is communicated through **Bold Borders** and **Tonal Layering** rather than shadows. Shadows are strictly prohibited to avoid "softening" the industrial aesthetic.

1.  **Level 0 (Base):** Midnight Blue (#0A192F). The foundation.
2.  **Level 1 (Modules):** Graphite (#1B263B) with a 1px solid border (#2D3436).
3.  **Level 2 (Active/Hover):** Surfaces remain dark, but the border color shifts to Safety Orange or a lighter slate.

Visual stacking is achieved through inset strokes and high-contrast color blocks. For example, a header on a card should have a solid Graphite background to separate it from the card's body, rather than using a shadow.

## Shapes

The design system utilizes **Sharp (0px)** corners for all primary UI elements, including buttons, cards, and input fields. This zero-radius approach reinforces the industrial, rugged nature of the brand.

Small-scale elements like checkboxes or status pips must also remain square. The only exception to the sharp rule is for data visualizations (circles in scatter plots), but even these should be contained within rectangular, sharp-edged modules.

## Components

### Buttons
Primary buttons use a solid **Safety Orange** background with black text for maximum visibility. Secondary buttons use a transparent background with a 2px Safety Orange border. Interaction is signaled by a 45-degree corner-notch visual effect on hover (simulated via CSS clips or borders).

### Inputs & Fields
Inputs are Graphite-filled rectangles with a 1px slate border. When focused, the entire border turns Safety Orange. The label is always positioned above the input in `label-caps` style.

### High-Contrast Alerts
Alerts do not use soft tints. An "Emergency" alert is a solid red block with white JetBrains Mono text. For critical warnings, use a "Hazard Stripe" pattern (diagonal Orange and Black lines) for the header of the component.

### Data Chips
Chips are rectangular with a solid Graphite background and a vertical "status bar" on the left edge (Green for safe, Orange for warning, Red for alert).

### Monitoring Cards
These are the primary unit of the design system. They must feature a "Technical Header" containing a title and a unique ID number in a smaller font size. The body of the card should use the `code-data` typography for all metrics.