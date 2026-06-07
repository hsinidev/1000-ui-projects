---
name: Cryo-Ops Aesthetic
colors:
  surface: '#111416'
  surface-dim: '#111416'
  surface-bright: '#37393c'
  surface-container-lowest: '#0c0e11'
  surface-container-low: '#191c1e'
  surface-container: '#1d2022'
  surface-container-high: '#282a2d'
  surface-container-highest: '#333537'
  on-surface: '#e1e2e5'
  on-surface-variant: '#c1c7ce'
  inverse-surface: '#e1e2e5'
  inverse-on-surface: '#2e3133'
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
  secondary-container: '#454747'
  on-secondary-container: '#b5b5b5'
  tertiary: '#ffebd4'
  on-tertiary: '#442b00'
  tertiary-container: '#fdc97f'
  on-tertiary-container: '#785313'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#c9e6ff'
  primary-fixed-dim: '#9accf3'
  on-primary-fixed: '#001e2f'
  on-primary-fixed-variant: '#0c4b6c'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#ffddb2'
  tertiary-fixed-dim: '#f1be75'
  on-tertiary-fixed: '#291800'
  on-tertiary-fixed-variant: '#624000'
  background: '#111416'
  on-background: '#e1e2e5'
  surface-variant: '#333537'
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
  body-md:
    fontFamily: Geist
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  data-mono:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.2'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  container-padding: 32px
  gutter: 20px
---

## Brand & Style
The ethos of this design system is rooted in "Cold-Tech"—a marriage of medical-grade precision and the sensory experience of thermal therapy. It targets high-performance athletes and recovery specialists who demand professional, trust-centric tools. 

The visual style is a specialized evolution of **Glassmorphism**, specifically tailored to evoke the properties of ice and frosted glass. Surfaces are highly translucent, relying on deep backdrop blurs to maintain legibility against a matte black void. The emotional response is one of calm, sterile reliability and cutting-edge innovation. Every interaction should feel like operating a piece of advanced cryogenic machinery: silent, efficient, and freezing to the touch.

## Colors
This design system utilizes a high-contrast dark palette designed for low-light clinical or athletic environments.

- **Primary (Ice Blue):** Used for primary headings and critical brand moments. It represents the "cold" element of the brand.
- **Secondary (Silver):** Used for secondary text and decorative iconography to provide a metallic, high-tech sheen.
- **Background (Matte Black):** A deep, non-distracting foundation that allows "frost" elements to pop.
- **Accent (Electric Blue):** Reserved exclusively for interactive states (active buttons, toggles, indicators) to provide a "charged" high-energy contrast.

## Typography
The typographic hierarchy blends geometric modernism with technical utility. 

- **Headlines:** Use **Space Grotesk** for its slightly eccentric, technical apertures which reinforce the high-tech narrative.
- **Body:** **Geist** provides a clean, minimal, and ultra-readable experience for descriptions and instructional text.
- **Data Points:** **JetBrains Mono** is used for all telemetry, temperatures, and timing data. This monospaced choice ensures that fluctuating numerical values remain stable and legible during real-time recovery monitoring.

## Layout & Spacing
This design system follows a rigid **12-column fluid grid** for web applications, transitioning to a structured single-column stack for mobile control interfaces. 

The spacing rhythm is strictly based on a 4px baseline, ensuring that technical data aligns perfectly across the horizontal plane. Elements are often grouped into "zones" using the frosted glass panels, with generous internal padding (min 24px) to ensure the high-tech UI feels airy and premium rather than cluttered.

## Elevation & Depth
Depth is created through **diffraction and translucency** rather than traditional shadows. 

1.  **Base Layer:** Matte Black (#121212).
2.  **Middle Layer (Glass Cards):** Translucent fills (`rgba(255, 255, 255, 0.03)`) with a `backdrop-filter: blur(20px)`.
3.  **Border Treatment:** 1px solid strokes in Silver/White with low opacity create the "edge" of the ice. 
4.  **Interactive Layer:** Glowing status indicators use a 0px 0px 12px spread of the Electric Blue accent color to simulate light emitting through frost.

Shadows, when used, are rare and strictly neutral, intended only to lift modals slightly further off the glass plane.

## Shapes
Shapes in this design system are "Soft" (0.25rem - 0.75rem). This avoids the friendliness of overly rounded UI while softening the aggression of sharp 90-degree corners. 

The intent is to mimic precision-machined hardware. Primary glass cards use `rounded-lg` (0.5rem), while buttons and interactive inputs use the base `rounded` (0.25rem). This slight variation helps differentiate structural layout pieces from clickable controls.

## Components
- **Glass Cards:** The primary container. Must have a subtle top-to-bottom gradient stroke to simulate light hitting an edge. Fills should never exceed 5% opacity to maintain "high translucency."
- **Frosted Navigation:** A fixed-top bar with a 40px backdrop blur. The bottom border should be a high-contrast 1px Silver line.
- **Glowing Status Indicators:** Circular elements used for "System Ready" or "Active Cooling." They feature a core color (Electric Blue) with a multi-layered outer glow.
- **Buttons:**
    - *Primary:* Solid Ice Blue with Black text.
    - *Secondary (Ghost):* Frosted background with Silver border and Ice Blue text.
    - *Accent:* Electric Blue with a subtle outer glow on hover.
- **Technical Inputs:** Dark backgrounds with 1px Silver borders that turn Electric Blue on focus. Labels must use the `label-caps` monospaced style.
- **Telemetry Chips:** Small, semi-transparent capsules containing data points like "-110°C," using monospaced typography for precision.