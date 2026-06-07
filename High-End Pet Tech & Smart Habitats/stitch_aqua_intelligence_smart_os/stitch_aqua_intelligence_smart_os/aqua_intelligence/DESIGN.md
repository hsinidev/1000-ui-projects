---
name: Aqua-Intelligence
colors:
  surface: '#021619'
  surface-dim: '#021619'
  surface-bright: '#283d3f'
  surface-container-lowest: '#001113'
  surface-container-low: '#091f21'
  surface-container: '#0e2325'
  surface-container-high: '#192d30'
  surface-container-highest: '#24383b'
  on-surface: '#d0e7ea'
  on-surface-variant: '#b9cbc2'
  inverse-surface: '#d0e7ea'
  inverse-on-surface: '#1f3436'
  outline: '#83958d'
  outline-variant: '#3a4a44'
  surface-tint: '#00e0b3'
  primary: '#fdfffc'
  on-primary: '#00382b'
  primary-container: '#00ffcc'
  on-primary-container: '#00725a'
  inverse-primary: '#006b54'
  secondary: '#afc8f0'
  on-secondary: '#163152'
  secondary-container: '#2f486a'
  on-secondary-container: '#9eb7de'
  tertiary: '#fdffff'
  on-tertiary: '#313030'
  tertiary-container: '#e4e1e0'
  on-tertiary-container: '#656463'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#24ffcd'
  primary-fixed-dim: '#00e0b3'
  on-primary-fixed: '#002118'
  on-primary-fixed-variant: '#00513f'
  secondary-fixed: '#d4e3ff'
  secondary-fixed-dim: '#afc8f0'
  on-secondary-fixed: '#001c3a'
  on-secondary-fixed-variant: '#2f486a'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c9c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474646'
  background: '#021619'
  on-background: '#d0e7ea'
  surface-variant: '#24383b'
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
    lineHeight: '1.3'
  body-base:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  data-mono:
    fontFamily: Geist
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Geist
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
  gutter: 24px
  margin: 40px
  container-max: 1440px
---

## Brand & Style

This design system embodies the intersection of deep-sea exploration and elite laboratory precision. The brand personality is authoritative yet ethereal, catering to high-end reef hobbyists who demand scientific accuracy within a luxurious digital environment. 

The aesthetic is **Fluid-Modern**, blending the structural rigidity of professional automation software with the organic movement of marine life. It utilizes **Glassmorphism** to simulate the refractive qualities of water and glass tanks, creating a multi-layered interface that feels deep and immersive. The emotional response is one of calm control—transforming complex biological data into a serene, high-tech command center.

## Colors

The palette is anchored by **Obsidian Black**, providing a void-like canvas that minimizes light pollution for sensitive aquatic environments. **Deep Azure Blue** is used for structural depth and container backgrounds, mimicking the twilight zone of the ocean. 

**Neon Mint** serves as the primary action and status color, providing high-contrast visibility against the dark base. It is used sparingly for critical data points, active states, and "life-support" indicators. A secondary "Bio-Luminescent" gradient is permitted for data visualizations, transitioning from the Deep Azure to the Neon Mint to represent healthy biological ranges.

## Typography

The typographic hierarchy prioritizes legibility under low-light conditions. **Space Grotesk** is used for headlines and display metrics, lending a futuristic, geometric character to the system. 

For technical readouts and monospaced data (salinity, pH, temperature), **Geist** provides the necessary precision and "developer-grade" feel. **Inter** handles all long-form body text, ensuring that complex automation instructions are easy to digest. High-importance metrics should always utilize the `data-mono` style to ensure digit alignment in live-updating streams.

## Layout & Spacing

The design system utilizes a **12-column fluid grid** with generous margins to create a spacious, premium feel. The spacing rhythm is based on a **4px baseline**, ensuring that even the most data-dense dashboards feel organized and intentional.

Layouts are structured into "Zones": 
1. **The Life Support Rail:** A persistent sidebar for critical metrics.
2. **The Observation Deck:** The main content area for data visualization.
3. **The Control Bay:** A bottom-docked area for manual overrides.

Containers use "Organic Padding"—larger internal padding at the top and bottom of cards to simulate the buoyancy of objects in water.

## Elevation & Depth

Depth is conveyed through **Glassmorphism** rather than traditional drop shadows. Surfaces are layered using varying levels of background blur (12px to 40px) and a subtle 1px inner border ("rim lighting") in a low-opacity Neon Mint or Azure.

- **Surface 0 (Base):** Obsidian Black (#0A0A0A).
- **Surface 1 (Cards):** Deep Azure at 40% opacity with a 20px backdrop blur.
- **Surface 2 (Modals/Popovers):** Deep Azure at 60% opacity with a 40px backdrop blur and a glowing Neon Mint top-edge.

Active elements should appear to "glow" from within, using a soft outer bloom rather than a directional shadow.

## Shapes

The shape language is inspired by **fluid dynamics**. While the primary grid is rectangular for technical precision, corners are softened to a `rounded-lg` (16px) standard to mimic water tension. 

Buttons and toggle tracks utilize fully rounded (pill-shaped) ends to differentiate them from informational cards. Data points in line charts should use circular markers, and progress bars must feature "Liquid Fill" animations, where the leading edge of the bar has a slight wave-like oscillation.

## Components

### Buttons & Inputs
Buttons are rendered as semi-transparent "capsules" with a 1px border. The primary action button features a subtle **Neon Mint glow** that intensifies on hover. Input fields use a "Ghost" style—transparent backgrounds with a simple underline that illuminates when focused.

### Liquid Progress Bars
Used for tank volume, dosing levels, and filtration life. These bars are not static; they feature a slow-moving CSS gradient pulse to simulate flowing water. The fill color shifts from Neon Mint (Optimal) to Deep Azure (Idle) to Amber (Warning).

### Data Tiles
High-precision cards displaying single metrics. They feature a "Sparkline" background—a simplified historical graph of the last 24 hours—rendered in a low-opacity Mint stroke behind the primary value.

### Glow-State Indicators
Status lights do not just change color; they "breathe." Active automation tasks are represented by a pulsing Neon Mint dot with a 12px radial blur, creating a bio-luminescent effect that signals the system is alive and monitoring.

### Glass Modals
Full-screen overlays use a heavy 40px backdrop blur, effectively turning the background aquarium video or data into an abstract wash of color, focusing the user entirely on the configuration task at hand.