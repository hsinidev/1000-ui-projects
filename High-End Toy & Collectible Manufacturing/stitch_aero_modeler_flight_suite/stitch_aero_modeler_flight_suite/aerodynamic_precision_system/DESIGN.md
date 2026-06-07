---
name: Aerodynamic Precision System
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
  on-surface-variant: '#c5c6cd'
  inverse-surface: '#e0e3e5'
  inverse-on-surface: '#2d3133'
  outline: '#8f9097'
  outline-variant: '#44474d'
  surface-tint: '#b9c7e4'
  primary: '#b9c7e4'
  on-primary: '#233148'
  primary-container: '#0a192f'
  on-primary-container: '#74829d'
  inverse-primary: '#515f78'
  secondary: '#ffb595'
  on-secondary: '#571e00'
  secondary-container: '#fd6600'
  on-secondary-container: '#541d00'
  tertiary: '#c8c6c5'
  on-tertiary: '#303030'
  tertiary-container: '#191919'
  on-tertiary-container: '#838281'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d6e3ff'
  primary-fixed-dim: '#b9c7e4'
  on-primary-fixed: '#0d1c32'
  on-primary-fixed-variant: '#39475f'
  secondary-fixed: '#ffdbcd'
  secondary-fixed-dim: '#ffb595'
  on-secondary-fixed: '#351000'
  on-secondary-fixed-variant: '#7c2e00'
  tertiary-fixed: '#e4e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#474746'
  background: '#101415'
  on-background: '#e0e3e5'
  surface-variant: '#323537'
typography:
  headline-xl:
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
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  data-mono:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 4px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 40px
  xl: 64px
  gutter: 20px
  margin: 32px
---

## Brand & Style

This design system is engineered for the high-stakes world of professional aerospace modeling and drone piloting. It evokes a "cockpit" mental model—highly technical, performance-driven, and uncompromising in its clarity. The brand personality is elite and authoritative, catering to professionals who view their equipment as precision instruments rather than toys.

The visual style is a fusion of **Minimalism** and **Technical Industrialism**. It utilizes high-contrast interfaces to ensure legibility in various lighting conditions (field use), while subtle carbon fiber textures and vector line graphics imply velocity and structural integrity. Every pixel should feel as though it was machined to a specific tolerance, avoiding unnecessary decorative fluff in favor of data-rich, functional aesthetics.

## Colors

The palette is optimized for a dark-mode-first environment, reflecting the high-end nature of professional avionics. 

- **Primary (Deep Navy):** Used for the core canvas and foundational surfaces, providing a deep, stable background that reduces eye strain.
- **Secondary (Safety Orange):** Reserved strictly for critical actions, status alerts, and telemetry highlights. It is the "human-interface" color that guides the eye to vital information.
- **Tertiary (Carbon Fiber Grey):** Used for structural elements, containers, and "machined" components.
- **Neutral (Cool White):** Applied to typography and data points for maximum contrast against the dark base.

Use subtle linear gradients (Deep Navy to Carbon Grey) to create a sense of metallic curvature on large surfaces.

## Typography

Typography in this design system functions as a readout instrument. 

**Space Grotesk** is used for headlines and data points. Its geometric, slightly eccentric forms lend a futuristic, technical edge that mimics modern heads-up displays (HUDs). For telemetry and specific metrics, use the `data-mono` or `label-caps` styles to ensure characters align vertically for quick scanning.

**Inter** serves as the workhorse for body copy and instructional text. It provides the necessary neutral balance to the more aggressive headlines, ensuring that long-form documentation or specifications remain highly readable. All labels should lean toward uppercase with slight tracking (letter-spacing) to mimic engraved serial numbers on hardware.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model to mirror the rigid constraints of aerospace engineering. A 12-column grid is standard for desktop, shifting to a 4-column grid for mobile flight-controllers.

Spacing is governed by a strict 4px baseline rhythm. Margins and gutters are kept relatively tight to maximize information density—allowing pilots and engineers to view multiple data streams (battery, signal, GPS, velocity) simultaneously without scrolling. Containers should utilize `sm` (16px) or `md` (24px) padding to maintain a compact, "instrument panel" feel.

## Elevation & Depth

Hierarchy is established through **Tonal Layers** and **Low-Contrast Outlines** rather than traditional shadows. In an "engineered" environment, light sources are often internal or ambient.

1.  **Base Layer:** Deep Navy (#0A192F) for the global background.
2.  **Container Layer:** Carbon Fiber Grey (#2B2B2B) with a subtle 1px border (#FFFFFF, 10% opacity) to define edges.
3.  **Active Layer:** Safety Orange (#FF6700) used for thin "glow" borders or 2px underlines to indicate focus.

Use backdrop blurs (Glassmorphism) sparingly—only for transient UI like dropdowns or overlays—to simulate the look of a polycarbonate HUD placed over a cockpit view.

## Shapes

The shape language is "Soft-Technical." Elements use a 0.25rem (4px) base radius, reflecting the "chamfered edge" of machined aluminum or molded carbon fiber. 

Avoid full circles except for status indicators or toggle pips. Rectangular elements should feel structural. Buttons and input fields should maintain these crisp, subtle corners to suggest precision. For decorative vector lines, use 45-degree angles to imply aerodynamic flow and movement.

## Components

**Buttons:** Primary buttons are solid Safety Orange with black text. Secondary buttons are ghost-style with a Carbon Grey border that shifts to white on hover. Use a "clipped corner" effect via CSS clip-path for high-tier CTA buttons to mimic aerodynamic surfaces.

**Input Fields:** Dark backgrounds with a 1px bottom border. When focused, the border transitions to Safety Orange. Labels are always `label-caps` and positioned above the field.

**Chips/Badges:** Used for status (e.g., "STABLE," "LOCKED"). These should be rectangular with no rounding, using a semi-transparent fill of the status color (e.g., green for signal, red for low battery).

**Cards:** Use a subtle carbon fiber pattern overlay at 5% opacity. Headers within cards should be separated by a 1px technical line that doesn't quite reach the edges, implying a blueprint aesthetic.

**Specialty - Telemetry Gauges:** Vertical and horizontal bar charts with segmented increments. Each segment represents a unit of power or signal, filling with Safety Orange as values increase.