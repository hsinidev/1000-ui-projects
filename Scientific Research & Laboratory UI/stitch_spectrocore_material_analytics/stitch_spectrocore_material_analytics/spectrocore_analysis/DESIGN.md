---
name: SpectroCore Analysis
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#b9cacb'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#849495'
  outline-variant: '#3a494b'
  surface-tint: '#00dce6'
  primary: '#e3fdff'
  on-primary: '#00373a'
  primary-container: '#00f3ff'
  on-primary-container: '#006b71'
  inverse-primary: '#00696f'
  secondary: '#c6c6cf'
  on-secondary: '#2f3037'
  secondary-container: '#45464e'
  on-secondary-container: '#b4b4bd'
  tertiary: '#fbf8f7'
  on-tertiary: '#303030'
  tertiary-container: '#dedbdb'
  on-tertiary-container: '#616060'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#6ff6ff'
  primary-fixed-dim: '#00dce6'
  on-primary-fixed: '#002022'
  on-primary-fixed-variant: '#004f53'
  secondary-fixed: '#e2e1eb'
  secondary-fixed-dim: '#c6c6cf'
  on-secondary-fixed: '#1a1b22'
  on-secondary-fixed-variant: '#45464e'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1b1b1c'
  on-tertiary-fixed-variant: '#474746'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
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
    lineHeight: '1.2'
  body-lg:
    fontFamily: Space Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.5'
  body-md:
    fontFamily: Space Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  body-sm:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.4'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
  mono-data:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.02em
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  sidebar-width: 280px
  telemetry-panel: 320px
  gutter: 12px
---

## Brand & Style

This design system targets high-precision laboratory and industrial environments where speed and data accuracy are paramount. The "Dark Lab" aesthetic projects a technical, futuristic personality—evoking the feeling of a sophisticated instrument panel rather than a standard software interface. 

The visual style blends **Minimalism** with **High-Contrast Neon accents**. It utilizes a "matte-on-black" layering strategy to manage data density without visual clutter. The emotional response is one of controlled authority, reliability, and high-tech immersion. Design elements are sharp and intentional, prioritizing legibility and functional telemetry over decorative flair.

## Colors

The palette is anchored by a deep matte black (#131313) which serves as the canvas for all analytical activities. Neon Cyan (#00F3FF) is reserved strictly for active states, primary actions, and critical data points, providing a "high-energy" contrast that guides the eye.

Silver and gray structural elements (#A1A1AA) define borders and inactive states, ensuring the interface feels industrial and solid. Background tiers are created using subtle shifts in dark grays to separate toolbars from the main analysis workspace. Functional colors (red, yellow, green) are desaturated slightly but remain vivid enough to pierce the dark UI for immediate status recognition.

## Typography

This design system exclusively utilizes **Space Grotesk** to maintain a technical, geometric edge across all interfaces. The typeface's open apertures ensure legibility at small sizes, which is critical for high-density telemetry.

Hierarchy is established through weight shifts and the strategic use of uppercase tracking for labels. "Display" sizes are used sparingly for hero metrics, while the "Mono-data" style (achieved through medium weights and specific letter spacing) is utilized for all numerical readouts, sensor data, and coordinate systems to simulate a fixed-width technical readout.

## Layout & Spacing

The layout utilizes a **Fluid Grid** model designed for 16:9 and ultrawide desktop displays. The screen is divided into a multi-pane architecture: a persistent left navigation sidebar, a main analytical viewport, and a collapsible right-side telemetry panel.

The spacing rhythm is based on a **4px base unit** to allow for tight, data-dense configurations. Gutters are kept narrow (12px) to maximize the "surface-to-data" ratio. Modules within the main viewport should use a 12-column sub-grid to allow for flexible arrangements of charts, code editors, and 3D visualizations.

## Elevation & Depth

Depth is conveyed through **Tonal Layers** and **Low-Contrast Outlines**. In the dark-lab environment, traditional shadows are avoided to maintain the matte aesthetic.

1.  **Level 0 (Base):** #131313 - The primary application background.
2.  **Level 1 (Panels):** #1E1E1E - Used for sidebars and header bars.
3.  **Level 2 (Cards/Modules):** #252525 - Floating modules within the viewport.

To define boundaries, elements use 1px solid borders in #2D2D2D. Active or focused elements receive a "glow" effect not through shadows, but through a 1px #00F3FF stroke and a subtle, 4px blur of the same color strictly confined to the border region.

## Shapes

The design system employs **Sharp (0px)** corners for all structural elements, including buttons, panels, and input fields. This reinforces the industrial, precision-instrument feel. 

Small exceptions are made for inner status indicators (e.g., circular "live" pips), but all containers, containers' borders, and interactive surfaces must maintain 90-degree angles to align with the rigid grid architecture.

## Components

**Buttons:** Primary buttons are solid Neon Cyan with black text. Secondary buttons are ghost-style with a silver stroke and silver text. Inverted hover states (filling the background) are preferred.

**Input Fields:** Minimalist design with only a bottom border in silver. On focus, the border transitions to Neon Cyan with a technical coordinate label (e.g., `[INPUT.ALPHA]`) appearing in the top right.

**Telemetry Chips:** Small, rectangular tags with #1E1E1E backgrounds and monochromatic icons. They are used for toggling data overlays or displaying metadata.

**Data Grids:** High-density tables with no vertical lines. Horizontal dividers are 1px #2D2D2D. Row hovering should trigger a subtle brightness increase rather than a color change.

**Multi-Pane Dividers:** Draggable handles marked with a 3-dot vertical silver pattern. Dividers are 2px wide to ensure precision interaction.

**Additional Components:** 
- **Sparklines:** Compact, colorless line graphs for inline trend analysis.
- **Terminal Consoles:** Dedicated bottom-pane for raw system logs using the Mono-data type style.
- **Status Beacons:** Small pulsing neon pips to indicate active data streams.