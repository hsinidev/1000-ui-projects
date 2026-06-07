---
name: Aero-Range Design System
colors:
  surface: '#0d1228'
  surface-dim: '#0d1228'
  surface-bright: '#333850'
  surface-container-lowest: '#080d22'
  surface-container-low: '#151a31'
  surface-container: '#191e35'
  surface-container-high: '#242940'
  surface-container-highest: '#2f334b'
  on-surface: '#dde1ff'
  on-surface-variant: '#c1c7ce'
  inverse-surface: '#dde1ff'
  inverse-on-surface: '#2a2f47'
  outline: '#8b9198'
  outline-variant: '#41484d'
  surface-tint: '#9accf3'
  primary: '#e1f0ff'
  on-primary: '#00344d'
  primary-container: '#a5d8ff'
  on-primary-container: '#285f80'
  inverse-primary: '#2e6385'
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#eeeeee'
  on-tertiary: '#2f3131'
  tertiary-container: '#d1d2d2'
  on-tertiary-container: '#585a5a'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#c9e6ff'
  primary-fixed-dim: '#9accf3'
  on-primary-fixed: '#001e2f'
  on-primary-fixed-variant: '#0c4b6c'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#0d1228'
  on-background: '#dde1ff'
  surface-variant: '#2f334b'
typography:
  display-hero:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  data-lg:
    fontFamily: JetBrains Mono
    fontSize: 36px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.1em
  caption-technical:
    fontFamily: JetBrains Mono
    fontSize: 10px
    fontWeight: '400'
    lineHeight: '1.2'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  micro: 4px
  base: 8px
  md: 16px
  lg: 24px
  xl: 40px
  container-padding: 32px
---

## Brand & Style

The design system is engineered for high-performance electric vehicle environments where aerodynamic efficiency is paramount. It bridges the gap between professional laboratory instrumentation and luxury automotive aesthetics. The brand personality is cold, calculating, and elite.

The visual style is defined by **Scientific Glassmorphism**. This involves multi-layered translucent surfaces that suggest depth and complex data processing. The aesthetic utilizes high-contrast technical backgrounds to make glowing data lines and 3D wireframes pop with clarity. Every element must feel intentional and measured, using precise technical borders and "light-leak" accents to simulate a high-end HUD (Heads-Up Display).

## Colors

The color palette is anchored by **Deep Space Navy (#0B1026)**, providing a void-like canvas that minimizes glare during high-speed driving. 

- **Ice Blue (#A5D8FF)**: Used for primary data readouts, active states, and glowing accents. It represents the "cool" efficiency of optimal airflow.
- **Silver (#C0C0C0)**: Applied to secondary labels, inactive states, and structural wireframes to provide a metallic, mechanical feel.
- **Clean White (#FFFFFF)**: Reserved for critical alerts, high-level headers, and the brightest points of light in the glassmorphism effects.
- **Glow Accents**: Utilize semi-transparent versions of Ice Blue with additive blending to create the "Laboratory Instrument" luminescence.

## Typography

This design system employs a tiered typographic approach to ensure split-second readability. 

- **Space Grotesk** is used for primary headings and display titles, lending a futuristic and structural tone.
- **Inter** handles standard UI text and descriptions, providing maximum legibility against complex glass backgrounds.
- **JetBrains Mono** is the "Technical Engine" of the system, used for all numerical data readouts, gauges, and status labels. The monospaced nature ensures that fluctuating numbers do not cause layout shifts.

All labels should utilize the `label-caps` style to mimic printed technical specifications on hardware.

## Layout & Spacing

The layout philosophy follows a **Fixed Technical Grid**. Content is organized into modular "Data Bays" that align to a 12-column structure. 

- **Desktop/In-Dash**: A rigid 12-column layout with 16px gutters. Elements should feel like they are "bolted" into the interface.
- **Information Density**: High density is preferred. Spacing is tight (8px–16px) between related data points to maximize the amount of telemetry visible at once.
- **Safe Zones**: Ensure a 40px margin from all screen edges to account for bezel interference in physical vehicle cockpits.

## Elevation & Depth

Depth in this design system is achieved through **Optical Layering** rather than traditional shadows. 

1. **The Base**: The Deep Space Navy background.
2. **Glass Tiers**: Surfaces use a 10-20% opacity white fill with a 20px background blur. These surfaces have a 1px "Inner Stroke" (Ice Blue at 30% opacity) on the top and left edges to simulate light hitting the edge of a glass pane.
3. **Glow Planes**: Active data lines and car wireframes sit "above" the glass, utilizing a `drop-shadow` with a spread of 10px in Ice Blue to create a neon-luminescent effect.
4. **Technical Borders**: Use sharp, 1px Silver lines with 45-degree chamfered corners to define container boundaries.

## Shapes

The shape language is **Precision-Engineered**. While standard elements use a 0.25rem (4px) radius to maintain a modern feel, the overall silhouette of components should incorporate "technical cutouts." 

Avoid large, organic curves. Instead, use sharp angles and small radii that suggest machined parts. Large cards should feature "clipped corners" (45-degree notches) at the top-right and bottom-left to reinforce the laboratory equipment aesthetic.

## Components

- **Technical Data Cards**: These are the primary containers. They feature a glassmorphic background, a 1px technical border, and a "Header Bar" with a monospaced ID tag (e.g., `DRAG_COEFF_01`).
- **Live Gauges**: Semi-circular or linear progress bars using a "segmented" fill style. Each segment should glow individually as the value increases.
- **Aero-Control Toggles**: Switches should feel mechanical. Use high-contrast states (Navy for OFF, Ice Blue glow for ON) with a 3D-extruded toggle handle.
- **Heatmap Overlays**: Applied directly to 3D car wireframes. Transitions between colors (Blue to Red) should be smooth gradients but bounded by the wireframe's geometric mesh lines.
- **Technical Buttons**: Ghost buttons with a 1px border. On hover, the background fills with a low-opacity Ice Blue, and the border thickness appears to double via an outer glow.
- **Value Steppers**: Used for adjusting wing angles. These feature "+" and "-" symbols in a monospaced font, encased in a square border with chamfered corners.