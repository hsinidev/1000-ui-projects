---
name: Sustainable-Tech System
colors:
  surface: '#121414'
  surface-dim: '#121414'
  surface-bright: '#383939'
  surface-container-lowest: '#0d0e0f'
  surface-container-low: '#1b1c1c'
  surface-container: '#1f2020'
  surface-container-high: '#292a2a'
  surface-container-highest: '#343535'
  on-surface: '#e3e2e2'
  on-surface-variant: '#c2c9bb'
  inverse-surface: '#e3e2e2'
  inverse-on-surface: '#303031'
  outline: '#8c9387'
  outline-variant: '#42493e'
  surface-tint: '#a1d494'
  primary: '#a1d494'
  on-primary: '#0a3909'
  primary-container: '#2d5a27'
  on-primary-container: '#9dd090'
  inverse-primary: '#3b6934'
  secondary: '#c8c6c5'
  on-secondary: '#313030'
  secondary-container: '#474746'
  on-secondary-container: '#b7b5b4'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#4e5051'
  on-tertiary-container: '#c2c2c3'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#bcf0ae'
  primary-fixed-dim: '#a1d494'
  on-primary-fixed: '#002201'
  on-primary-fixed-variant: '#23501e'
  secondary-fixed: '#e5e2e1'
  secondary-fixed-dim: '#c8c6c5'
  on-secondary-fixed: '#1c1b1b'
  on-secondary-fixed-variant: '#474746'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#121414'
  on-background: '#e3e2e2'
  surface-variant: '#343535'
typography:
  display-xl:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
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
    lineHeight: '1.6'
  data-mono:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  gutter: 24px
  margin: 32px
---

## Brand & Style

This design system centers on the intersection of rugged durability and advanced environmental technology. The brand personality is authoritative, sophisticated, and high-performance, targeting professional explorers and eco-conscious tech enthusiasts. 

The visual style is **High-Contrast Minimalism** infused with **Technical Data Visualization**. The UI should feel like a high-end instrument—precise, reliable, and efficient. To represent energy movement, the system utilizes "flow" lines—ultra-thin, animated or static vector paths—that connect data points and navigate the user through the interface, symbolizing the seamless transfer of solar power to device.

## Colors

The palette is anchored in **Charcoal (#1A1A1A)** to evoke the premium casing of high-end hardware, providing a deep, sophisticated canvas. **Forest Green (#2D5A27)** serves as the primary brand anchor, representing sustainability with a grounded, mature tone. 

**Crisp White (#FFFFFF)** is used exclusively for high-contrast typography and essential UI triggers, ensuring maximum legibility in outdoor or high-glare environments. An auxiliary **Accent Green (#4BA83F)** is reserved for active "flow" lines and "charging" states to provide a luminous, high-energy contrast against the dark background.

## Typography

The typography strategy employs a "dual-engine" approach. **Space Grotesk** is used for headlines, data points, and labels to provide a geometric, technical feel that mirrors engineering schematics. This font’s unique apertures and futuristic structure reinforce the "tech" aspect of the brand.

**Inter** is used for all long-form body text and functional descriptions. Its systematic, neutral design ensures that complex technical information remains highly readable and professional. All labels and data points should use uppercase styling with increased letter spacing to mimic industrial equipment labeling.

## Layout & Spacing

This design system utilizes a **Fixed Grid** model for desktop (12 columns, 1200px max-width) and a **Fluid Grid** for mobile. The rhythm is governed by an 8px base unit, ensuring mathematical precision across all components.

Layouts should prioritize "Information Density." Rather than excessive whitespace, use structured modules separated by clear margins. Energy "flow" lines should be positioned to guide the eye between these modules, effectively replacing traditional dividers with narrative-driven connectors.

## Elevation & Depth

Depth is achieved through **Tonal Layering** and **Low-Contrast Outlines** rather than traditional shadows. Surfaces are stacked using subtle variations of Charcoal:
1. **Base:** #1A1A1A (The void)
2. **Surface:** #242424 (Main containers)
3. **Overlay:** #2D2D2D (Modals and tooltips)

To define boundaries, use 1px "Hardware Borders" in #333333 or Forest Green. Glassmorphism is used sparingly, only for persistent navigation bars or floating status indicators, using a subtle backdrop blur (12px) to maintain focus on the technical data underneath.

## Shapes

The shape language is **Technical and Precise**. UI elements use a "Soft" (Level 1) roundedness (4px radius). This mimics the machined edges of outdoor gear—not sharp enough to be brittle, but not round enough to appear consumer-soft.

Data visualization components (progress bars, battery indicators) should use sharp corners or 2px radii to maintain a rigorous, instrument-like aesthetic. Interactive elements like buttons may use a slightly larger 8px radius (`rounded-lg`) to distinguish them from static data containers.

## Components

- **Buttons:** Primary buttons use a solid Forest Green background with White text. Secondary buttons are "Ghost" style with a 1px White or Green border and high-contrast labels.
- **Data Flow Cards:** Large containers for power metrics. They feature 1px Forest Green borders and integrate "flow" line animations that pulsate when active power is being generated.
- **Chips/Status Tags:** Used for "Live," "Eco," or "Max" modes. These use the `data-mono` type style and small, high-saturation color dots.
- **Inputs:** Dark fields (#111111) with a 1px Charcoal border that turns Forest Green on focus.
- **Energy Gauges:** Instead of circular charts, use linear horizontal "Power Strips" with segmented blocks to indicate capacity, reinforcing the durable, industrial feel.
- **Flow Lines:** 1px wide paths with a glow effect (`drop-shadow`) that connect input/output modules, visualizing the journey of energy from the solar panel to the battery.