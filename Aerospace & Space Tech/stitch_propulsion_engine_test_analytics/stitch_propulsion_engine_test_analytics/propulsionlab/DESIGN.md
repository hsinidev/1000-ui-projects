---
name: PropulsionLab
colors:
  surface: '#0c141a'
  surface-dim: '#0c141a'
  surface-bright: '#323a41'
  surface-container-lowest: '#070f15'
  surface-container-low: '#141d23'
  surface-container: '#182127'
  surface-container-high: '#222b32'
  surface-container-highest: '#2d363d'
  on-surface: '#dbe4ec'
  on-surface-variant: '#e0c0b2'
  inverse-surface: '#dbe4ec'
  inverse-on-surface: '#293138'
  outline: '#a88a7e'
  outline-variant: '#594238'
  surface-tint: '#ffb595'
  primary: '#ffb595'
  on-primary: '#571e00'
  primary-container: '#ee671c'
  on-primary-container: '#4c1a00'
  inverse-primary: '#a23f00'
  secondary: '#96ccff'
  on-secondary: '#003353'
  secondary-container: '#025483'
  on-secondary-container: '#8ec8fe'
  tertiary: '#c8c6c5'
  on-tertiary: '#313030'
  tertiary-container: '#929090'
  on-tertiary-container: '#2a2a2a'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbcd'
  primary-fixed-dim: '#ffb595'
  on-primary-fixed: '#351000'
  on-primary-fixed-variant: '#7c2e00'
  secondary-fixed: '#cee5ff'
  secondary-fixed-dim: '#96ccff'
  on-secondary-fixed: '#001d32'
  on-secondary-fixed-variant: '#004a75'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474746'
  background: '#0c141a'
  on-background: '#dbe4ec'
  surface-variant: '#2d363d'
typography:
  display-lg:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.02em
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0.01em
  data-mono:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  gutter: 16px
  margin: 24px
  panel-padding: 12px
  stack-compact: 8px
  stack-loose: 32px
---

## Brand & Style

The visual identity of the design system is rooted in the high-stakes environment of aerospace engineering and mission control. It evokes the feeling of a glass cockpit or a specialized diagnostic terminal used on a hangar floor. The aesthetic prioritizes utility and immediate data comprehension over decorative flair.

The design style is a hybrid of **High-Contrast Industrial** and **Tactile Minimalism**. It utilizes sharp geometries, "milled" interface edges, and a rigid adherence to technical grids. Every element must feel intentional, as if it were a physical component engineered to withstand extreme G-forces or thermal stress. The emotional response is one of absolute reliability, precision, and mission-critical focus.

## Colors

The palette is anchored by a deep **Charcoal (#1A1A1A)**, providing a low-glare foundation essential for long-duration monitoring. **Burnt Orange (#D35400)** is reserved for critical data points, active propulsion states, and primary calls to action, mirroring the heat and energy of a rocket exhaust. **Steel Blue (#4682B4)** provides a technical contrast, used for steady-state telemetry, secondary navigation, and interactive data visualization.

Neutrals are biased toward cool, metallic tones to reinforce the industrial hardware metaphor. Functional colors for success and warnings are slightly desaturated to maintain the professional, understated tone of the design system.

## Typography

Typography in this design system balances the futuristic, geometric qualities of **Space Grotesk** with the utilitarian clarity of **Inter**. 

Headlines utilize Space Grotesk to provide a technical, "engineered" look for section headers and large telemetry readouts. All body copy and tabular data utilize Inter for its exceptional legibility at small scales. To enhance the mechanical feel, labels and small metadata often use uppercase styling with increased letter spacing, mimicking the etched plates found on physical hardware.

## Layout & Spacing

The layout philosophy follows a **High-Density Fluid Grid**. Efficiency is paramount; the design system maximizes information density to ensure engineers can monitor multiple variables without excessive scrolling. 

A 4px baseline grid ensures all components align with mathematical precision. Layouts are typically structured into collapsible panels and modular widgets, allowing for a customizable dashboard experience. Margin and padding are kept tight to minimize wasted space, while clear vertical dividers help separate distinct data streams.

## Elevation & Depth

This design system eschews soft, ambient shadows in favor of **Tonal Layers** and **Milled Borders**. Depth is communicated through color value shifts and hairline strokes:

1.  **Base Layer:** The deepest Charcoal (#1A1A1A) for the primary application background.
2.  **Panel Layer:** A slightly lighter surface (#242424) for widgets and data containers.
3.  **Inset Depth:** Inner shadows and 1px dark borders are used for input fields and status wells to make them look "recessed" into the hardware.
4.  **Interactive Layer:** High-contrast Steel Blue or Burnt Orange borders indicate focus or active states. 

Glossy overlays are used sparingly to simulate glass screens over certain chart components.

## Shapes

The shape language is strictly **Sharp (0px roundedness)**. This reinforces the industrial, heavy-machinery aesthetic and ensures that high-density components fit together perfectly without visual gaps. 

Structural elements such as buttons, cards, and input fields must maintain 90-degree corners. The only exceptions are circular status LEDs and specific oscilloscope chart nodes, where geometric primitive shapes are necessary for functional clarity.

## Components

### Buttons & Controls
Buttons are "ruggedized," featuring high-contrast borders and clear state changes. The primary action button uses a solid Burnt Orange fill with white text. Secondary actions use the Steel Blue as a ghost-style border. Toggle switches should mimic heavy-duty physical rockers, with a clear "active" glow indicator.

### Data Grids
Tables are high-density, utilizing thin borders between rows. Header cells use the `label-caps` typography style with a darker background to distinguish them from data rows. Hover states should highlight the entire row in a subtle Steel Blue tint.

### Oscilloscope Charts
Charts use a "CRT glow" effect. Lines are thin (1px to 1.5px) and use Steel Blue or Burnt Orange. A subtle background grid is required for all temporal charts, and data points should appear as sharp, square pips rather than rounded dots.

### Status Indicators
Indicators mimic physical hardware LEDs. They should have three states: Off (dim), Pulse (warning), and Steady (active). Use a high-saturation version of the system colors to simulate light emission.

### Segmented Controls
Used for switching between telemetry views, these appear as a single milled block where the active segment is "depressed" into the surface using a darker background and an inner shadow.