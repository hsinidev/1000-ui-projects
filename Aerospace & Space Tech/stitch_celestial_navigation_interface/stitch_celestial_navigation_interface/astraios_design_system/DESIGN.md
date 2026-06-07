---
name: Astraios Design System
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#d0c6ab'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#999077'
  outline-variant: '#4d4732'
  surface-tint: '#e9c400'
  primary: '#fff6df'
  on-primary: '#3a3000'
  primary-container: '#ffd700'
  on-primary-container: '#705e00'
  inverse-primary: '#705d00'
  secondary: '#dfb7ff'
  on-secondary: '#4b007e'
  secondary-container: '#6c11af'
  on-secondary-container: '#d5a4ff'
  tertiary: '#f5f5fc'
  on-tertiary: '#2e3036'
  tertiary-container: '#d9d9e0'
  on-tertiary-container: '#5d5f64'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffe16d'
  primary-fixed-dim: '#e9c400'
  on-primary-fixed: '#221b00'
  on-primary-fixed-variant: '#544600'
  secondary-fixed: '#f1daff'
  secondary-fixed-dim: '#dfb7ff'
  on-secondary-fixed: '#2d004f'
  on-secondary-fixed-variant: '#690bac'
  tertiary-fixed: '#e2e2e9'
  tertiary-fixed-dim: '#c5c6cd'
  on-tertiary-fixed: '#191c20'
  on-tertiary-fixed-variant: '#45474c'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display-lg:
    fontFamily: Space Grotesk
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 40px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.1em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  technical-data:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: 0.15em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.2em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  gutter: 24px
  margin: 40px
---

## Brand & Style
The brand personality of this design system is authoritative yet adventurous, capturing the vastness of deep space through a high-tech lens. It targets researchers, explorers, and space enthusiasts who require a sophisticated, data-rich environment that remains atmospheric and immersive. 

The aesthetic is a hybrid of **Glassmorphism** and **High-Contrast Bold**. It relies on the depth of field created by translucent layers and the sharp, energetic focus of glowing navigational elements. The user experience should feel like operating a terminal from a distant starship—precise, luminous, and expansive.

## Colors
The palette is built on a foundation of Deep Space Black (#050505) to ensure maximum depth and infinite contrast. Solar Gold serves as the primary action color, used sparingly for critical interactions and indicators to mimic the warmth of a distant sun. Nebula Violet provides atmospheric depth and is used for secondary UI elements, gradients, and subtle glow effects. Starlight White is reserved for high-legibility content and micro-copy, ensuring technical data remains sharp against the void.

## Typography
This design system utilizes **Space Grotesk** for all headlines and technical data labels to maintain a cutting-edge, geometric feel. For high-density telemetry and technical readouts, Space Grotesk is set with increased letter spacing to simulate the look of a terminal mono-space font. **Inter** is used for body copy and descriptive text to ensure readability remains high during long-form research. All headings should be treated with a slight "glow" text-shadow when appearing in Solar Gold.

## Layout & Spacing
The layout follows a **Fluid Grid** model, allowing data visualizations to expand across the viewport like a stellar map. A 12-column system is used for standard content, while immersive views utilize a "No Grid" philosophy based on circular anchors and radial alignment. Spacing is generous to prevent "claustrophobia" in the UI, reinforcing the theme of infinite space. Elements are often centered or orbit around a central focal point.

## Elevation & Depth
Depth is achieved through **Glassmorphism** and backdrop filters. Rather than traditional shadows, this design system uses "Tonal Luminance." 

1.  **The Void (Base):** Deep Space Black background.
2.  **Nebula Layer (Low Elevation):** Semi-transparent Nebula Violet overlays with 20px backdrop-blur.
3.  **Command Layer (High Elevation):** Glass panels with thin, 1px Solar Gold "glowing" borders.
4.  **Interactive Peak:** Elements that are active or hovered emit a diffused outer glow, creating a "halo" effect.

## Shapes
The shape language is primarily **Soft** and precision-engineered. Buttons and cards feature subtle 0.25rem corner radii to feel like machined aerospace components. Circular patterns are prominent in navigation, representing orbits and planetary bodies. Large containers may use clipped corners or "octagonal" geometries to evoke futuristic starship architecture.

## Components
- **Buttons:** High-contrast Solar Gold fills for primary actions. Borders are omitted in favor of a subtle outer glow on hover. Text is always uppercase Space Grotesk.
- **Glass Cards:** Containers use a 10% opacity Starlight White background with a heavy backdrop-blur (30px) and a 1px border at 20% opacity.
- **Circular Navigation:** A primary navigation pattern where menu items "orbit" a central logo or status indicator.
- **Input Fields:** Bottom-border only, using Nebula Violet for the inactive state and Solar Gold with a subtle glow for focus.
- **Telemetry Chips:** Small, pill-shaped indicators for data states (e.g., "Active," "Oxygen Low"). These use high-saturation versions of the brand colors with a pulse animation for critical alerts.
- **Star-Charts (Custom Component):** Interactive data visualizations that use thin lines and point-clusters to represent exploration coordinates.