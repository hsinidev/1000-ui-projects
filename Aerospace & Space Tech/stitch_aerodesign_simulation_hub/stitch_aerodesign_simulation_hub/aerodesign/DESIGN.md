---
name: AeroDesign
colors:
  surface: '#011230'
  surface-dim: '#011230'
  surface-bright: '#293958'
  surface-container-lowest: '#000d27'
  surface-container-low: '#091b39'
  surface-container: '#0e1f3d'
  surface-container-high: '#192a48'
  surface-container-highest: '#253453'
  on-surface: '#d8e2ff'
  on-surface-variant: '#c5c6cd'
  inverse-surface: '#d8e2ff'
  inverse-on-surface: '#20304f'
  outline: '#8f9097'
  outline-variant: '#44474d'
  surface-tint: '#b9c7e4'
  primary: '#b9c7e4'
  on-primary: '#233148'
  primary-container: '#0a192f'
  on-primary-container: '#74829d'
  inverse-primary: '#515f78'
  secondary: '#c6c6c7'
  on-secondary: '#2f3131'
  secondary-container: '#454747'
  on-secondary-container: '#b4b5b5'
  tertiary: '#e7bf99'
  on-tertiary: '#432b10'
  tertiary-container: '#281400'
  on-tertiary-container: '#9d7b5a'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d6e3ff'
  primary-fixed-dim: '#b9c7e4'
  on-primary-fixed: '#0d1c32'
  on-primary-fixed-variant: '#39475f'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#ffdcbd'
  tertiary-fixed-dim: '#e7bf99'
  on-tertiary-fixed: '#2b1701'
  on-tertiary-fixed-variant: '#5d4124'
  background: '#011230'
  on-background: '#d8e2ff'
  surface-variant: '#253453'
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
    lineHeight: '1.6'
  data-mono:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.02em
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.2'
spacing:
  grid-unit: 4px
  gutter: 16px
  margin-mobile: 16px
  margin-desktop: 32px
  panel-padding: 24px
---

## Brand & Style
The design system is engineered for the high-precision world of aerospace engineering and Computational Fluid Dynamics (CFD). It evokes a sense of technical mastery, absolute accuracy, and scientific rigor. The aesthetic is rooted in **Modern Minimalism** mixed with **Strict Engineering** principles, prioritizing data density and clarity over decorative elements.

The UI should feel like a high-performance instrument—unobtrusive but powerful. It targets aerospace engineers, researchers, and fluid dynamics specialists who require a low-fatigue environment for monitoring long-duration simulations and analyzing complex 3D flow data. The visual language utilizes a "HUD" (Heads-Up Display) philosophy: high-contrast elements, razor-sharp borders, and a logical hierarchy that guides the eye through dense datasets without friction.

## Colors
This design system utilizes a sophisticated dark mode by default to reduce eye strain during long simulation reviews and to make the heatmap gradients pop.

- **Primary:** Deep Navy (#0A192F) serves as the foundation, providing a deep, stable background that recedes behind active data.
- **Secondary:** Crisp White (#FFFFFF) is reserved for high-priority typography and critical UI controls.
- **Heatmap Palette:** A strictly calibrated gradient from Blue (low pressure/velocity) to Red (high pressure/velocity) is used for data visualization. This palette must be used consistently across 3D overlays and 2D charts to ensure cross-functional data recognition.
- **Surface Accents:** Mid-tone navies and cool grays are used for panel borders and inactive states to maintain a high-contrast but professional environment.

## Typography
The typography strategy prioritizes legibility in high-density environments. 

- **Headlines:** Use **Space Grotesk** to provide a technical, geometric character to page headers and major section titles. Its futuristic but stable letterforms reinforce the aerospace theme.
- **Body & Technical Data:** **Inter** is the workhorse for all technical readout and interface text. Its high x-height and neutral design ensure that even the smallest tabular data remains legible on mobile screens.
- **Monospaced Contexts:** While Inter is used for general UI, ensure that numerical data points in tables are set with tabular lining (tnum) to keep columns aligned. Labels use uppercase styling with slight tracking to differentiate from interactive body text.

## Layout & Spacing
The layout is governed by a **Strict Engineering Grid** based on a 4px baseline. This ensures that every element, from a chart axis to a button, feels deliberate and aligned.

- **Fluid Grid:** The main viewport uses a 12-column fluid system for the dashboard, allowing simulation videos to expand to the full width of the screen.
- **Side Panels:** Technical controls and data trees are housed in fixed-width side panels (typically 320px) to ensure that control inputs remain consistent regardless of screen resolution.
- **Mobile First:** On mobile devices, the 12-column grid collapses into a single-column scroll, with horizontal swiping enabled specifically for wide data tables and high-resolution charts to prevent scaling issues.

## Elevation & Depth
In this design system, depth is communicated through **Tonal Layers** and **Bold Borders** rather than traditional shadows. This maintains a "flat-technical" aesthetic suitable for engineering software.

- **Base Layer:** Deep Navy (#0A192F).
- **Surface Layer:** Neutral Navy (#112240) for cards, sidebars, and header areas.
- **Borders:** Subtle, 1px solid borders (#233554) are used to define boundaries. In high-priority states, borders may glow slightly using the accent colors to indicate active simulation or selection.
- **Overlays:** 3D model controls and HUD elements use a slight backdrop-blur (8px) to separate the interface from the complex visual noise of the simulation video behind it.

## Shapes
To reinforce the scientific and "built" nature of the software, the design system utilizes **Sharp (0px)** roundedness. Every corner is a precise right angle. This maximizes usable space for data displays and reflects the precision required in fluid dynamics calculations. 

The only exception to the sharp-edge rule is for circular status indicators (e.g., "Recording" or "Live" pulses), which should remain perfect circles to stand out against the rectilinear grid.

## Components
- **Buttons:** Primary buttons are Solid White with Navy text. Secondary buttons are outlined with 1px borders. Use a "cut-corner" hover effect rather than a color shift to maintain the technical vibe.
- **Data Tables:** High-density with Zebra-striping (using #112240). Columns must support sorting icons and units of measurement (e.g., m/s, Pa) in a muted text style.
- **Input Fields:** Bottom-border only or full-border with no fill. Focus states should use the "Flow Velocity" cyan accent color for the border.
- **Charts:** Use thin line weights (1px to 1.5px). Tooltips should be high-contrast (White background, Navy text) to pop against the dark simulation environment.
- **Simulation Controls:** Use standard media player metaphors (Play, Pause, Scrub) but styled with minimalist iconography. The "Scrub" bar should be a heatmap gradient representing the simulation timeline's pressure average.
- **Chips:** Small, rectangular tags with 1px borders used for indicating simulation parameters (e.g., "Re=10,000", "Mach 0.8").