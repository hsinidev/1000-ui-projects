---
name: Engineering-Sleek
colors:
  surface: '#121414'
  surface-dim: '#121414'
  surface-bright: '#37393a'
  surface-container-lowest: '#0c0f0f'
  surface-container-low: '#1a1c1c'
  surface-container: '#1e2020'
  surface-container-high: '#282a2b'
  surface-container-highest: '#333535'
  on-surface: '#e2e2e2'
  on-surface-variant: '#c3c6d5'
  inverse-surface: '#e2e2e2'
  inverse-on-surface: '#2f3131'
  outline: '#8d909e'
  outline-variant: '#434653'
  surface-tint: '#b1c5ff'
  primary: '#b1c5ff'
  on-primary: '#002c70'
  primary-container: '#0047ab'
  on-primary-container: '#a5bdff'
  inverse-primary: '#2559bd'
  secondary: '#b5c7ea'
  on-secondary: '#1f314d'
  secondary-container: '#364765'
  on-secondary-container: '#a4b6d8'
  tertiary: '#c6c6c6'
  on-tertiary: '#2f3131'
  tertiary-container: '#4c4d4d'
  on-tertiary-container: '#bebebe'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dae2ff'
  primary-fixed-dim: '#b1c5ff'
  on-primary-fixed: '#001946'
  on-primary-fixed-variant: '#00419e'
  secondary-fixed: '#d6e3ff'
  secondary-fixed-dim: '#b5c7ea'
  on-secondary-fixed: '#071c37'
  on-secondary-fixed-variant: '#364765'
  tertiary-fixed: '#e3e2e2'
  tertiary-fixed-dim: '#c6c6c6'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#464747'
  background: '#121414'
  on-background: '#e2e2e2'
  surface-variant: '#333535'
typography:
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0em
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
  technical-mono:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: 0.05em
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  gutter: 24px
  margin: 40px
---

## Brand & Style

This design system is built for the sophisticated hobbyist, prioritizing technical precision and architectural integrity. The brand personality is clinical, professional, and modular, reflecting the exacting standards of structural engineering. 

The visual style draws heavily from **Minimalism** and **Modern Corporate** movements, but with a structural twist: it utilizes "schematic" aesthetics. It replaces decorative elements with functional ones—visible grid lines, coordinate systems, and technical notations. The UI should evoke the feeling of a high-end CAD workstation or a physical architectural blueprint laid out on a professional drafting table.

## Colors

The palette is rooted in the "Blueprint" aesthetic. The default mode is **dark**, using Slate Blue as the primary canvas to mimic heavy-duty drafting paper. 

- **Blueprint Blue (#0047AB):** Used for primary actions, active states, and focal points of progress.
- **Slate Blue (#1C2E4A):** The foundational background color, providing a deep, professional depth.
- **Silver (#C0C0C0):** Reserved for technical borders, dividers, and inactive structural elements, mimicking aluminum and steel.
- **Stark White (#FFFFFF):** Utilized for high-contrast labels and critical data readouts to ensure maximum legibility against dark backgrounds.

## Typography

Typography in this design system functions as a data-delivery mechanism. **Space Grotesk** is used for headlines to provide a sharp, geometric edge that feels engineered. **Inter** is used for all functional body text and labels due to its utilitarian clarity.

Technical labels should always be presented in uppercase with increased letter spacing to mimic architectural notations. Numeric data and measurements should use the `technical-mono` style to ensure vertical alignment and a "read-out" feel.

## Layout & Spacing

This design system adheres to a **Fixed 12-column grid** system with a strict 8px baseline. Precision is paramount; every element must snap to the grid. 

Layouts are defined by "Zones." Use Silver (#C0C0C0) 1px borders to define these zones, creating a modular appearance where the interface looks like it was assembled from discrete components. Gutters are fixed at 24px to ensure breathing room between technical data blocks. Whitespace should be used intentionally to separate different "modules" of the assembly instructions or product specs.

## Elevation & Depth

Depth is conveyed through **Bold Borders and Tonal Layers** rather than shadows. This maintains a flat, technical drafting feel.

- **Level 0 (Base):** Slate Blue (#1C2E4A) background.
- **Level 1 (Panels):** Surfaces slightly lighter than the base, defined by a 1px Silver border.
- **Level 2 (Modals/Pop-overs):** Defined by a thicker 2px Blueprint Blue border to denote focus.
- **Intersections:** Use small "crosshair" icons or "+" marks at the corners of containers where grid lines meet to reinforce the engineering aesthetic.

Avoid all ambient shadows. If a "raised" effect is required, use a high-contrast Stark White top-border to simulate a technical highlight.

## Shapes

The shape language is strictly **Sharp (0px)**. Roundness contradicts the architectural and modular nature of the product. Every button, input field, card, and container must have perfectly square corners. This reinforces the "brick" and "structural component" metaphor, suggesting that every UI element is a precisely machined part.

## Components

### Buttons
Primary buttons are solid Blueprint Blue with Stark White text, strictly rectangular. Secondary buttons are transparent with a 1px Silver border. All buttons should feature a small "Ref ID" or coordinate in the corner in 8pt type to enhance the technical feel.

### Input Fields
Fields consist of a Slate Blue background and a bottom-only 1px Silver border. The label sits above the field in `label-caps` style, accompanied by a technical prefix (e.g., "FLD_01 >").

### Cards & Modules
Cards are containers for product kits. They must feature a 1px Silver border and a "Header Block" containing the kit’s serial number and scale. Use thin blueprint-style grid lines as a background pattern for image containers.

### Data Visualization
Use 1px line weights for all charts and diagrams. High-contrast labels should be placed at the end of leader lines (thin lines connecting data points to text), mirroring architectural callouts.

### Progress Indicators
Progress is shown through segmented bars (individual blocks) rather than a smooth continuous line, emphasizing the modular "brick" nature of the assembly process.