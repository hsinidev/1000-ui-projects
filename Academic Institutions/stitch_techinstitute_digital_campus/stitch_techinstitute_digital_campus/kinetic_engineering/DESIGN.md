---
name: Kinetic Engineering
colors:
  surface: '#10131b'
  surface-dim: '#10131b'
  surface-bright: '#363942'
  surface-container-lowest: '#0b0e16'
  surface-container-low: '#181c23'
  surface-container: '#1c2027'
  surface-container-high: '#272a32'
  surface-container-highest: '#31353d'
  on-surface: '#e0e2ed'
  on-surface-variant: '#c1c6d7'
  inverse-surface: '#e0e2ed'
  inverse-on-surface: '#2d3039'
  outline: '#8b90a0'
  outline-variant: '#414754'
  surface-tint: '#adc7ff'
  primary: '#adc7ff'
  on-primary: '#002e68'
  primary-container: '#4a8eff'
  on-primary-container: '#00285b'
  inverse-primary: '#005bc0'
  secondary: '#c8c6c5'
  on-secondary: '#313030'
  secondary-container: '#4a4949'
  on-secondary-container: '#bab8b7'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#909191'
  on-tertiary-container: '#282a2a'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d8e2ff'
  primary-fixed-dim: '#adc7ff'
  on-primary-fixed: '#001a41'
  on-primary-fixed-variant: '#004493'
  secondary-fixed: '#e5e2e1'
  secondary-fixed-dim: '#c8c6c5'
  on-secondary-fixed: '#1c1b1b'
  on-secondary-fixed-variant: '#474646'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#10131b'
  on-background: '#e0e2ed'
  surface-variant: '#31353d'
typography:
  h1:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  body-main:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  data-label:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: 0.05em
  mono-data:
    fontFamily: Space Grotesk
    fontSize: 13px
    fontWeight: '400'
    lineHeight: '1.4'
    letterSpacing: '0'
  caption:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.02em
spacing:
  base: 4px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 40px
  xl: 64px
  grid-gutter: 20px
  grid-margin: 32px
---

## Brand & Style

The design system is engineered for a high-performance STEM environment, evoking the precision of an aerospace cockpit and the clarity of a blueprint. It targets students and researchers who value technical efficiency and structural integrity. 

The aesthetic is **Technical-Modern**, blending elements of **Modernism** and **Brutalism**. It utilizes high-contrast layouts, structural grid lines, and "active" glowing elements to signal live data and system readiness. The emotional response is one of authority, innovation, and unwavering accuracy.

## Colors

This design system utilizes a high-contrast dark mode as its default state to reduce eye strain during intensive technical work and to allow the Electric Blue to function as a high-visibility signal.

- **Matte Black (#121212):** Used for primary surfaces to create depth and focus.
- **Electric Blue (#007BFF):** Used for primary actions, progress indicators, and "live" system states.
- **Crisp White (#FFFFFF):** Reserved for high-priority typography and essential data points.
- **Neutral Grays:** Used for structural grid lines and secondary information.

## Typography

The typography strategy relies on the utilitarian perfection of **Inter** for narrative and structural content, paired with **Space Grotesk** for technical data and labels. 

Space Grotesk provides the "monospace accent" feel while maintaining superior readability for coordinates, code snippets, and engineering specifications. All labels should be uppercase with slight tracking to mimic technical drafting standards.

## Layout & Spacing

This design system employs a **Fixed Grid** model based on a 12-column architecture. The layout is reinforced by visible, 1px subtle grid lines that define the boundaries of the workspace.

Spacing follows a strict 4px baseline shift. All elements must align to the grid intersections. Use "md" (24px) for standard container padding to ensure technical data does not feel cluttered.

## Elevation & Depth

Hierarchy is established through **Bold Borders** and **Tonal Layering** rather than traditional shadows. 

1.  **Base Layer:** Matte Black (#121212).
2.  **Surface Layer:** A slightly lighter charcoal (#1E1E1E) with a 1px solid border (#2A2A2A).
3.  **Active Elevation:** Components do not "lift" via shadows; instead, they gain a 1px Electric Blue border and a subtle outer "glow" (4px-8px blur) of the same color to indicate focus or activity.
4.  **Glassmorphism:** Use only for transient overlays (modals/drawers) with a heavy blur (20px) and 80% opacity to maintain the technical "HUD" feel.

## Shapes

The shape language is strictly **Sharp (0px)**. Engineering precision is communicated through 90-degree angles and clean terminations. 

Avoid all rounded corners for buttons, inputs, and cards. This reinforces the "industrial equipment" aesthetic and ensures that the 1px grid lines align perfectly with component edges.

## Components

- **Buttons:** Rectangular with no radius. Primary buttons use a solid Electric Blue fill with White text. Secondary buttons are ghost-style with a White border.
- **Inputs:** Matte black background with a 1px gray border. On focus, the border changes to Electric Blue with a subtle glow. Labels must use the "data-label" typography style above the field.
- **Chips:** Small, rectangular tags with a 1px border. Status chips use the monospace font to display "SYSTEM_OK" or "ERR_404" style strings.
- **Cards:** Defined by 1px borders and visible grid-alignment. Use a "corner accent" (a 4px blue L-shape in the top-right corner) for featured content.
- **Lists:** Separated by 1px horizontal lines. Hover states should trigger a full-row background shift to #1E1E1E.
- **Data Visualizers:** All charts and graphs must use Electric Blue for primary data lines, with secondary data in White or Gray. Use subtle grid backgrounds within all chart containers.