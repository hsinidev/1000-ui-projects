---
name: Aero-Cycle
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#20201f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e5e2e1'
  on-surface-variant: '#b9cacb'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#849495'
  outline-variant: '#3a494b'
  surface-tint: '#00dbe7'
  primary: '#e1fdff'
  on-primary: '#00363a'
  primary-container: '#00f2ff'
  on-primary-container: '#006a71'
  inverse-primary: '#00696f'
  secondary: '#c6c6c7'
  on-secondary: '#2f3131'
  secondary-container: '#454747'
  on-secondary-container: '#b4b5b5'
  tertiary: '#f9f7f6'
  on-tertiary: '#303030'
  tertiary-container: '#dddada'
  on-tertiary-container: '#605f5f'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#74f5ff'
  primary-fixed-dim: '#00dbe7'
  on-primary-fixed: '#002022'
  on-primary-fixed-variant: '#004f54'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#e4e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#474747'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  display-xl:
    fontFamily: Space Grotesk
    fontSize: 4.5rem
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 2.5rem
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 1.5rem
    fontWeight: '500'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Inter
    fontSize: 1.125rem
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 1rem
    fontWeight: '400'
    lineHeight: '1.6'
  data-mono:
    fontFamily: Space Grotesk
    fontSize: 1rem
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Space Grotesk
    fontSize: 0.75rem
    fontWeight: '600'
    lineHeight: '1'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 24px
  margin: 40px
  container-max: 1440px
---

## Brand & Style
The brand personality is clinical, elite, and obsessed with marginal gains. It targets professional cyclists and engineers who demand precision over decoration. This design system evokes the feeling of a wind-tunnel control room: dark, focused, and high-velocity.

The UI style merges **Minimalism** with **Glassmorphism**. Surfaces are treated like polycarbonate visors or carbon fiber shells—lightweight but structurally sound. To visualize performance, the design incorporates "airflow" vector lines—ultra-thin, 0.5pt strokes with linear gradients that guide the eye across data streams, simulating aerodynamic drag and laminar flow.

## Colors
This design system utilizes a high-contrast dark mode to reduce eye strain during technical analysis and to make the "Electric Cyan" accents feel luminous.

- **Primary (Electric Cyan):** Reserved for active states, critical data points, and "velocity" indicators. It represents the energy and tech-forward nature of the lab.
- **Surface Palette:** A duo of Matte Greys (#1A1A1A for the base canvas and #2C2C2C for elevated modules) creates a sophisticated, non-reflective environment.
- **Functional White:** Used sparingly for primary typography and high-priority readouts to ensure maximum legibility against the dark void.

## Typography
The typographic strategy balances the technical edge of **Space Grotesk** with the utilitarian clarity of **Inter**. 

Space Grotesk is used for headlines and data labels to provide a futuristic, geometric rhythm. Inter handles all long-form technical descriptions and body copy to ensure readability isn't sacrificed for style. Numerical data should always utilize the "data-mono" style, ensuring that digits align perfectly in tables and live-tracking dashboards, mimicking a digital stopwatch or cyclocomputer.

## Layout & Spacing
The layout follows a **Fixed Grid** model (12 columns) to maintain the precision of a technical lab report. Spacing is governed by a 4px base unit, ensuring every element is mathematically aligned. 

Large "safe zones" are used between data modules to prevent visual clutter, allowing the user to focus on specific performance metrics. Layouts should prioritize horizontal movement, echoing the forward momentum of a cyclist.

## Elevation & Depth
Depth is achieved through **Glassmorphism** and **Tonal Layering** rather than traditional shadows.

1.  **Level 0 (Floor):** The base matte #1A1A1A surface.
2.  **Level 1 (Modules):** #2C2C2C panels with a 1px stroke of 10% white to define edges.
3.  **Level 2 (Overlays/Modals):** Semi-transparent (70% opacity) matte grey with a 20px backdrop blur. This simulates a high-tech head-up display (HUD).
4.  **Accents:** Thin Cyan gradients (100% to 0% opacity) are used to "lift" specific data lines off the canvas, creating a sense of three-dimensional airflow.

## Shapes
Shapes are "Soft" (4px - 12px radius). This avoids the aggression of sharp corners while maintaining a professional, engineered feel. Buttons and input fields use the `rounded-lg` (8px) setting. Data visualization containers use the `rounded-xl` (12px) setting to create a subtle frame around complex charts. Icons and small status indicators should remain sharp or use minimal rounding to maintain a "technical tool" aesthetic.

## Components
- **Buttons:** Primary buttons are Solid Cyan with Black text. Secondary buttons are "Ghost" style with a 1px White border and hover-state Cyan glow.
- **Data Cards:** Utilize the Glassmorphism effect. Headers within cards should feature a subtle "airflow" line (a 1px horizontal gradient) separating the title from the data.
- **Input Fields:** Dark background (#1A1A1A) with a bottom-border only, which glows Cyan when focused.
- **Status Chips:** Small, pill-shaped markers for "In-Sync," "Aero-Optimal," or "Calibration Required."
- **Progress Bars:** Ultra-thin (2px) lines using a gradient from #1A1A1A to #00F2FF to show real-time metric completion.
- **Specialty Component (The Wind Gauge):** A circular data visualization representing yaw angle and wind resistance, using precise vector lines and Electric Cyan needles.