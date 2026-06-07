---
name: Kinetic Grid
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
  on-surface-variant: '#e3bfb1'
  inverse-surface: '#e2e2e2'
  inverse-on-surface: '#2f3131'
  outline: '#aa8a7d'
  outline-variant: '#5a4136'
  surface-tint: '#ffb595'
  primary: '#ffb595'
  on-primary: '#571e00'
  primary-container: '#ff6700'
  on-primary-container: '#561e00'
  inverse-primary: '#a23f00'
  secondary: '#c8c6c7'
  on-secondary: '#303031'
  secondary-container: '#49494a'
  on-secondary-container: '#bab8b9'
  tertiary: '#c8c6c7'
  on-tertiary: '#303031'
  tertiary-container: '#989798'
  on-tertiary-container: '#303031'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbcd'
  primary-fixed-dim: '#ffb595'
  on-primary-fixed: '#351000'
  on-primary-fixed-variant: '#7c2e00'
  secondary-fixed: '#e5e2e3'
  secondary-fixed-dim: '#c8c6c7'
  on-secondary-fixed: '#1b1b1c'
  on-secondary-fixed-variant: '#474647'
  tertiary-fixed: '#e4e2e3'
  tertiary-fixed-dim: '#c8c6c7'
  on-tertiary-fixed: '#1b1b1c'
  on-tertiary-fixed-variant: '#474648'
  background: '#121414'
  on-background: '#e2e2e2'
  surface-variant: '#333535'
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
  body-base:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  data-mono:
    fontFamily: Space Grotesk
    fontSize: 18px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  gutter: 16px
  margin: 24px
  container-max: 1440px
---

## Brand & Style

The design system is engineered for high-performance residential energy management. It targets tech-literate homeowners and industrial engineers who value precision, reliability, and real-time data transparency. The UI evokes the feeling of a professional command center—utilitarian, authoritative, and sophisticated.

The aesthetic follows a **High-Contrast / Technical Brutalism** style. It prioritizes raw data density and functional clarity over decorative softness. Visual interest is generated through geometric "Flow" lines that represent electrical currents and hardware-inspired structural layouts. The environment is unapologetically dark, mirroring the premium hardware of solar inverters and battery enclosures.

## Colors

The palette is rooted in industrial safety and hardware aesthetics. 

- **Primary (Safety Orange):** Reserved for active energy states, primary CTAs, and critical system alerts. It must be used sparingly to maintain its "warning/action" psychological impact.
- **Secondary (Charcoal):** The foundation of the UI. Used for the deep background to reduce eye strain and provide a canvas for glowing data visualizations.
- **Tertiary (Graphite):** Used for component surfaces and card backgrounds to create subtle layering against the Charcoal base.
- **Neutral (White):** Used exclusively for high-readability typography and iconography. 
- **Support Colors:** Success Green and Alert Red are saturated and bright, ensuring system statuses are unmistakable at a glance.

## Typography

This design system utilizes a dual-font strategy to balance technical character with readability.

- **Space Grotesk** is used for headlines, labels, and numeric data displays. Its geometric construction reinforces the "tech-industrial" narrative. All uppercase labels should have increased letter spacing for a blueprint-inspired look.
- **Inter** is used for body copy and descriptions. It provides a neutral, highly legible contrast to the more expressive headers, ensuring long-form technical data is easily digestible.
- **Numeric Data:** Live metrics should always use Space Grotesk to emphasize the technical nature of the energy output.

## Layout & Spacing

This design system employs a **Fixed Grid** model on desktop and a **Fluid Grid** on mobile. The layout is built on a strict 4px baseline grid to ensure mathematical alignment of all technical components.

- **Grid:** 12-column layout with 16px gutters.
- **Rhythm:** Use multiples of 4px for all padding and margins to maintain a tight, engineered feel.
- **Visual Flow:** Elements are connected by "flow lines"—1px borders that extend vertically or horizontally to guide the eye between related data points (e.g., from Solar Array to Battery Storage).

## Elevation & Depth

In this dark-mode-first environment, depth is conveyed through **Tonal Layers** and **Low-Contrast Outlines** rather than traditional shadows.

1.  **Base (Level 0):** Charcoal (#1A1A1B) for the main application canvas.
2.  **Surface (Level 1):** Graphite (#2E2E2F) for cards and containers, defined by a 1px solid border (#3E3E3F) rather than a shadow.
3.  **Active (Level 2):** Elements in focus or "live" states may feature a subtle Safety Orange inner glow or a high-contrast white border.

Shadows are avoided entirely to maintain the "flat" industrial schematic aesthetic.

## Shapes

The shape language is defined by **Sharp Corners (0px)**. This reinforces the architectural and industrial nature of the brand.

- **Buttons & Cards:** Must have 90-degree angles. No radii are permitted.
- **Status Badges:** May use a slight chamfered corner (clipped corner) effect if specific differentiation is needed, but should default to sharp rectangles.
- **Icons:** Should use consistent stroke weights (2px) with sharp joins and square caps.

## Components

- **Buttons:** High-contrast blocks. Primary buttons use a solid Safety Orange fill with White or Black text. Secondary buttons use a transparent fill with a 2px White border.
- **Data Cards:** Sharp-edged containers with a 1px border. Headlines within cards should use the `label-caps` style for a "serial number" feel.
- **Status Badges:** Use a "Signal Lamp" metaphor—a small, high-intensity colored square next to uppercase text.
- **Technical Charts:** Line charts should use 2px stroke widths with no smoothing (angular transitions). Area charts use a 10% opacity fill of the stroke color.
- **Live Metrics:** Large-scale numbers using `data-mono` typography, paired with a small unit label (e.g., "kW" or "kWh") in a lighter weight.
- **Input Fields:** Minimalist design with a bottom-border only or a very thin 1px frame. Active states are indicated by the Safety Orange color.
- **Energy Flow Indicators:** Animated 1px lines that use a "dash-array" animation to show the direction of electricity moving between components.