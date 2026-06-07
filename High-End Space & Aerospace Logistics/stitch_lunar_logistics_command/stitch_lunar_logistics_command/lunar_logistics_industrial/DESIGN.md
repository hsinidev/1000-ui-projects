---
name: Lunar-Logistics Industrial
colors:
  surface: '#1d100a'
  surface-dim: '#1d100a'
  surface-bright: '#47352e'
  surface-container-lowest: '#180b06'
  surface-container-low: '#261812'
  surface-container: '#2b1c16'
  surface-container-high: '#362620'
  surface-container-highest: '#42312a'
  on-surface: '#f8ddd2'
  on-surface-variant: '#e3bfb1'
  inverse-surface: '#f8ddd2'
  inverse-on-surface: '#3d2d26'
  outline: '#aa8a7d'
  outline-variant: '#5a4136'
  surface-tint: '#ffb596'
  primary: '#ffb596'
  on-primary: '#581e00'
  primary-container: '#ff6600'
  on-primary-container: '#561d00'
  inverse-primary: '#a33e00'
  secondary: '#c7c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#c8c6c5'
  on-tertiary: '#313030'
  tertiary-container: '#989696'
  on-tertiary-container: '#2f2f2f'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbcd'
  primary-fixed-dim: '#ffb596'
  on-primary-fixed: '#360f00'
  on-primary-fixed-variant: '#7c2e00'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c7c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474746'
  background: '#1d100a'
  on-background: '#f8ddd2'
  surface-variant: '#42312a'
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
  headline-sm:
    fontFamily: Space Grotesk
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.2'
  body-lg:
    fontFamily: JetBrains Mono
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Archivo Narrow
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.1em
  data-display:
    fontFamily: JetBrains Mono
    fontSize: 18px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
spacing:
  unit: 4px
  gutter: 16px
  margin: 24px
  border-width: 2px
  border-width-heavy: 3px
---

## Brand & Style

The visual identity of this design system is built on **Mission-Critical Brutalism**. It prioritizes utility, durability, and technical precision, reflecting the harsh, high-stakes environment of lunar supply chain management. The brand personality is uncompromisingly industrial, drawing inspiration from aerospace interfaces, heavy machinery decals, and structural engineering schematics.

The target audience consists of logistics commanders and site engineers who require immediate access to complex data without visual distractions. The UI should evoke a sense of "hardened" hardware—software that feels like it was etched into a bulkhead. Expect high-contrast interactions, dense information displays, and a total absence of decorative flourishes.

## Colors

This design system utilizes a high-contrast, functional palette designed for legibility in low-light environments. 

- **Matte Black (#1A1A1A):** Serves as the primary void, used for the main background to minimize eye strain and simulate the lunar horizon.
- **Safety Orange (#FF6600):** Reserved strictly for primary actions, warnings, and mission-critical status indicators. It is the "active" energy of the system.
- **Lunar Grey (#A9A9A9):** Used for structural elements, borders, and secondary text, providing a neutral, metallic middle ground.
- **Accent Highlighting:** Status indicators use pure, high-saturation colors (Critical Red, Nominal Green) to ensure zero ambiguity during rapid data scanning.

## Typography

The typographic hierarchy is split between structural wayfinding and technical data. 

- **Structural Headers:** Uses **Space Grotesk** for a futuristic, geometric feel that remains legible at large scales.
- **Technical Data:** Uses **JetBrains Mono** for all body text and data tables. The monospaced nature ensures that fluctuating numerical values (coordinates, fuel levels, timestamps) do not cause layout shifts.
- **System Labels:** Uses **Archivo Narrow** for compact, high-density labeling of controls and status chips, maximizing screen real estate in complex dashboards.

## Layout & Spacing

This design system employs a **Rigid Grid** philosophy. All layouts are based on a 4px baseline grid to ensure mathematical alignment of technical data. 

- **Grid Model:** A standard 12-column fixed grid for desktop, collapsing to a 4-column grid for mobile handheld units.
- **Density:** Information density is high. Padding is kept to the functional minimum required for touch targets and legibility.
- **Containers:** Content is housed in "Hardened Containers"—panels defined by heavy 2px or 3px borders. There is no fluid white space; every pixel is utilized for data or structural reinforcement.

## Elevation & Depth

In this design system, depth is conveyed through **Structural Tiering** rather than shadows. The concept of "above" or "below" is discarded in favor of "active" versus "background."

- **Zero Shadows:** Light sources are non-existent in this UI. No drop shadows or ambient occlusions are used.
- **Border-Based Hierarchy:** Primary panels use a 3px **Lunar Grey** border. Sub-elements or nested modules use 2px borders.
- **Inverted Surfaces:** Active states or "raised" elements are represented by inverting colors (e.g., Safety Orange background with Matte Black text) rather than physical elevation.
- **Occlusion:** Overlays (modals) are handled by a solid, high-opacity Matte Black fill with a 3px Safety Orange border to indicate an "Emergency Interrupt" state.

## Shapes

The shape language is defined as **Hardened**. To reinforce the industrial nature of the supply chain, all corners are strictly sharp (0px) or marginally eased (maximum 4px) for physical handheld durability metaphors.

- **Primary Radius:** 0px. Use for all main structural panels, layout containers, and data grids.
- **Secondary Radius:** 4px. Use exclusively for interactive components like buttons and input fields to differentiate them from static structural elements.
- **Angled Geometry:** Decorative elements may use 45-degree chamfered corners to mimic aerospace structural plates and "Cut Here" decals.

## Components

### Buttons & Controls
Buttons are high-contrast blocks. The **Primary Action** button uses a solid Safety Orange fill with Matte Black JetBrains Mono text. The **Secondary Action** uses a Matte Black fill with a 2px Lunar Grey border. All buttons use 0px - 4px corners and a 45-degree "clipped corner" effect on the top-right to denote interactivity.

### Data Grids
Data is the core of the supply chain. Grids must feature 1px Lunar Grey dividers between rows and 2px borders for the container. Header rows should be inverted (Lunar Grey background, Matte Black text).

### Status Indicators
Status indicators are "warning lights." They consist of a label in Archivo Narrow and a square indicator box. A "Critical" state uses a flashing Safety Orange or Solid Red border. 

### Input Fields
Fields are Matte Black with a 2px Lunar Grey border. Upon focus, the border thickness increases to 3px and changes to Safety Orange. Monospaced font is mandatory for all inputs to ensure alignment with read-only data.

### Mission-Specific Components
- **Telemetry Readout:** A specialized card for real-time tracking, featuring a "Scanline" texture overlay.
- **Hazard Badge:** High-visibility tags for dangerous cargo, using diagonal Safety Orange and Matte Black stripes (hazard pattern).