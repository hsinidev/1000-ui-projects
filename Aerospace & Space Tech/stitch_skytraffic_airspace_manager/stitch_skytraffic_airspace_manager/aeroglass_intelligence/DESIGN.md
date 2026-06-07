---
name: AeroGlass Intelligence
colors:
  surface: '#101415'
  surface-dim: '#101415'
  surface-bright: '#363a3b'
  surface-container-lowest: '#0b0f10'
  surface-container-low: '#191c1e'
  surface-container: '#1d2022'
  surface-container-high: '#272a2c'
  surface-container-highest: '#323537'
  on-surface: '#e0e3e5'
  on-surface-variant: '#c7c4d7'
  inverse-surface: '#e0e3e5'
  inverse-on-surface: '#2d3133'
  outline: '#908fa0'
  outline-variant: '#464554'
  surface-tint: '#c0c1ff'
  primary: '#c0c1ff'
  on-primary: '#1000a9'
  primary-container: '#8083ff'
  on-primary-container: '#0d0096'
  inverse-primary: '#494bd6'
  secondary: '#bec6e0'
  on-secondary: '#283044'
  secondary-container: '#3f465c'
  on-secondary-container: '#adb4ce'
  tertiary: '#4cd6ff'
  on-tertiary: '#003543'
  tertiary-container: '#009dc1'
  on-tertiary-container: '#002e3a'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e1e0ff'
  primary-fixed-dim: '#c0c1ff'
  on-primary-fixed: '#07006c'
  on-primary-fixed-variant: '#2f2ebe'
  secondary-fixed: '#dae2fd'
  secondary-fixed-dim: '#bec6e0'
  on-secondary-fixed: '#131b2e'
  on-secondary-fixed-variant: '#3f465c'
  tertiary-fixed: '#b7eaff'
  tertiary-fixed-dim: '#4cd6ff'
  on-tertiary-fixed: '#001f28'
  on-tertiary-fixed-variant: '#004e60'
  background: '#101415'
  on-background: '#e0e3e5'
  surface-variant: '#323537'
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
  body-base:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  data-mono:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  gutter: 20px
  margin-edge: 32px
---

## Brand & Style

The design system is engineered for the high-stakes environment of air traffic and drone coordination. It evokes a sense of absolute precision, technical authority, and futuristic innovation. The aesthetic centers on "Aerodynamic Glassmorphism"—a style that prioritizes depth and layering to organize complex data without overwhelming the operator.

The UI should feel like a heads-up display (HUD) in a modern cockpit: sophisticated, responsive, and ultra-high-tech. By utilizing translucent layers and glowing accents, the design system maintains a sense of lightness and speed, ensuring that even data-dense screens feel breathable and navigable.

## Colors

The palette is anchored in a deep, nocturnal foundation to minimize eye strain during long-duration monitoring.

- **Deep Navy:** Used for the primary application canvas and base layout containers.
- **Electric Indigo:** The primary action color, used for interactive elements, primary buttons, and active flight paths.
- **Cyan/Tertiary:** Reserved for secondary telemetry data and drone-specific indicators.
- **White/Neutral:** Used for high-contrast typography and essential highlights.
- **Glow States:** Alerts and critical warnings utilize high-saturation reds and ambers with outer glow effects (bloom) to ensure immediate peripheral recognition.

## Typography

This design system employs a dual-font strategy. **Space Grotesk** provides a technical, geometric edge for headlines, labels, and telemetry data, reinforcing the aerodynamic theme. **Inter** is used for body copy and dense instructional text to ensure maximum legibility and neutral tone.

For data readouts (lat/long, altitude, velocity), use the "data-mono" style to ensure character alignment and rapid scanning. Uppercase styling is preferred for utility labels and system status indicators to evoke military and aviation standards.

## Layout & Spacing

The layout utilizes a 12-column fluid grid system that prioritizes a "Center-Out" hierarchy. The most critical spatial data (maps/radar) occupies the central viewport, while modular glass panels are docked to the edges or float as overlays.

Spacing follows a strict 4px baseline. Components should use generous internal padding (16px–24px) to maintain the "clean" feel despite high data density. Group related telemetry in clusters with 8px gaps, while major UI sections are separated by 40px margins to create distinct cognitive zones.

## Elevation & Depth

Depth is conveyed through **Glassmorphism** rather than traditional drop shadows. 

- **Base Layer:** The Deep Navy background, representing the "void."
- **Mid-Level (Surfaces):** Translucent layers with a 20px–40px backdrop blur and 15% opacity Indigo or Navy fill.
- **High-Level (Active/Modals):** Increased opacity and a secondary 1px "inner-glow" border (Electric Indigo at 30% opacity) to signify focus.
- **Borders:** All glass panels must feature a refined, 1px solid border. Use a linear gradient for borders (Top-Left to Bottom-Right) ranging from White (20% opacity) to Transparent to simulate light hitting an edge.

## Shapes

The shape language is inspired by aerodynamic profiles—sleek, rounded, and frictionless. 

A base roundedness of 0.5rem (8px) is applied to standard buttons and input fields. Larger containers and floating glass panels use 1.5rem (24px) to create a softer, more sophisticated silhouette. Avoid sharp 90-degree angles to maintain the high-tech, engineered feel of the design system.

## Components

- **Glass Buttons:** Primary buttons feature a semi-transparent Indigo fill with a 2px outer glow on hover. Secondary buttons are "Ghost" style with only a refined 1px border.
- **Telemetry Chips:** Small, pill-shaped indicators for drone status. They use high-saturation accent colors (Cyan, Green, Red) with a slight "pulse" animation for active tracking.
- **Data-Dense Cards:** Backgrounds must use backdrop-blur (saturate 150%, blur 20px). Headers within cards should have a subtle bottom-border to separate metadata from primary values.
- **Input Fields:** Minimalist design with only a bottom-border that glows Electric Indigo when focused.
- **Active Paths:** On-map flight paths should be rendered as glowing poly-lines with a gradient trail to indicate direction of travel and velocity.
- **Alert HUDs:** Critical system alerts should use a "scanning" animation across the glass panel to draw immediate operator attention.