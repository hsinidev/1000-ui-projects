---
name: Quantum Precision
colors:
  surface: '#081425'
  surface-dim: '#081425'
  surface-bright: '#2f3a4c'
  surface-container-lowest: '#040e1f'
  surface-container-low: '#111c2d'
  surface-container: '#152031'
  surface-container-high: '#1f2a3c'
  surface-container-highest: '#2a3548'
  on-surface: '#d8e3fb'
  on-surface-variant: '#c7c6cc'
  inverse-surface: '#d8e3fb'
  inverse-on-surface: '#263143'
  outline: '#909096'
  outline-variant: '#46464c'
  surface-tint: '#c3c6d7'
  primary: '#c3c6d7'
  on-primary: '#2c303d'
  primary-container: '#0a0e1a'
  on-primary-container: '#777b8a'
  inverse-primary: '#5a5e6d'
  secondary: '#c4c6cd'
  on-secondary: '#2d3136'
  secondary-container: '#44474d'
  on-secondary-container: '#b3b5bc'
  tertiary: '#00e38f'
  on-tertiary: '#003920'
  tertiary-container: '#001207'
  on-tertiary-container: '#008d57'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dfe2f3'
  primary-fixed-dim: '#c3c6d7'
  on-primary-fixed: '#171b28'
  on-primary-fixed-variant: '#434654'
  secondary-fixed: '#e0e2e9'
  secondary-fixed-dim: '#c4c6cd'
  on-secondary-fixed: '#191c21'
  on-secondary-fixed-variant: '#44474d'
  tertiary-fixed: '#53ffab'
  tertiary-fixed-dim: '#00e38f'
  on-tertiary-fixed: '#002111'
  on-tertiary-fixed-variant: '#005231'
  background: '#081425'
  on-background: '#d8e3fb'
  surface-variant: '#2a3548'
typography:
  display-xl:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: 32px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
  data-mono:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  container-max: 1440px
  gutter: 24px
  margin: 40px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style

The brand personality is defined by three pillars: **Impregnability**, **Scientific Precision**, and **Technological Superiority**. This design system targets high-level security architects and government stakeholders who require an interface that feels as secure as the encryption it manages. 

The visual style combines **Minimalism** with **Glassmorphism** to create a "command center" aesthetic. This approach uses heavy whitespace to isolate critical data points while employing translucent layers to suggest the depth and complexity of quantum mathematics. The aesthetic avoids decorative fluff in favor of functional geometry and mathematical patterns.

## Colors

The palette is strictly high-contrast to ensure clarity under intense scrutiny. 

- **Midnight Blue (#0A0E1A):** Used for the primary background to evoke the vastness of deep space and the stability of a secure vault.
- **Silver (#C0C2C9):** The primary color for typography and structural borders. It provides a metallic, authoritative finish that contrasts sharply against the dark void.
- **Laser-Green (#00F59B):** A high-vibrancy accent reserved exclusively for "active" states, successful encryption status, and critical data visualizations. 
- **Subtle Surface (#1E293B):** Used for container backgrounds to create a tiered hierarchy of information.

## Typography

This design system utilizes a dual-font strategy to balance futuristic character with extreme legibility.

- **Space Grotesk** is used for headlines and data points. Its technical, geometric construction echoes the mathematical nature of quantum cryptography.
- **Inter** is the workhorse for body copy, reports, and whitepapers. It is chosen for its neutral, systematic clarity, ensuring that complex technical documentation remains readable at small sizes.

All labels should be set in uppercase with slight tracking (letter-spacing) to mimic the appearance of technical schematics.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model to maintain a sense of rigid authority. Content is centered within a 1440px container using a 12-column grid. 

A strict 8px spacing scale (The Octal System) governs all spatial relationships. This consistency ensures the UI feels engineered rather than "designed." Backgrounds should feature subtle, non-distracting fractal patterns or mathematical grids (e.g., a 32px dot grid) to provide a sense of scale and depth without cluttering the foreground.

## Elevation & Depth

In this design system, depth is conveyed through **Glassmorphism** and **Tonal Layers** rather than traditional shadows.

1.  **Base Layer:** Midnight Blue with a subtle fractal noise texture.
2.  **Surface Layer:** Semi-transparent Midnight Blue with a `backdrop-filter: blur(12px)`.
3.  **Borders:** 1px solid Silver at 10% to 20% opacity.
4.  **Interaction Glow:** Rather than shadows, active elements emit a soft "Laser-Green" outer glow (e.g., `0px 0px 15px rgba(0, 245, 155, 0.3)`) to suggest high-energy states.

Stacked elements should use increasing border-opacity to signal elevation, creating the illusion of translucent panes of glass floating in a dark environment.

## Shapes

The shape language is **Precision-focused (Soft)**. Elements use a 0.25rem (4px) corner radius to strike a balance between industrial sharpness and modern UI standards. 

- **Buttons & Inputs:** Use the standard 4px radius.
- **Large Cards:** May use an 8px radius (`rounded-lg`) to soften the density of complex data.
- **Interactive Gauge:** Must be perfectly circular to represent the cyclical nature of mathematical calculations.

Avoid fully rounded "pill" shapes, as they appear too casual for an authoritative security platform.

## Components

### Buttons
Primary buttons feature a solid Laser-Green background with Midnight Blue text for maximum contrast. Secondary buttons use a Silver "ghost" style with a 1px border. All buttons should have a high-energy hover state involving a subtle increase in glow intensity.

### High-Tech Cards
Cards should be treated as "Data Containers." They feature a hairline Silver border and a 5% opacity Silver fill. Background mathematical patterns should be visible through the card via a backdrop blur.

### Data-Heavy Tables
Tables must prioritize density and scanning. Row hover states should use a faint Laser-Green tint. Headers are uppercase `label-sm` typography with a solid 1px Silver bottom border.

### Quantum Readiness Gauge
The signature component. An interactive, segmented radial chart. Segments pulse with Laser-Green when "Secure" and shift to a muted Silver when "At Risk." The center of the gauge displays a percentage in `display-xl` Space Grotesk.

### Inputs
Input fields are dark and recessed. The focus state is a 1px Laser-Green border with no glow, maintaining a sharp, disciplined appearance.